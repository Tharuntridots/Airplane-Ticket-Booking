frappe.ready(function () {
    frappe.web_form.after_load = () => {
        const params = new URLSearchParams(window.location.search);
        const flight = params.get("flight");
        if (flight) {
            frappe.web_form.set_value("flight", flight);
        }
    };
});
