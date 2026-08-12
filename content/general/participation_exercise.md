Title: Participation Exercises
date: 2026-08-11
tags: assignment, grading
authors: Raj Prasad, Michelle Deng, Hazel Victoria Campbell, Abram Hindle
status: published
summary: Individual Assignments, Participation

----

[TOC]

PUBLIC VERSION - WILL BE REMOVED

<div>
  <label for="student-id">Student ID:</label>
  <input
    type="text"
    id="student-id"
    placeholder="Enter your student ID"
  >

  <button onclick="authenticateStudent()">
    Authenticate
  </button>

  <p id="auth-result"></p>

  <div id="qrcode"></div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>

<script>
async function authenticateStudent() {
  const studentId =
    document.getElementById("student-id").value.trim();

  const result =
    document.getElementById("auth-result");

  const qrContainer =
    document.getElementById("qrcode");

  if (!studentId) {
    result.textContent = "Please enter your student ID.";
    return;
  }

  const exerciseUrl =
    "https://cmput301.github.io/exercises/1.png";

  try {
    // Step 1: Ask Pizza to generate a code
    const response = await fetch(
      "https://pizza.cs.ualberta.ca/auth/",
      {
        method: "POST",
        headers: {
          "Content-Type": "text/plain"
        },
        body: studentId + ";" + exerciseUrl
      }
    );

    const x = await response.text();

    console.log("Pizza generated:", x);

    // Step 2: Verify the code with Pizza
    const verifyResponse = await fetch(
      "https://pizza.cs.ualberta.ca/auth/?verify="
        + encodeURIComponent(x),
      {
        method: "POST",
        headers: {
          "Content-Type": "text/plain"
        },
        body: studentId + ";" + exerciseUrl
      }
    );

    const verification = await verifyResponse.text();

    console.log("Pizza verification:", verification);

    if (verification.trim() === "OK") {

      result.textContent =
        "Pizza authentication successful!";

      // Clear any previous QR
      qrContainer.innerHTML = "";

      // Data to put into the QR
      const qrData =
        studentId + "|" +
        exerciseUrl + "|" +
        x;

      console.log("QR data:", qrData);

      // Generate QR
      new QRCode(qrContainer, {
        text: qrData,
        width: 256,
        height: 256
      });

    } else {

      result.textContent =
        "Pizza authentication failed.";

    }

  } catch (error) {

    console.error(error);

    result.textContent =
      "Error communicating with Pizza.";
  }
}
</script>