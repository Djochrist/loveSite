/**
 * Floating hearts animation module.
 *
 * Dynamically generates heart elements with random properties
 * to create a romantic ambiance in the background.
 */
(function() {
  const overlay = document.getElementById('hearts-overlay');
  if (!overlay) return;

  // Optimized heart SVG template
  const heartSVG = `<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path fill="currentColor" d="M12 21s-8-6.6-8-11.4C4 6.5 6.5 4 9.4 4 11 4 12 5 12 5s1-1 2.6-1C17.5 4 20 6.5 20 9.6 20 14.4 12 21 12 21z"/>
  </svg>`;

  // Romantic color palette
  const colors = ['#ff6b81', '#ff8fa3', '#ffb3c1', '#ffcccc'];

  /**
   * Creates and animates a floating heart.
   */
  function createHeart() {
    const element = document.createElement('div');
    element.className = 'heart';

    // Random properties for visual variety
    const size = 20 + Math.random() * 25;
    element.style.width = size + 'px';
    element.style.height = size + 'px';
    element.style.left = (10 + Math.random() * 80) + '%';
    element.style.top = (70 + Math.random() * 30) + '%';
    element.style.color = colors[Math.floor(Math.random() * colors.length)];
    element.style.animationDuration = (4 + Math.random() * 4) + 's';

    element.innerHTML = heartSVG;
    overlay.appendChild(element);

    // Automatic cleanup after animation
    setTimeout(() => {
      element.remove();
    }, 8000);
  }

  // Periodic heart generation
  setInterval(createHeart, 800);

  // Staggered initial generation
  for (let i = 0; i < 8; i++) {
    setTimeout(createHeart, i * 200);
  }
})();
