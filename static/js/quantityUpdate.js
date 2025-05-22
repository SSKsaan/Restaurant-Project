document.querySelectorAll('.update-qty').forEach(btn => {
  btn.onclick = () => {
    const input = btn.closest('.quantity-wrapper').querySelector('.qty-input'),
          quantity = Math.max(1, parseInt(input.value) + (btn.dataset.action === 'increase' ? 1 : -1)),
          id = btn.dataset.id;

    fetch(`/orders/update/`, {
      method: 'POST',
      headers: { 'X-CSRFToken': document.cookie.split('; ').find(row => row.startsWith('csrftoken='))?.split('=')[1] },
      body: new URLSearchParams({ item_id: id, quantity: quantity })
    })
    .then(res => res.json())
    .then(data => data.success ? input.value = quantity : showAlert(data.error || 'Failed to update.'));
  };
});