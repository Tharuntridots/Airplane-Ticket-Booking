frappe.ui.form.on('Test ToDo', {
    before_save: function(frm) {
        console.log("Custom ToDo JS loaded");
        alert("Hello ToDo!");
    }
    
});
