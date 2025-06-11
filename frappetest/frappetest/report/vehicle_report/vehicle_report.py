import frappe

def execute(filters=None):
    columns = [
        {"label": "Vehicle", "fieldname": "vehicle", "fieldtype": "Data", "width": 150},
        {"label": "Total Rides", "fieldname": "ride_count", "fieldtype": "Int", "width": 100}
    ]

    data = frappe.db.sql("""
        SELECT vehicle, COUNT(*) as ride_count
        FROM `tabRide Order`
        GROUP BY vehicle
    """, as_dict=True)

    chart = {
        "data": {
            "labels": [d["vehicle"] for d in data],
            "datasets": [
                {
                    "name": "Total Rides",
                    "values": [d["ride_count"] for d in data]
                }
            ]
        },
        "type": "line"
    }

    return columns, data, chart

# def execute(filters= None):
#     columns = [
#         {"label": "Vehicle", "fieldname": "vehicle", "fieldtype": "Data", "width" : 150},
#         {"label": "Total Rides", "fieldname": "ride_count", "fieldtype": "Int", "width": 150}

#     ]

#     data = frappe.db.sql(""" 
#         SELECT vehicle, COUNT(*) as ride_count
#         FROM `tabRide Order`
#         GROUP BY vehicle    
#     """,as_dict= True)

#     chart = {
#         "data": {
#             "labels": [d["vehicle"] for d in data],
#             "datasets": [
#                 {
#                     "name": "Total Rides", 
#                     "values": [d["ride_count"] for d in data]
#                 }
#             ]
            
#         }, 
#         "type" : "line"
#     }

