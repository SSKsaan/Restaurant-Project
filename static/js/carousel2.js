document.addEventListener('DOMContentLoaded', () => {
  const cards = [...document.querySelectorAll('.carousel-card')];
  let current = 1;

  function update() {
    const total = cards.length;
    cards.forEach((card, idx) => {
      card.classList.remove('active', 'show-left', 'show-center', 'show-right');
      if (idx === (current - 1 + total) % total) card.classList.add('show-left');
      else if (idx === current) card.classList.add('show-center', 'active');
      else if (idx === (current + 1) % total) card.classList.add('show-right');
    });
  }

  cards.forEach((card, idx) => {
    card.addEventListener('click', () => {
      const total = cards.length;
      const left = (current - 1 + total) % total;
      const right = (current + 1) % total;
      if (idx === left) current = left;
      else if (idx === right) current = right;
      update();
    });
  });

  update();
});