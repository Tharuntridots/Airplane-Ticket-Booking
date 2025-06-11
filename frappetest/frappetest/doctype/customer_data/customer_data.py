import frappe
from frappe.model.document import Document
import time

class CustomerData(Document):
    pass
    # def after_insert(self):
    #     # enqueue background job in 'short' queue
    #     frappe.enqueue(
    #         method='frappetest.frappetest.doctype.customer_data.customer_data.process_customer_data',
    #         queue='short',
    #         customer_name=self.name
    #     )

def process_customer_data(customer_name):
    customer = frappe.get_doc("Customer Data", customer_name)
    frappe.logger().info(f"Started processing {customer_name}")

    import time
    time.sleep(60)  # simulate long task

    # set flag and save
    customer.processing_done = 1
    customer.save()
    frappe.db.commit()  # commit to persist changes

    frappe.logger().info(f"Finished processing {customer_name}")


@frappe.whitelist(allow_guest = True)
def get_customer_data():
    data = frappe.get_all('Customer Data', fields=["emp_name", "emp_role", "emp_salrary"])
    return data

# Add a new customer record
@frappe.whitelist(allow_guest = True)
def add_customer(emp_name, emp_role, emp_salrary):
    doc = frappe.get_doc({
        "doctype": "Customer Data",
        "emp_name": emp_name,
        "emp_role": emp_role,
        "emp_salrary": emp_salrary
    })
    doc.insert()
    return doc.name

# Update an existing customer record
@frappe.whitelist(allow_guest = True)
def update_customer(name, emp_name, emp_role, emp_salrary):
    doc = frappe.get_doc("Customer Data", name)
    doc.emp_name = emp_name
    doc.emp_role = emp_role
    doc.emp_salrary = emp_salrary
    doc.save()
    return "Updated"

# Delete a customer record
@frappe.whitelist(allow_guest = True)
def delete_customer(name):
    frappe.delete_doc("Customer Data", name)
    return "Deleted"
