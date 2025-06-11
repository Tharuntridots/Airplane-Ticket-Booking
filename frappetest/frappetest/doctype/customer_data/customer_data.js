frappe.ui.form.on('Customer Data', {
    after_save: function(frm) {
        frappe.show_alert({
            message: __('Your data is received. Processing will complete in about 1 minute. Please wait...'),
            indicator: 'blue'
        });

        let interval = setInterval(() => {
            frappe.db.get_doc('Customer Data', frm.doc.name)
            .then(doc => {
                if (doc.processing_done) {
                    frappe.show_alert({
                        message: __('Processing completed successfully!'),
                        indicator: 'green'
                    });
                    clearInterval(interval);
                }
            })
            .catch(() => {
                clearInterval(interval);
            });
        }, 5000);  // every 5 seconds
    }
});
