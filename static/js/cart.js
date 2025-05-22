function addToCart(itemSlug) {
  fetch(`/menu/add_to_cart/${itemSlug}`, {
    method: "POST",
    headers: {
      "X-CSRFToken": document.cookie.split('; ').find(row => row.startsWith('csrftoken='))?.split('=')[1]
    }
  })
  .then(res => res.json())
  .then(data => { if(data.message) {showAlert(data.message);} });
}