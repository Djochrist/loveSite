/**
 * Message animation module with interactive carousel.
 *
 * Implements a carousel where each message appears with a typing effect,
 * with navigation via buttons and keyboard for a controlled experience.
 */
(function() {
  const messageElements = document.querySelectorAll('.message');
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');

  // Retrieve message data
  // messagesData is defined in base.html

  // Check prerequisites
  if (!messageElements.length || !messagesData.length || !prevBtn || !nextBtn) return;

  let currentMessageIndex = 0;
  let isAnimating = false;

  /**
   * Animates the progressive appearance of text character by character.
   *
   * @param {HTMLElement} element - Target DOM element
   * @param {string} text - Text to display
   * @param {Function} callback - Function called after animation
   * @param {number} speed - Delay between each character (ms)
   */
  function typeWriter(element, text, callback, speed = 30) {
    element.textContent = '';
    element.style.display = 'block';

    let charIndex = 0;

    function type() {
      if (charIndex < text.length) {
        element.textContent += text.charAt(charIndex);
        charIndex++;
        setTimeout(type, speed);
      } else {
        if (callback) callback();
      }
    }

    type();
  }

  /**
   * Hides all messages.
   */
  function hideAllMessages() {
    messageElements.forEach(el => {
      el.style.display = 'none';
      el.textContent = '';
    });
  }

  /**
   * Updates the state of navigation buttons.
   */
  function updateNavigationButtons() {
    prevBtn.disabled = currentMessageIndex === 0;
    nextBtn.disabled = currentMessageIndex === messagesData.length - 1;
  }

  /**
   * Displays the current message with animation.
   */
  function showCurrentMessage() {
    if (isAnimating) return;

    isAnimating = true;
    hideAllMessages();

    const element = messageElements[currentMessageIndex];
    const text = messagesData[currentMessageIndex].text;

    typeWriter(element, text, () => {
      isAnimating = false;
      updateNavigationButtons();
    });
  }

  /**
   * Navigate to the next message.
   */
  function nextMessage() {
    if (currentMessageIndex < messagesData.length - 1 && !isAnimating) {
      currentMessageIndex++;
      showCurrentMessage();
    }
  }

  /**
   * Navigate to the previous message.
   */
  function prevMessage() {
    if (currentMessageIndex > 0 && !isAnimating) {
      currentMessageIndex--;
      showCurrentMessage();
    }
  }

  /**
   * Keyboard event handler.
   */
  function handleKeyPress(event) {
    if (event.key === 'ArrowRight' || event.key === ' ') {
      event.preventDefault();
      nextMessage();
    } else if (event.key === 'ArrowLeft') {
      event.preventDefault();
      prevMessage();
    }
  }

  // Event listeners
  prevBtn.addEventListener('click', prevMessage);
  nextBtn.addEventListener('click', nextMessage);
  document.addEventListener('keydown', handleKeyPress);

  // Start the carousel
  updateNavigationButtons();
  showCurrentMessage();

  // Display the messages section
  const messagesSection = document.getElementById('messages-section');
  if (messagesSection && messagesData.length > 0) {
    messagesSection.style.display = 'block';
  }
})();
