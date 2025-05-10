function showAlert(message) {
  const alert = document.createElement("div");
  alert.className = "alert alert-success alert-dismissible m-3";
  alert.style = "position: fixed; bottom: 10px; right: 10px; z-index: 1000;";
  alert.innerHTML = `
    <div>${message}</div>
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
  `;
  document.body.appendChild(alert);
  setTimeout(() => alert.remove(), 3000);
}