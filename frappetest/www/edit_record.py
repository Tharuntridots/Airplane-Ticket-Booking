import frappe

# def get_context(context):
#     record_name = frappe.form_dict.get("name") or "MED-0001"
#     doc = frappe.get_doc("Medical Record", record_name)

#     if frappe.request.method == "POST":
#         # Form la irundhu data eduthutu
#         doc.patient_name = frappe.form_dict.patient_name
#         doc.diseases = frappe.form_dict.diseases
#         doc.date = frappe.form_dict.date
#         doc.doctor = frappe.form_dict.doctor

#         doc.save()  # DB ku update agum
#         frappe.db.commit()  # Confirm the change

#         context.msg = "Record Updated Successfully ✅"

#     context.doc = doc
#     return context

import frappe

def get_context(context):
    name = frappe.form_dict.name

    if frappe.request.method == "POST":
        # Update record
        doc = frappe.get_doc("Medical Record", name)
        doc.patient_name = frappe.form_dict.patient_name
        doc.diseases = frappe.form_dict.diseases
        doc.date = frappe.form_dict.date
        doc.doctor = frappe.form_dict.doctor
        doc.save()
        frappe.db.commit()
        context.msg = "Record updated successfully."

    doc = frappe.get_doc("Medical Record", name)
    context.doc = doc
    return context



