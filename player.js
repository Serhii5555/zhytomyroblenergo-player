(() => {
  async function playVideo() {
    const response = await fetch("output.json");
    const data = await response.json();
    const frames = data.frames;
    const fps = data.fps || 10;

    const audio = new Audio("audio.mp3");
    audio.volume = 1.0;

    const rows = Array.from(document.querySelectorAll("tr")).slice(6);

    const cells = rows.slice(0, 12).map((row, i) => {
      const tds = Array.from(row.querySelectorAll("td"));
      const skip = i % 2 === 0 ? 3 : 2;
      return tds.slice(skip, skip + 48);
    });

    await audio.play();
    const startTime = performance.now();

    function drawFrame() {
      const elapsed = (performance.now() - startTime) / 1000;
      const frameIndex = Math.floor(elapsed * fps);

      if (frameIndex >= frames.length) return; 

      const frame = frames[frameIndex];

      for (let y = 0; y < 12; y++) {
        for (let x = 0; x < 48; x++) {
          const cell = cells[y][x];
          if (!cell) continue;
          const val = frame[y][x];
          cell.style.background = val === 1 ? "#ff3333" : "#ffffff";
        }
      }

      requestAnimationFrame(drawFrame);
    }

    drawFrame();
  }

  // Ctrl + Alt + M почати відтворення
  window.addEventListener("keydown", (e) => {
    if (e.ctrlKey && e.altKey && e.key.toLowerCase() === "m") {
      console.log("Video playback started");
      playVideo();
    }
  });
})();
