frappe.ui.form.on('Samosa Shop', {
    refresh: function (frm) {
        frm.add_custom_button('Accept' , ()=>{
            frm.doc.order = "selected"
        })
    }
});

