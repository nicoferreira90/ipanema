/* In-browser exercise runner.
 *
 * Loads Pyodide lazily on the first Run (so the ~10 MB runtime isn't fetched
 * on page load), then runs the user's code followed by the exercise's hidden
 * check block. No exception ⇒ pass; AssertionError ⇒ "not yet"; anything else
 * ⇒ show the traceback. On a pass it fires a `passed` event on the completion
 * form, which HTMX turns into a POST that records the completion server-side.
 */
(function () {
  "use strict";

  var PYODIDE_URL = "https://cdn.jsdelivr.net/pyodide/v0.27.2/full/pyodide.js";
  var pyodideReady = null;

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = function () { reject(new Error("script load failed")); };
      document.head.appendChild(s);
    });
  }

  function getPyodide(onStatus) {
    if (!pyodideReady) {
      pyodideReady = (async function () {
        if (onStatus) onStatus("warming up Python…");
        await loadScript(PYODIDE_URL);
        return await window.loadPyodide();
      })();
    }
    return pyodideReady;
  }

  function lineEl(text, cls) {
    var div = document.createElement("div");
    div.className = "term-line" + (cls ? " " + cls : "");
    div.textContent = text;
    return div;
  }

  function initRunner(root) {
    var editor = root.querySelector("[data-editor]");
    var runBtn = root.querySelector("[data-run]");
    var status = root.querySelector("[data-status]");
    var output = root.querySelector("[data-output]");
    var stamp = root.querySelector("[data-stamp]");
    var form = root.querySelector("[data-complete-form]");
    var codeField = root.querySelector("[data-code-field]");
    var checkScript = root.querySelector('script[type="application/json"]');
    var check = checkScript ? JSON.parse(checkScript.textContent) : "";

    editor.addEventListener("keydown", function (e) {
      if (e.key === "Tab") {
        e.preventDefault();
        var a = editor.selectionStart, b = editor.selectionEnd;
        editor.value = editor.value.slice(0, a) + "    " + editor.value.slice(b);
        editor.selectionStart = editor.selectionEnd = a + 4;
      }
    });

    function setStatus(text, cls) {
      status.className = "runner-status" + (cls ? " " + cls : "");
      status.textContent = text;
    }
    function emit(text, cls) {
      output.appendChild(lineEl(text, cls));
      output.scrollTop = output.scrollHeight;
    }

    runBtn.addEventListener("click", async function () {
      runBtn.disabled = true;
      setStatus("loading…");
      output.innerHTML = "";

      var py;
      try {
        py = await getPyodide(setStatus);
      } catch (err) {
        emit("Couldn't load the Python runtime — check your connection.", "fail");
        setStatus("offline?", "no");
        runBtn.disabled = false;
        return;
      }
      setStatus("running…");

      var buffer = [];
      py.setStdout({ batched: function (s) { buffer.push(s); } });
      py.setStderr({ batched: function (s) { buffer.push(s); } });

      var userCode = editor.value;
      var script = userCode + "\n\n# --- checks ---\n" + check + "\n";

      var ns = py.runPython("dict()");
      try {
        await py.runPythonAsync(script, { globals: ns });
        buffer.forEach(function (b) { emit(b.replace(/\n$/, "")); });
        emit("✓ All checks passed.", "pass");
        setStatus("passed", "ok");
        stamp.classList.add("show");
        if (codeField) codeField.value = userCode;
        if (form) form.dispatchEvent(new CustomEvent("passed"));
      } catch (err) {
        buffer.forEach(function (b) { emit(b.replace(/\n$/, "")); });
        var msg = String((err && err.message) || err).trim();
        if (msg.indexOf("AssertionError") !== -1) {
          var parts = msg.split("\n");
          emit("✗ Not quite yet.", "fail");
          emit(parts[parts.length - 1], "hint");
          setStatus("not yet", "no");
        } else {
          emit(msg, "fail");
          setStatus("error", "no");
        }
      } finally {
        if (ns && ns.destroy) ns.destroy();
        runBtn.disabled = false;
      }
    });
  }

  function initAll(scope) {
    (scope || document).querySelectorAll("[data-runner]").forEach(function (el) {
      if (!el.dataset.bound) {
        el.dataset.bound = "1";
        initRunner(el);
      }
    });
  }

  if (document.readyState !== "loading") {
    initAll();
  } else {
    document.addEventListener("DOMContentLoaded", function () { initAll(); });
  }
})();
