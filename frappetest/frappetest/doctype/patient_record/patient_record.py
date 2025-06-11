import frappe
import time
from frappe.model.document import Document

class PatientRecord(Document):
    pass

# # @frappe.whitelist()
# # def get_patient_details(patient_name):
# #     patient = frappe.get_all("Patient Record", 
# #         filters={"patient_name": patient_name},
# #         fields=["name", "age", "gender"])
# #     return patient


# # def send_age_data():
# #     for age in range(1, 101):
# #         frappe.publish_realtime('test_event', {
# #             'label': str(age),     # x-axis label (must be string)
# #             'points': [age]        # y-axis value(s) — here: age
# #         })
# #         time.sleep(1)  

# @frappe.whitelist()
# def get_patient_record(docname):
#     doc = frappe.get_doc('Patient Record', docname)
#     return doc


# # @frappe.whitelist()
# # def get_chat_by_phone(phone_number):
# #     chat_doc = frappe.get_all("Chat Message", filters={"phone_number": phone_number}, fields=["name", "name1", "address", "phone_number"], limit=1)
    
# #     if chat_doc:
# #         return chat_doc[0]
# #     else:
# #         return {"error": "No chat found for this phone number."}

# @frappe.whitelist()
# def get_chat_by_name(chat_name):
#     try:
#         chat_doc = frappe.get_doc('Chat Message', chat_name)
#         return {
#             "name" : chat_doc.name,
#             "phone": chat_doc.phone_number
#         }
#     except frappe.DoesNotExistError:
#         return {"error": "Chat messahe not found"}

# @frappe.whitelist()
# def get_last_patient_record():
#     doc = frappe.get_last_doc("Patient Record")
#     return doc

# @frappe.whitelist()
# def create_chat_message():
#     doc = frappe.get_doc({
#         "doctype": "Chat Message",
#         "name1": "John Doe",
#         "phone_number": "9876543210",
#         "address": "Chennai"
#     })
#     doc.insert(ignore_permissions=True)
#     return doc.name

# @frappe.whitelist()
# def update_chat_address(docname, new_address):
#     doc = frappe.get_doc("Chat Message", docname)
#     doc.address = new_address
#     doc.save(ignore_permissions=True)
#     return "Updated successfully"


# @frappe.whitelist()
# def chat_phone_change(docname, new_phone):
#     doc = frappe.get_doc("Chat Message", docname)
#     doc.phone_number = new_phone

#     changed = doc.has_value_changed("phone_number")
#     if changed:
#         doc.save(ignore_permissions=True)
#         return "phone number changed"
#     return "no change"

# @frappe.whitelist()
# def notify_chat_update(docname):
#     doc = frappe.get_doc("Chat Message", docname)
#     doc.notify_update()
#     return "Notify sent"


# @frappe.whitelist()
# def age_update(docname):
#     doc = frappe.get_doc("Patient Record", docname)
#     doc.db_set('age', 23)
#     return doc.age

# @frappe.whitelist()
# def get_url(docname):
#     doc = frappe.get_doc("Patient Record", docname)
#     url = doc.get_url()
#     return url

# @frappe.whitelist()
# def get_app_patients():
#     doc = frappe.db.get_list("Patient Record",
#     filters= {
#         'docstatus': 1
#     },
#     fields = ['patient_name', 'age'])
#     return doc

# @frappe.whitelist()
# def get_db_value():
#     doc= frappe.db.get_value("Patient Record", "PAT-0030", ["patient_name", "age"])
#     return doc

# @frappe.whitelist()
# def set_db_value(docname, fieldname, value):
#     ## Check if a Patient Record exists
#     if frappe.db.exists("Patient Record", "PAT-0028"):
#         frappe.msgprint("Record exists!")


# @frappe.whitelist()
# def get_count():
#     doc = frappe.db.count('Patient Record', {
#         "docstatus": 1
#     })
#     return doc

# @frappe.whitelist()
# def db_delete():
#     doc = frappe.db.truncate("Patient Record", 'PAT-0035' )
#     return "Deleted"


# @frappe.whitelist()
# def db_delete(docname):
#     doc = frappe.get_doc("Patient Record", docname)
#     doc.truncate()
#     frappe.db.commit()
#     return f"Deleted record {docname}"


@frappe.whitelist()
def sql_query():
    age_limit = 60
    data = frappe.db.sql("""
        SELECT name, patient_name, age
        FROM `tabPatient Record`
        WHERE age > %s
    """, (age_limit,), as_dict = 1)


    for patient in data:
        frappe.msgprint(f"{patient['patient_name']} isd {patient['age']} years old")

    return data

# @frappe.whitelist()
# def rename_patient_table():
#     # This renames an internal custom table (NOT recommended for Doctypes)
#     try:
#         frappe.db.rename_table("Patient Record Archive", "Patient Record")
#         return "Table renamed successfully"
#     except Exception as e:
#         frappe.db.rollback()
#         frappe.log_error(title="Rename Table Failed", message=str(e))
#         return f"Error: {e}"


@frappe.whitelist()
def describe_patient_table():
    description = frappe.db.describe("Patient Record")
    frappe.msgprint(str(description))

@frappe.whitelist()
def change_age():
    doc = frappe.get_doc("Patient Record", "PAT-0035")
    doc.age = 156
    return doc