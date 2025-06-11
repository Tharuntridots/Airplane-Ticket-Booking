# import frappe

# def send_note_realtime(doc, method):
#     frappe.publish_realtime(
#         event="purchase_note_created",
#         message={
#             "name": doc.name,
#             "note_name": doc.note_name,
#             "amount": doc.amount,
#             "status": doc.status
#         },
#         user=None 
#     )


import frappe

def send_note_realtime(doc, method):
    frappe.publish_realtime(
        event='purchase_note_created',
        message={
            'name': doc.name,
            'note_name': doc.note_name,
            'amount': doc.amount,
            'status': doc.status
        },
        user=None 
       
    )
    
    frappe.logger().info(f"🔔 Sent realtime event for {doc.name}")
