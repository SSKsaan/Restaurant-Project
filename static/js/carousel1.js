let scrollIndex = 0;

function scrollItems(direction) {
  const track = document.getElementById("carousel-track");
  const item = track.querySelector(".item-card, .redirect-card");
  const gap = parseFloat(getComputedStyle(track).gap) || 0;
  const itemWidth = item.offsetWidth + gap;
  const maxIndex = track.children.length - 3;

  scrollIndex += direction;
  if (scrollIndex < 0) scrollIndex = 0;
  if (scrollIndex > maxIndex) scrollIndex = maxIndex;

  const scrollX = scrollIndex * itemWidth;
  track.style.transform = `translateX(-${scrollX}px)`;
}