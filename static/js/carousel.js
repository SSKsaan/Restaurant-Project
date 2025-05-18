// For Featured Items:

let scrollIndex = 0;

function scrollItems(direction) {
  const track = document.getElementById("featuredTrack");
  const item = track.querySelector(".item-card, .menu-link-card");
  const gap = parseFloat(getComputedStyle(track).gap) || 0;
  const itemWidth = item.offsetWidth + gap;
  const maxIndex = track.children.length - 3;

  scrollIndex += direction;
  if (scrollIndex < 0) scrollIndex = 0;
  if (scrollIndex > maxIndex) scrollIndex = maxIndex;

  const scrollX = scrollIndex * itemWidth;
  track.style.transform = `translateX(-${scrollX}px)`;
}

// For Featured Reviews:

document.addEventListener('DOMContentLoaded', () => {
  const cards = [...document.querySelectorAll('.review-card')];
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
