/**
 * Enhanced hearts animation module with emotional choreography.
 *
 * Creates spectacular heart bursts with sparkles and stars when messages appear,
 * along with ambient floating hearts for romantic ambiance.
 */
(function() {
  const overlay = document.getElementById('hearts-overlay');
  if (!overlay) return;

  // Optimized heart SVG template
  const heartSVG = `<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path fill="currentColor" d="M12 21s-8-6.6-8-11.4C4 6.5 6.5 4 9.4 4 11 4 12 5 12 5s1-1 2.6-1C17.5 4 20 6.5 20 9.6 20 14.4 12 21 12 21z"/>
  </svg>`;

  // Star SVG template
  const starSVG = `<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path fill="currentColor" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
  </svg>`;

  // Vibrant romantic color palette
  const heartColors = ['#ff0080', '#ff1493', '#dc143c', '#ff4500', '#ff6347', '#ffd700', '#ff69b4', '#da70d6'];
  const starColors = ['#ffd700', '#ffff00', '#ffeb3b', '#ffa500', '#ff1493'];

  /**
   * Creates and animates a floating heart for ambient background.
   */
  function createAmbientHeart() {
    const element = document.createElement('div');
    element.className = 'heart ambient';

    // Random properties for visual variety
    const size = 15 + Math.random() * 20;
    element.style.width = size + 'px';
    element.style.height = size + 'px';
    element.style.left = (5 + Math.random() * 90) + '%';
    element.style.top = (75 + Math.random() * 25) + '%';
    element.style.color = heartColors[Math.floor(Math.random() * heartColors.length)];
    element.style.animationDuration = (6 + Math.random() * 6) + 's';
    element.style.animationDelay = Math.random() * 3 + 's';

    element.innerHTML = heartSVG;
    overlay.appendChild(element);

    // Automatic cleanup after animation
    setTimeout(() => {
      element.remove();
    }, 15000);
  }

  /**
   * Creates a spectacular heart burst with sparkles and stars.
   * Hearts appear from center, sparkle, explode outward, and fly away with stars.
   */
  function createHeartBurst(centerX, centerY) {
    const burstCount = 8 + Math.floor(Math.random() * 12); // 8-20 hearts per burst

    for (let i = 0; i < burstCount; i++) {
      setTimeout(() => {
        // Create heart
        const heartElement = document.createElement('div');
        heartElement.className = 'heart burst';

        const size = 25 + Math.random() * 35;
        heartElement.style.width = size + 'px';
        heartElement.style.height = size + 'px';
        heartElement.style.left = centerX + 'px';
        heartElement.style.top = centerY + 'px';
        heartElement.style.color = heartColors[Math.floor(Math.random() * heartColors.length)];
        heartElement.style.setProperty('--angle', (360 / burstCount * i) + 'deg');
        heartElement.style.setProperty('--distance', (200 + Math.random() * 300) + 'px');

        heartElement.innerHTML = heartSVG;
        overlay.appendChild(heartElement);

        // Add sparkles to the heart
        addSparkles(heartElement, size);

        // Create accompanying star
        if (Math.random() > 0.3) { // 70% chance for star
          const starElement = document.createElement('div');
          starElement.className = 'star burst';

          const starSize = 15 + Math.random() * 20;
          starElement.style.width = starSize + 'px';
          starElement.style.height = starSize + 'px';
          starElement.style.left = centerX + 'px';
          starElement.style.top = centerY + 'px';
          starElement.style.color = starColors[Math.floor(Math.random() * starColors.length)];
          starElement.style.setProperty('--angle', (360 / burstCount * i + 45) + 'deg');
          starElement.style.setProperty('--distance', (150 + Math.random() * 250) + 'px');

          starElement.innerHTML = starSVG;
          overlay.appendChild(starElement);

          // Cleanup star
          setTimeout(() => {
            starElement.remove();
          }, 4000);
        }

        // Cleanup heart
        setTimeout(() => {
          heartElement.remove();
        }, 4000);
      }, i * 50); // Stagger creation
    }
  }

  /**
   * Adds sparkle effects to a heart element.
   */
  function addSparkles(heartElement, heartSize) {
    const sparkleCount = 3 + Math.floor(Math.random() * 5);

    for (let i = 0; i < sparkleCount; i++) {
      const sparkle = document.createElement('div');
      sparkle.className = 'sparkle';

      const sparkleSize = 3 + Math.random() * 4;
      sparkle.style.width = sparkleSize + 'px';
      sparkle.style.height = sparkleSize + 'px';
      sparkle.style.left = (Math.random() * heartSize) + 'px';
      sparkle.style.top = (Math.random() * heartSize) + 'px';
      sparkle.style.animationDelay = (Math.random() * 0.5) + 's';

      heartElement.appendChild(sparkle);

      // Remove sparkle after animation
      setTimeout(() => {
        sparkle.remove();
      }, 1500);
    }
  }

  /**
   * Triggers a heart burst at the center of the messages section.
   * Called when a new message is displayed.
   */
  function triggerHeartBurst() {
    const messagesSection = document.getElementById('messages-section');
    if (!messagesSection) return;

    const rect = messagesSection.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    createHeartBurst(centerX, centerY);
  }

  // Expose to global scope for animation.js
  window.triggerHeartBurst = triggerHeartBurst;

  // Periodic ambient heart generation (reduced frequency)
  setInterval(createAmbientHeart, 2000);

  // Staggered initial ambient hearts
  for (let i = 0; i < 5; i++) {
    setTimeout(createAmbientHeart, i * 500);
  }
})();
