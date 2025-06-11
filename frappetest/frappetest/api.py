# import frappe


# @frappe.whitelist(allow_guest = True)
# def get_emoji():
#     return {"emoji" : "😅"}

import frappe

@frappe.whitelist()
def get_vehicle_chart_data():
    data = frappe.db.sql("""
        SELECT vehicle, COUNT(*) as count
        FROM `tabRide Order`
        GROUP BY vehicle
    """, as_dict=True)

    labels = [d["vehicle"] for d in data]
    values = [d["count"] for d in data]
    colors = ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF", "#FF9F40"]

    return {
        "labels": labels,
        "datasets": [{
            "name": "Ride Orders",
            "values": values,
            "chartType": "bar",
            "colors": colors[:len(labels)]
        }]
    }
