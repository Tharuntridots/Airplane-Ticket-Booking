// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt
frappe.query_reports["Airline Revenue Report"] = {
    "filters": [
        {
            "fieldname": "include_cancelled",
            "label": __("Include Cancelled"),
            "fieldtype": "Check",
            "default": 0
        }
    ]
}
;
