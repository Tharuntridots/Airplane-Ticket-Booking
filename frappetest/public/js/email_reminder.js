frappe.realtime.on("email_reminder_event", function(data) {
    frappe.show_alert({
        message: `${data.title}: ${data.message}`,
        indicator: 'blue'
    });
});
