function showAlert(message) {
  const alert = document.createElement("div");
  alert.className = "alert alert-info alert-dismissible";
  alert.innerHTML = `
    <div>${message}</div>
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
  `;
  const container = document.getElementById("Alert");
  if (container) container.appendChild(alert);
  setTimeout(() => alert.remove(), 3000);
}