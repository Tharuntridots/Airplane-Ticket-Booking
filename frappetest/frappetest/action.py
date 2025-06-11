import frappe

@frappe.whitelist()
def execute_function(*args,**kwargs):
    frappe.msgprint("this is for test purpose")


