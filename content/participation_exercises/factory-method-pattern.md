Title: Factory Method Pattern Exercise
date: 2026-08-15
tags: participation, exercise
authors: Michelle Deng, Raj Prasad, Abram Hindle
status: hidden
summary: Factory Method Pattern Participation Exercise
robots: noindex, nofollow
----

# Factory Method Pattern Participation Exercise

Enter your seven-digit student number to generate your participation exercise.

<div
  class="hybrid-exercise"
  data-hybrid-exercise
  data-exercise-id="factory-method-pattern"
  data-exercise-url="https://ualberta-cmput301.github.io/participation_exercises/factory-method-pattern.html"
  data-template-url="/theme/exercises/2026-fall/factory-method-pattern.png">

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