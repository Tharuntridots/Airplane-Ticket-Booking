// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {

	},

    rate(frm){
        frm.trigger("update_total_amount")
    },
    update_total_amount(frm){
        let total_d = 0;
        for (let item of frm.doc.items){
            total_d += item.distance
        }

        const a = frm.doc.rate * total_d;
        frm.set_value("amount", a)

    }
});


frappe.ui.form.on("Ride Booking Item", {
    reffresh(frm){

    }, 
    distance(frm, cdt, cdn){
        frm.trigger("update_total_amount")

    },
    items_remove(frm){
        frm.trigger("update_total_amount")
    }
})