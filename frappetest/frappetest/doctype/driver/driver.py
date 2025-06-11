# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Driver(Document):
    def before_save(self):
        frappe.msgprint("Running before_save")
        self.full_name = f"{self.firstname} {self.lastname}"

    def send_alert(self):
        print("send message")
