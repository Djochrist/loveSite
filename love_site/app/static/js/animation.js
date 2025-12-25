/**
 * Module d'animation des messages avec carousel interactif.
 *
 * Implémente un carousel où chaque message apparaît avec effet de frappe,
 * avec navigation via boutons et clavier pour une expérience contrôlée.
 */
(function() {
  const messageElements = document.querySelectorAll('.message');
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');

  // Récupération des données des messages
  // messagesData est défini dans base.html

  // Vérification des prérequis
  if (!messageElements.length || !messagesData.length || !prevBtn || !nextBtn) return;

  let currentMessageIndex = 0;
  let isAnimating = false;

  /**
   * Anime l'apparition progressive du texte caractère par caractère.
   *
   * @param {HTMLElement} element - Élément DOM cible
   * @param {string} text - Texte à afficher
   * @param {Function} callback - Fonction appelée après l'animation
   * @param {number} speed - Délai entre chaque caractère (ms)
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
   * Masque tous les messages.
   */
  function hideAllMessages() {
    messageElements.forEach(el => {
      el.style.display = 'none';
      el.textContent = '';
    });
  }

  /**
   * Met à jour l'état des boutons de navigation.
   */
  function updateNavigationButtons() {
    prevBtn.disabled = currentMessageIndex === 0;
    nextBtn.disabled = currentMessageIndex === messagesData.length - 1;
  }

  /**
   * Affiche le message actuel avec animation.
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
   * Navigue vers le message suivant.
   */
  function nextMessage() {
    if (currentMessageIndex < messagesData.length - 1 && !isAnimating) {
      currentMessageIndex++;
      showCurrentMessage();
    }
  }

  /**
   * Navigue vers le message précédent.
   */
  function prevMessage() {
    if (currentMessageIndex > 0 && !isAnimating) {
      currentMessageIndex--;
      showCurrentMessage();
    }
  }

  /**
   * Gestionnaire d'événements clavier.
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

  // Écouteurs d'événements
  prevBtn.addEventListener('click', prevMessage);
  nextBtn.addEventListener('click', nextMessage);
  document.addEventListener('keydown', handleKeyPress);

  // Démarrage du carousel
  updateNavigationButtons();
  showCurrentMessage();

  // Afficher la section messages si des messages sont présents
  const formSection = document.getElementById('form-section');
  const messagesSection = document.getElementById('messages-section');
  if (formSection && messagesSection && messagesData.length > 0) {
    formSection.style.display = 'none';
    messagesSection.style.display = 'block';
  }
})();
