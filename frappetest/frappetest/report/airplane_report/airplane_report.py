# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = [
		{
			"label" : _("Airline"),
			"fieldname": "airline",
			"fieldtype": "link",
			"options": "Airline",
			"width": 200
		},
		{
			"label" : ("Airplane Count"),
			"fieldname" : "count",
			"fieldtype": "Int",
			"width": 150
		}
	]

	data = frappe.db.sql("""
		SELECT airline, COUNT(name) AS count
		FROM `tabAirplane`
		GROUP BY airline

	""", as_dict= True)

	return columns, data