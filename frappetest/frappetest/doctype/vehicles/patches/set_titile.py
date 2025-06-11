import frappe

def execute():
    vehicles = frappe.get_all("Vehicles", pluck="name")
    for name in vehicles:
        doc = frappe.get_doc("Vehicles", name)
        doc.set_title()
        doc.save()

    frappe.db.commit()

