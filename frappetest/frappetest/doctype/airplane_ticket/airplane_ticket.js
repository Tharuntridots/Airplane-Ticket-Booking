// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt



frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
		frm.add_custom_button("Seat Selection", () => {
			frappe.prompt(
				{
					label: 'Enter Seat Number',
					fieldname: 'seat_number',
					fieldtype: 'Data',
					reqd: 1
				},
				(values) => {
					frm.set_value("seat", values.seat_number);
                    frm.toggle_display("seat", 'read_only', 1);
					frappe.msgprint(`Seat number set to ${values.seat_number}`);
				},
				"Select Your Seat",
				"Confirm"
			);
		});
	},
});

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        if (frappe.session.user === 'imran@example.com') {
            frm.set_df_property('status', 'read_only', 1);
        } else {
            frm.set_df_property('status', 'read_only', 0);
        }
    }
});


