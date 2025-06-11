# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Airplane(Document):
    def autoname(self):
        self.name = f"{self.airline}-{self.modal}"

