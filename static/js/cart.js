function addToCart(itemSlug) {
  fetch(`/add_to_cart/${itemSlug}/`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCSRF(),
      "Content-Type": "application/x-www-form-urlencoded"
    }
  })
  .then(res => res.json())
  .then(data => { if(data.message) {showAlert(data.message);} });
}

function getCSRF() {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}