document.addEventListener("DOMContentLoaded", function () {
  // Fetch and display existing Ride Orders (watch list)
  fetch("/api/resource/Ride Order?limit_page_length=5")
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("watch-list");
      data.data.forEach(item => {
        const li = document.createElement("li");
        li.innerText = `${item.customer_name} (${item.status})`;
        list.appendChild(li);
      });
    });

  // Handle form submission
  document.getElementById("cab-booking-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = {};
    formData.forEach((val, key) => (data[key] = val));

    fetch("/api/resource/Ride Order", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
        // Add Authorization header if login is not required
      },
      body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
      document.getElementById("success-msg").innerText = "Booking successful!";
      this.reset();
    });
  });
});
