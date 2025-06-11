# frappetest/frappetest/www/airplane/airplane_ticket.py
import frappe
from frappe import _

@frappe.whitelist()
def passenger_details():
    passengers = frappe.get_all(
        "Flight Passenger", 
        fields=["name", "first_name", "last_name"]
    )
    return [
        {
            "name": p["name"],
            "full_name": f"{p['first_name']} {p['last_name']}"
        } for p in passengers
    ]
