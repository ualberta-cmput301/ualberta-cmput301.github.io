Title: Mock Testing Participation Exercise
date: 2026-09-21
tags: participation, exercise
authors: Abram Hindle
status: hidden
summary: Mock Testing Participation Exercise
robots: noindex, nofollow
----

# Mock Testing Participation Exercise

Enter your seven-digit student number to generate your participation exercise.

<div
  class="hybrid-exercise"
  data-hybrid-exercise
  data-exercise-url="https://ualberta-cmput301.github.io/individual/mock-testing-01.html"
  data-template-url="/theme/exercises/2026-fall/mock-testing-01.png"
  data-download-name="mock-testing-01.png">

  <form data-role="form">
    <label>
      Student number
      <input
        data-role="student-number"
        name="student-number"
        type="text"
        inputmode="numeric"
        autocomplete="off"
        maxlength="7"
        pattern="[0-9]{7}"
        required>
    </label>
    <button data-role="generate" type="submit">Go</button>
  </form>

  <p data-role="status" role="status" aria-live="polite"></p>

  <canvas
    data-role="preview"
    aria-label="Generated participation exercise preview"
    style="display:block; max-width:100%; height:auto"
    hidden></canvas>

  <p>
    <a data-role="download" role="button" hidden>Download exercise</a>
  </p>
</div>

<script src="/theme/js/hybrid-exercise.js" defer></script>