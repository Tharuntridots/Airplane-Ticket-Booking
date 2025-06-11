import frappe
from frappe.model.document import Document

class MedicalRecord(Document):
    def validate(self):
        if not self.doctor:
            frappe.throw("Doctor is required.")
        if "virus" in self.diseases.lower():
            frappe.msgprint("Handle with care! Viral infection detected.")
