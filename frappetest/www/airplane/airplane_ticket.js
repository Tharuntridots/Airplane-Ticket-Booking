window.onload = function () {
    frappe.call({
        method: "frappetest.frappetest.www.airplane.airplane_ticket.passenger_details",
        callback: function (r) {
            const passengerSelect = document.getElementById("passenger");
            if (r.message && r.message.length > 0) {
                r.message.forEach(passenger => {
                    const option = document.createElement("option");
                    option.value = passenger.name;
                    option.textContent = passenger.full_name;
                    passengerSelect.appendChild(option);
                });
            } else {
                const option = document.createElement("option");
                option.textContent = "No Passengers Found";
                option.disabled = true;
                passengerSelect.appendChild(option);
            }
        }
    });
};

document.getElementById("ticketForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => data[key] = value);
    alert("Form Submitted Successfully!\n" + JSON.stringify(data, null, 2));
});
