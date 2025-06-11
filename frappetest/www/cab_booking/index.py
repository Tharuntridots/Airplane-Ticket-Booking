import frappe

def get_context(context):
    # Pass data from server to frontend
    context.custom_message = "Welcome to Cab Booking!"
