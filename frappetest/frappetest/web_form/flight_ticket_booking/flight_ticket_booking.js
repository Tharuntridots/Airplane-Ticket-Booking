frappe.ready(function () {
    // Pre-fill flight from URL param
    frappe.web_form.after_load = () => {
        const params = new URLSearchParams(window.location.search);
        const flight = params.get("flight");
        if (flight) {
            frappe.web_form.set_value("flight", flight);
        }

        // Add Seat Selection button
        frappe.web_form.add_button('Seat Selection', () => {
            frappe.prompt(
                {
                    label: 'Enter Seat Number',
                    fieldname: 'seat_number',
                    fieldtype: 'Data',
                    reqd: 1
                },
                (values) => {
                    frappe.web_form.set_value("seat", values.seat_number);
                    frappe.msgprint(`Seat number set to ${values.seat_number}`);
                },
                'Select Your Seat',
                'Confirm'
            );
        });

        // Add Make Payment button
        frappe.web_form.add_button('Make Payment', () => {
            let doc = frappe.web_form.get_values();
            let amount_in_paise = (doc.total_amount || 100) * 100;

            let options = {
                key: "rzp_test_1DP5mmOlF5G5ag",
                amount: amount_in_paise,
                currency: "INR",
                name: doc.passenger || "Demo User",
                description: "Airplane Ticket Payment",
                handler: function (response) {
                    frappe.web_form.set_value("payment_id", response.razorpay_payment_id);
                    frappe.web_form.set_value("status", "Booked");

                    frappe.web_form.save().then(() => {
                        frappe.msgprint("Payment Successful. Ticket Booked!");
                        window.location.reload();
                    });
                },
                prefill: {
                    name: doc.passenger || "Test User",
                    email: doc.email || "test@example.com",
                    contact: doc.mobile || "9999999999"
                },
                theme: {
                    color: "#3399cc"
                },
                modal: {
                    ondismiss: function () {
                        frappe.msgprint("You closed the Razorpay popup.");
                    }
                }
            };

            let rzp = new Razorpay(options);
            rzp.open();
        });
    };
});
