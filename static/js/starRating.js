document.querySelectorAll('#starContainer .star-label').forEach(label =>
    label.addEventListener('click', () => {
      const val = +label.dataset.value;
      document.querySelectorAll('#starContainer .star-label i').forEach((icon, i) => {
        icon.className = (i < val) ? 'fa-solid fa-star' : 'fa-regular fa-star';
      });
    })
  );