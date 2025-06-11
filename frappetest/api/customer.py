# frappetest/frappetest/api/customer.py

import frappe

@frappe.whitelist()
def get_customer_data():
    return frappe.get_all('Customer Data', fields=["emp_name", "emp_role", "emp_salrary"])
