(function() {
  const fileInput = document.getElementById('song_file');
  const fileLabel = document.getElementById('song_file_label');
  const fileNameSpan = document.getElementById('song_file_name');

  if (!fileInput || !fileLabel || !fileNameSpan) return;

  fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    if (file) {
      fileNameSpan.textContent = file.name;
      fileLabel.textContent = 'Changer...';
    } else {
      fileNameSpan.textContent = '';
      fileLabel.textContent = 'Choisir un fichier...';
    }
  });
})();