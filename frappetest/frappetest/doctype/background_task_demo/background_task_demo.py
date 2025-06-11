import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime
from datetime import timedelta


class BackgroundTaskDemo(Document):

    def before_insert(self):
        self.status = "Pending"

    @staticmethod
    def mark_tasks_completed():
        tasks = frappe.get_all("Background Task Demo", filters={"status": "Pending"}, fields=["name"])
        for task in tasks:
            doc = frappe.get_doc("Background Task Demo", task.name)
            doc.status = "Completed"
            doc.last_updated = now_datetime()
            doc.save()

    @staticmethod
    def cancel_completed_tasks():
        tasks = frappe.get_all("Background Task Demo", filters={"status": "Completed"}, fields=["name", "last_updated"])
        for task in tasks:
            doc = frappe.get_doc("Background Task Demo", task.name)
            if doc.last_updated and now_datetime() >= doc.last_updated + timedelta(minutes=2):
                doc.status = "Cancelled"
                doc.save()



	# def before_insert(self):
	# 	self.status = "Pending"

	# def after_insert(self)
	# 	frappe.enqueue_doc(
	# 		doctype = self.doctype,
	# 		name= self.name,
	# 		method = "do_something",
	# 		queue = "short",
	# 		timeout= 1500
	# 	)
	# def do_something(self):
	# 	time.sleep(60)

	# 	self.status = "completed"
	# 	self.save()