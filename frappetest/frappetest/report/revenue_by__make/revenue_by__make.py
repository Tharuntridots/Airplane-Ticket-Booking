# import frappe

# def execute(filters=None):
# 	columns = [
# 		{"fieldname": "make", "label": "Make", "fieldtype": "Data"},
# 		{"fieldname": "amount", "label": "Amount", "fieldtype": "Currency"},
# 	]

# 	data = frappe.db.sql("""
# 		SELECT 
# 			v.make AS make,
# 			SUM(rb.amount) AS amount
# 		FROM 
# 			`tabRide Booking` rb
# 		JOIN 
# 			`tabVehicle` v ON rb.vehicle = v.name
# 		WHERE 
# 			rb.docstatus = 1
# 		GROUP BY 
# 			v.make
# 	""", as_dict=True)

# 	return columns, data
