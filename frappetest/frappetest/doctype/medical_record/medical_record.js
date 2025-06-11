frappe.ui.form.on('Medical Record', {
    onload: function(frm) {
        frappe.msgprint(__('Welcome! Please fill out the Medical Record.'));
    },

    // refresh: function(frm) {
    //     frm.set_df_property('doctor', 'read_only', 1);  // Make doctor field read-only
    // },

    patient_name: function(frm) {
        if (frm.doc.patient_name.length < 3) {
            frappe.msgprint(__('Patient Name must be at least 3 characters'));
        }
    }
});
