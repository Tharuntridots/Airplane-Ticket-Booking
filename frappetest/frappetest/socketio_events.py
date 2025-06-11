import frappe
from frappe_socketio import socketio

@socketio.on("send_chat_message")
def handle_send_message(data):
    try:
        room_name = data.get("room")
        phone = data.get("phone")
        address = data.get("address")

        # Fetch or create Chat Room
        chat_rooms = frappe.get_all("Chat Room", filters={"room_name": room_name})
        if chat_rooms:
            room = frappe.get_doc("Chat Room", chat_rooms[0].name)
        else:
            room = frappe.get_doc({
                "doctype": "Chat Room",
                "room_name": room_name
            })
            room.insert()

        # Append message to child table
        room.append("messages", {
            "phone": phone,
            "address": address
        })
        room.save()

        # Emit back to all clients
        socketio.emit("new_chat_message", {
            "room": room_name,
            "phone": phone,
            "address": address
        })

    except Exception as e:
        frappe.log_error(message=str(e), title="SocketIO Chat Error")
