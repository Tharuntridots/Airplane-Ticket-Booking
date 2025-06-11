// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        if(frm.doc.status !== "Accepted" && frm.doc.status !== "Rejected") {
            frm.add_custom_button("Accept", ()=>{
                frm.set_value("status", "Accepted");
                frm.save()
            }, "Actions")

            frm.add_custom_button("Reject", ()=>{
                frm.set_value("status", "Rejected")
                frm.save()
            }, "Actions")
        }

	},

    status(frm){
        console.log("status changed")
    }
});
