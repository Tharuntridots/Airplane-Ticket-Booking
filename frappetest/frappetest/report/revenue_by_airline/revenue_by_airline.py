import frappe
from frappe import _

def execute(filters=None):
    # Get all airlines
    airlines = frappe.get_all("Airline", fields=["name"])

    # Prepare a dict to store airline revenues
    airline_revenue = {airline.name: 0.0 for airline in airlines}

    # Fetch revenue from Airplane Ticket
    tickets = frappe.get_all(
        "Airplane Ticket",
        fields=["airline", "total_amount"],
        filters={"docstatus": ["!=", 2]}  # Exclude cancelled
    )

    # Aggregate revenue per airline
    for ticket in tickets:
        if ticket.airline in airline_revenue:
            airline_revenue[ticket.airline] += ticket.total_amount or 0.0

    # Prepare data for table
    data = []
    total_revenue = 0.0
    for airline, revenue in airline_revenue.items():
        data.append([airline, revenue])
        total_revenue += revenue

    # Column definitions
    columns = [
        {
            "label": _("Airline"),
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "label": _("Revenue"),
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    # Add chart
    chart = {
        "data": {
            "labels": [d[0] for d in data],
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [d[1] for d in data]
                }
            ]
        },
        "type": "donut"
    }

    # Summary
    summary = [
        {
            "label": "Total Revenue",
            "value": total_revenue,
            "indicator": "Green"
        }
    ]

    return columns, data, None, chart, summary
