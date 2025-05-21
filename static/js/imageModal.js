document.getElementById('imageModal').addEventListener('show.bs.modal', function (event) {
    const triggerImg = event.relatedTarget;
    const imageUrl = triggerImg.getAttribute('data-img');
    document.getElementById('modalImage').src = imageUrl;
  });