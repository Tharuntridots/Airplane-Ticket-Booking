import frappe

@frappe.whitelist(allow_guest=True) 

def get_doctype_records(doctype):
    return frappe.get_all(doctype, fields=["name1", "bar", "number"])
