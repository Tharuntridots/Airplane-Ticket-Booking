from __future__ import unicode_literals
import frappe

# def execute(filters=None):
#     columns = [
#         {"label": "Driver ID", "fieldname": "driverid", "fieldtype": "Int", "width": 100},
#         {"label": "First Name", "fieldname": "firstname", "fieldtype": "Data", "width": 150},
#         {"label": "Last Name", "fieldname": "lastname", "fieldtype": "Data", "width": 150},
#         {"label": "Phone Number", "fieldname": "phonenumber", "fieldtype": "Data", "width": 120},
#         {"label": "License Number", "fieldname": "licensenumber", "fieldtype": "Data", "width": 150},
#     ]

#     data = frappe.db.get_all(
#         "TestImport",
#         fields=["driverid", "firstname", "lastname", "phonenumber" , "licensenumber"],
#         order_by="modified desc"
#     )

#     message = "Showing all driver records from TestImport"
    
#     return columns, data, message

def execute(filters = None):
	columns = [
		{"label" : "Driver ID", "fieldname": "driverid", "fieldtype": "Int", "width": 100},
		{"label" : "First Name", "fieldname": "firstname", "fieldtype": "Data", "width": 150}
	]
	data =frappe.db.get_all(
		"TestImport", 
		fields = ["driverid", "firstname"],
		order_by = "modified desc"
	)
	chart = get_vehicle_chart_data()
	frappe.log_error("Chart", chart)
	message = "Showing all driver record from TestImport"

	return columns, data, chart, message, None

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
