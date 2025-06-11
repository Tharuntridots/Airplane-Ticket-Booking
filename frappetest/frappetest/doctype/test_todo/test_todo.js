// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Test ToDo", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on('Test ToDo', {
    onload: function(frm) {
        if (!frm.doc.phone_number) {
            frm.set_value('phone_number', '+91');
        }
    }
});
