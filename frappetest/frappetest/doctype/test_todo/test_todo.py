# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class TestToDo(Document):
    def before_save(self):
        # This will show a message in the UI (if called from Desk)
        frappe.msgprint("Hello from server-side Test ToDo before_save!")

        # This logs to the server logs
        frappe.logger().info(f"Saving Test ToDo with task: {self.task}")

        # Example: Add validation
        if not self.task or len(self.task.strip()) < 3:
            frappe.throw("Task must be at least 3 characters long.")

