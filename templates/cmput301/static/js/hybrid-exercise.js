/*
 * CMPUT 301 hybrid participation-exercise generator.
 *
 * The page supplies the canonical exercise URL and the unstamped PNG URL using
 * data attributes. This script sends `studentNumber;exerciseUrl` to the course
 * authentication service and places the student number, exercise ID, and
 * returned authentication code in a P2 QR,
 * stamps it onto the PNG in memory, and exposes the result as a browser
 * download. If authentication is unavailable, the QR contains a visible error.
 */
(function () {
  "use strict";

  const DEFAULT_AUTH_URL = "https://pizza.cs.ualberta.ca/auth/";
  const DEFAULT_QR_LIBRARY_URL =
    "https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js";
  const DEFAULT_QR_LIBRARY_INTEGRITY =
    "sha384-3zSEDfvllQohrq0PHL1fOXJuC/jSOO34H46t6UQfobFOmxE5BpjjaIJY5F2/bMnU";
  const STUDENT_NUMBER_PATTERN = /^\d{7}$/;
  const MAX_AUTH_CODE_LENGTH = 512;
  const MAX_EXERCISE_ID_LENGTH = 128;
  const GENERATION_ERROR_MARKER = "$error$";
  const AUTH_SERVER_OFFLINE_ERROR =
    `${GENERATION_ERROR_MARKER}:auth-server-offline`;
  const AUTH_TIMEOUT_MS = 12000;

  let qrLibraryPromise;

  function requiredElement(root, role) {
    const element = root.querySelector(`[data-role="${role}"]`);
    if (!element) {
      throw new Error(`Hybrid exercise markup is missing data-role="${role}".`);
    }
    return element;
  }

  function setStatus(statusElement, message, state) {
    statusElement.textContent = message;
    statusElement.dataset.state = state;
  }

  function positiveInteger(value, name) {
    if (value === undefined || value === "") {
      return null;
    }
    const parsed = Number.parseInt(value, 10);
    if (!Number.isInteger(parsed) || parsed < 0) {
      throw new Error(`${name} must be a non-negative integer.`);
    }
    return parsed;
  }

  function ensureQrLibrary(root) {
    if (typeof window.QRCode === "function") {
      return Promise.resolve(window.QRCode);
    }
    if (qrLibraryPromise) {
      return qrLibraryPromise;
    }

    const libraryUrl =
      root.dataset.qrLibraryUrl || DEFAULT_QR_LIBRARY_URL;
    qrLibraryPromise = new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = libraryUrl;
      script.async = true;
      script.crossOrigin = "anonymous";
      script.referrerPolicy = "no-referrer";
      if (libraryUrl === DEFAULT_QR_LIBRARY_URL) {
        script.integrity = DEFAULT_QR_LIBRARY_INTEGRITY;
      }
      script.addEventListener("load", () => {
        if (typeof window.QRCode !== "function") {
          reject(new Error("The QR library loaded without defining QRCode."));
          return;
        }
        resolve(window.QRCode);
      });
      script.addEventListener("error", () => {
        qrLibraryPromise = undefined;
        reject(new Error("The QR-generation library could not be loaded."));
      });
      document.head.appendChild(script);
    });
    return qrLibraryPromise;
  }

  function loadImage(url) {
    return new Promise((resolve, reject) => {
      const image = new Image();
      image.crossOrigin = "anonymous";
      image.addEventListener("load", () => resolve(image), { once: true });
      image.addEventListener(
        "error",
        () => reject(new Error(`The exercise template could not be loaded: ${url}`)),
        { once: true },
      );
      image.src = url;
    });
  }

  function imageElementToCanvas(image, width, height) {
    const canvas = document.createElement("canvas");
    canvas.width = width;
    canvas.height = height;
    const context = canvas.getContext("2d");
    if (!context) {
      throw new Error("This browser does not support two-dimensional canvas.");
    }
    context.drawImage(image, 0, 0, width, height);
    return canvas;
  }

  function findPlaceholderRect(image, width, height) {
    const source = imageElementToCanvas(image, width, height);
    const context = source.getContext("2d", { willReadFrequently: true });
    if (!context) {
      throw new Error("This browser cannot inspect the exercise template.");
    }

    const pixels = context.getImageData(0, 0, width, height).data;
    const pixelCount = width * height;
    const dark = new Uint8Array(pixelCount);
    const visited = new Uint8Array(pixelCount);
    const threshold = 190;
    for (let index = 0, offset = 0; index < pixelCount; index += 1, offset += 4) {
      const luminance =
        pixels[offset] * 0.2126 +
        pixels[offset + 1] * 0.7152 +
        pixels[offset + 2] * 0.0722;
      dark[index] = pixels[offset + 3] > 0 && luminance < threshold ? 1 : 0;
    }

    const shortSide = Math.min(width, height);
    const minimumSide = Math.round(shortSide * 0.07);
    const maximumSide = Math.round(shortSide * 0.32);
    const candidates = [];

    function borderCoverage(x, y, boxWidth, boxHeight) {
      const band = Math.max(2, Math.round(shortSide * 0.002));

      function hasDarkPixel(sampleX, sampleY, horizontal) {
        for (let delta = -band; delta <= band; delta += 1) {
          const px = horizontal ? sampleX : sampleX + delta;
          const py = horizontal ? sampleY + delta : sampleY;
          if (px >= 0 && px < width && py >= 0 && py < height) {
            if (dark[py * width + px]) {
              return true;
            }
          }
        }
        return false;
      }

      let top = 0;
      let bottom = 0;
      for (let px = x; px < x + boxWidth; px += 1) {
        top += hasDarkPixel(px, y, true) ? 1 : 0;
        bottom += hasDarkPixel(px, y + boxHeight - 1, true) ? 1 : 0;
      }

      let left = 0;
      let right = 0;
      for (let py = y; py < y + boxHeight; py += 1) {
        left += hasDarkPixel(x, py, false) ? 1 : 0;
        right += hasDarkPixel(x + boxWidth - 1, py, false) ? 1 : 0;
      }

      return [
        top / boxWidth,
        bottom / boxWidth,
        left / boxHeight,
        right / boxHeight,
      ];
    }

    for (let start = 0; start < pixelCount; start += 1) {
      if (!dark[start] || visited[start]) {
        continue;
      }

      const stack = [start];
      visited[start] = 1;
      let componentPixels = 0;
      let minX = width;
      let maxX = -1;
      let minY = height;
      let maxY = -1;

      while (stack.length) {
        const current = stack.pop();
        const x = current % width;
        const y = Math.floor(current / width);
        componentPixels += 1;
        minX = Math.min(minX, x);
        maxX = Math.max(maxX, x);
        minY = Math.min(minY, y);
        maxY = Math.max(maxY, y);

        const neighbors = [];
        if (x > 0) neighbors.push(current - 1);
        if (x + 1 < width) neighbors.push(current + 1);
        if (y > 0) neighbors.push(current - width);
        if (y + 1 < height) neighbors.push(current + width);
        for (const neighbor of neighbors) {
          if (dark[neighbor] && !visited[neighbor]) {
            visited[neighbor] = 1;
            stack.push(neighbor);
          }
        }
      }

      const boxWidth = maxX - minX + 1;
      const boxHeight = maxY - minY + 1;
      if (
        boxWidth < minimumSide ||
        boxHeight < minimumSide ||
        boxWidth > maximumSide ||
        boxHeight > maximumSide
      ) {
        continue;
      }

      const aspectRatio = boxWidth / boxHeight;
      const fillRatio = componentPixels / (boxWidth * boxHeight);
      if (aspectRatio < 0.82 || aspectRatio > 1.22 || fillRatio > 0.2) {
        continue;
      }

      const coverage = borderCoverage(minX, minY, boxWidth, boxHeight);
      const minimumCoverage = Math.min(...coverage);
      if (minimumCoverage < 0.78) {
        continue;
      }

      const averageCoverage =
        coverage.reduce((total, value) => total + value, 0) / coverage.length;
      const relativeSize = ((boxWidth + boxHeight) / 2) / shortSide;
      const score =
        averageCoverage * 5 -
        Math.abs(1 - aspectRatio) * 3 -
        Math.abs(0.19 - relativeSize) * 2 -
        fillRatio;
      candidates.push({
        x: minX,
        y: minY,
        width: boxWidth,
        height: boxHeight,
        score,
      });
    }

    candidates.sort((first, second) => second.score - first.score);
    if (!candidates.length) {
      throw new Error(
        "The Replace Me square could not be detected in this exercise template.",
      );
    }
    return candidates[0];
  }

  async function renderQrCode(root, payload, size) {
    const QRCode = await ensureQrLibrary(root);
    const quietZone = Math.max(8, Math.round(size * 0.06));
    const qrSize = size - quietZone * 2;
    if (qrSize < 64) {
      throw new Error("The configured QR size is too small.");
    }

    const holder = document.createElement("div");
    new QRCode(holder, {
      text: payload,
      width: qrSize,
      height: qrSize,
      colorDark: "#000000",
      colorLight: "#ffffff",
      correctLevel: QRCode.CorrectLevel.M,
    });

    let encoded = holder.querySelector("canvas");
    if (!encoded) {
      const encodedImage = holder.querySelector("img");
      if (!encodedImage) {
        throw new Error("The QR library did not produce an image.");
      }
      if (!encodedImage.complete) {
        await new Promise((resolve, reject) => {
          encodedImage.addEventListener("load", resolve, { once: true });
          encodedImage.addEventListener("error", reject, { once: true });
        });
      }
      encoded = imageElementToCanvas(encodedImage, qrSize, qrSize);
    }

    const result = document.createElement("canvas");
    result.width = size;
    result.height = size;
    const context = result.getContext("2d");
    if (!context) {
      throw new Error("This browser does not support two-dimensional canvas.");
    }
    context.fillStyle = "#ffffff";
    context.fillRect(0, 0, size, size);
    context.imageSmoothingEnabled = false;
    context.drawImage(encoded, quietZone, quietZone, qrSize, qrSize);
    return result;
  }

  function validateExerciseId(exerciseId) {
    if (
      !exerciseId ||
      exerciseId !== exerciseId.trim() ||
      exerciseId.length > MAX_EXERCISE_ID_LENGTH ||
      exerciseId.includes(",") ||
      /[\x00-\x1f\x7f]/.test(exerciseId)
    ) {
      throw new Error("The page specifies an invalid exercise ID.");
    }
  }

  function buildHybridPayload(studentNumber, exerciseId, authCode) {
    if (!STUDENT_NUMBER_PATTERN.test(studentNumber)) {
      throw new Error("Student number must contain exactly seven digits.");
    }
    validateExerciseId(exerciseId);
    if (
      !authCode ||
      authCode !== authCode.trim() ||
      authCode.length > MAX_AUTH_CODE_LENGTH ||
      /[\x00-\x1f\x7f]/.test(authCode)
    ) {
      throw new Error("The authentication service returned an invalid code.");
    }
    return `P2,${studentNumber},${exerciseId},${authCode}`;
  }

  function downloadFilename(studentNumber, exerciseId) {
    if (!STUDENT_NUMBER_PATTERN.test(studentNumber)) {
      throw new Error("Student number must contain exactly seven digits.");
    }
    validateExerciseId(exerciseId);
    return `${studentNumber}_${exerciseId}.png`;
  }

  async function requestAuthCode(
    authUrl,
    studentNumber,
    exerciseUrl,
    timeoutMs = AUTH_TIMEOUT_MS,
  ) {
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), timeoutMs);
    try {
      const response = await fetch(authUrl, {
        method: "POST",
        headers: { "Content-Type": "text/plain" },
        body: `${studentNumber};${exerciseUrl}`,
        cache: "no-store",
        credentials: "omit",
        signal: controller.signal,
      });
      if (!response.ok) {
        throw new Error(`The authentication service returned HTTP ${response.status}.`);
      }

      const authCode = (await response.text()).trim();
      if (
        !authCode ||
        authCode.length > MAX_AUTH_CODE_LENGTH ||
        /[\r\n]/.test(authCode)
      ) {
        throw new Error("The authentication service returned an invalid code.");
      }
      return authCode;
    } catch (error) {
      if (controller.signal.aborted) {
        throw new Error(
          "The authentication service did not respond before the request timed out.",
        );
      }
      throw error;
    } finally {
      window.clearTimeout(timeout);
    }
  }

  async function resolveAuthCode(
    authUrl,
    studentNumber,
    exerciseUrl,
    timeoutMs = AUTH_TIMEOUT_MS,
  ) {
    try {
      return {
        authCode: await requestAuthCode(
          authUrl,
          studentNumber,
          exerciseUrl,
          timeoutMs,
        ),
        authError: null,
      };
    } catch (authError) {
      return {
        authCode: AUTH_SERVER_OFFLINE_ERROR,
        authError,
      };
    }
  }

  function canvasBlob(canvas) {
    return new Promise((resolve, reject) => {
      canvas.toBlob((blob) => {
        if (blob) {
          resolve(blob);
        } else {
          reject(new Error("The generated exercise could not be converted to PNG."));
        }
      }, "image/png");
    });
  }

  async function stampExercise(root, payload, studentNumber, preview, download) {
    const templateUrl = root.dataset.templateUrl;
    if (!templateUrl) {
      throw new Error("The page does not specify data-template-url.");
    }

    const template = await loadImage(templateUrl);
    const width = template.naturalWidth || template.width;
    const height = template.naturalHeight || template.height;
    if (!width || !height) {
      throw new Error("The exercise template has invalid dimensions.");
    }

    const configuredSize = positiveInteger(root.dataset.qrSize, "data-qr-size");
    const configuredX = positiveInteger(root.dataset.qrX, "data-qr-x");
    const configuredY = positiveInteger(root.dataset.qrY, "data-qr-y");
    const configuredValues = [configuredX, configuredY, configuredSize];
    const configuredCount = configuredValues.filter((value) => value !== null).length;
    if (configuredCount !== 0 && configuredCount !== 3) {
      throw new Error(
        "Set all three QR overrides: data-qr-x, data-qr-y, and data-qr-size.",
      );
    }

    let x;
    let y;
    let size;
    if (configuredCount === 3) {
      x = configuredX;
      y = configuredY;
      size = configuredSize;
    } else {
      const placeholder = findPlaceholderRect(template, width, height);
      const padding = Math.max(2, Math.round(Math.min(width, height) * 0.002));
      size = Math.max(placeholder.width, placeholder.height) + padding * 2;
      x = Math.round(
        placeholder.x + placeholder.width / 2 - size / 2,
      );
      y = Math.round(
        placeholder.y + placeholder.height / 2 - size / 2,
      );
    }

    if (size < 96 || x < 0 || y < 0 || x + size > width || y + size > height) {
      throw new Error("The configured QR placement is outside the template image.");
    }

    const qrCanvas = await renderQrCode(root, payload, size);
    preview.width = width;
    preview.height = height;
    const context = preview.getContext("2d");
    if (!context) {
      throw new Error("This browser does not support two-dimensional canvas.");
    }
    context.drawImage(template, 0, 0, width, height);
    context.imageSmoothingEnabled = false;
    context.drawImage(qrCanvas, x, y, size, size);

    const blob = await canvasBlob(preview);
    if (download.dataset.objectUrl) {
      URL.revokeObjectURL(download.dataset.objectUrl);
    }
    const objectUrl = URL.createObjectURL(blob);
    download.dataset.objectUrl = objectUrl;
    download.href = objectUrl;
    download.download = downloadFilename(
      studentNumber,
      root.dataset.exerciseId,
    );
    preview.hidden = false;
    download.hidden = false;
  }

  function initialize(root) {
    if (root.dataset.initialized === "true") {
      return;
    }
    root.dataset.initialized = "true";

    const form = requiredElement(root, "form");
    const studentNumberInput = requiredElement(root, "student-number");
    const generateButton = requiredElement(root, "generate");
    const status = requiredElement(root, "status");
    const preview = requiredElement(root, "preview");
    const download = requiredElement(root, "download");
    const exerciseId = root.dataset.exerciseId;
    const exerciseUrl = root.dataset.exerciseUrl;
    const authUrl = root.dataset.authUrl || DEFAULT_AUTH_URL;

    if (!exerciseId || !exerciseUrl) {
      setStatus(
        status,
        "This exercise page is missing its exercise ID or canonical URL.",
        "error",
      );
      generateButton.disabled = true;
      return;
    }

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const studentNumber = studentNumberInput.value.trim();
      if (!STUDENT_NUMBER_PATTERN.test(studentNumber)) {
        setStatus(status, "Enter exactly seven digits.", "error");
        studentNumberInput.focus();
        return;
      }

      generateButton.disabled = true;
      generateButton.setAttribute("aria-busy", "true");
      download.hidden = true;
      setStatus(status, "Generating your exercise…", "working");

      try {
        const { authCode, authError } = await resolveAuthCode(
          authUrl,
          studentNumber,
          exerciseUrl,
        );
        const payload = buildHybridPayload(studentNumber, exerciseId, authCode);
        await stampExercise(
          root,
          payload,
          studentNumber,
          preview,
          download,
        );
        if (authError) {
          console.warn(
            "Authentication was unavailable; generated an offline-marked exercise.",
            authError,
          );
          generateButton.textContent = "Generated with warning";
          setStatus(
            status,
            "The authentication service was unavailable. Your offline-marked " +
              "exercise is ready; " +
              "submit it for instructor review.",
            "warning",
          );
        } else {
          generateButton.textContent = "Generated";
          setStatus(
            status,
            "Your exercise is ready. Use the download button below.",
            "success",
          );
        }
      } catch (error) {
        console.error(error);
        generateButton.disabled = false;
        setStatus(
          status,
          error instanceof Error ? error.message : "Exercise generation failed.",
          "error",
        );
      } finally {
        generateButton.removeAttribute("aria-busy");
      }
    });

    window.addEventListener("pagehide", () => {
      if (download.dataset.objectUrl) {
        URL.revokeObjectURL(download.dataset.objectUrl);
      }
    });
  }

  function initializeAll() {
    document.querySelectorAll("[data-hybrid-exercise]").forEach(initialize);
  }

  window.CMPUT301HybridExercise = Object.freeze({
    GENERATION_ERROR_MARKER,
    buildHybridPayload,
    downloadFilename,
    initialize,
    initializeAll,
    resolveAuthCode,
  });
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeAll, { once: true });
  } else {
    initializeAll();
  }
})();
