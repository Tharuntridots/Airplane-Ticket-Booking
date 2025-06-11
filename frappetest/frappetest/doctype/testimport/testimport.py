# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class TestImport(Document):
#     pass


# # @frappe.whitelist()
# # def get_driver_details(driverid):
# #     return frappe.db.get_value(
# #         "TestImport",
# #         {"driverid": driverid},
# #         ["firstname", "lastname", "phonenumber"],
# #         as_dict=True
# #     )

# @frappe.whitelist()
# def get_driver_chart_data():
#     drivers = frappe.get_all("TestImport", fields=["firstname"])
#     names = [d.firstname for d in drivers if d.firstname]

#     from collections import Counter
#     name_count = Counter(names)

#     return {
#         "labels": list(name_count.keys()),
#         "datasets": [{
#             "name": "Driver Count",
#             "values": list(name_count.values())
#         }]
#     }

import frappe
from frappe.model.document import Document

class TestImport(Document):
    pass

@frappe.whitelist()
def get_driver_chart_data():
    data = {
        "labels": ["Jan", "Feb", "Mar"],
        "datasets": [
            {
                "name": "Drivers",
                "values": [10, 15, 7]
            }
        ]
    }
    chart = {
        "data": data,
        "type": "line",
        "colors": ["#7cd6fd"],
        "title": "Driver Data Chart",
        "height": 300
    }
    return chart
