import frappe

@frappe.whitelist()
def get_driver_chart_data():
    records = frappe.get_all("TestImport", fields=["firstname"])
    labels = [r.firstname for r in records]
    values = [1 for _ in records]  # Just count for demo

    return {
        "labels": labels,
        "datasets": [
            {
                "name": "Driver Count",
                "type": "bar",
                "values": values
            }
        ]
    }
