# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ChatMessage(Document):
	pass

# sockit.io
# frappe.whitelist()
# def on_submit(doc, method):
# 		frappe.publish_realtime(
# 			event='new_chat_message',
# 			message = {
# 				'name':doc.name1,
# 				'phone':doc.phone_number,
# 				'address':doc.address
# 			}
# 		)