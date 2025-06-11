app_name = "frappetest"
app_title = "Frappetest"
app_publisher = "tharun"
app_description = "this is for test purpose"
app_email = "tharun@example.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "frappetest",
# 		"logo": "/assets/frappetest/logo.png",
# 		"title": "Frappetest",
# 		"route": "/frappetest",
# 		"has_permission": "frappetest.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappetest/css/frappetest.css"
# app_include_js = "/assets/frappetest/js/frappetest.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappetest/css/frappetest.css"
# web_include_js = "/assets/frappetest/js/frappetest.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "frappetest/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "frappetest/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "frappetest.utils.jinja_methods",
# 	"filters": "frappetest.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "frappetest.install.before_install"
# after_install = "frappetest.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "frappetest.uninstall.before_uninstall"
# after_uninstall = "frappetest.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "frappetest.utils.before_app_install"
# after_app_install = "frappetest.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "frappetest.utils.before_app_uninstall"
# after_app_uninstall = "frappetest.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappetest.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappetest.tasks.all"
# 	],
# 	"daily": [
# 		"frappetest.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappetest.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappetest.tasks.weekly"
# 	],
# 	"monthly": [
# 		"frappetest.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "frappetest.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappetest.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappetest.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["frappetest.utils.before_request"]
# after_request = ["frappetest.utils.after_request"]

# Job Events
# ----------
# before_job = ["frappetest.utils.before_job"]
# after_job = ["frappetest.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"frappetest.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


# --------------------------------------------------------------------------------

# app_include_js = "/assets/frappetest/js/email_reminder.js"
# scheduler_events = {
#     "hourly": [
#         "frappetest.emailreminder.emailreminder.send_reminder"
#     ]
# }

# doc_events = {
#     "Chat Message": {
#         "on_submit": "frappetest.frappetest.doctype.chat_message.chat_message.on_submit"
#     }
# }

# webform_include_js = {
#     "Test ToDo": "public/js/custom_todo.js"
# }

# webform_include_css = {
#     "Test ToDo": "public/css/custom_todo.css"
# }


# doctype_js = {
#     "Test ToDo": "public/js/custom_todo.js"
# }

# doctype_css = {
#     "Test ToDo": "public/css/custom_todo.css"
# }

# # In hooks.py
# doctype_python = {
#     "Test ToDo": "frappetest.frappetest.doctype.test_todo.test_todo"
# }

# # hooks.py

# scheduler_events = {
#     "cron": {
#         "*/2 * * * *": [
#             "frappetest.background_task_demo.mark_tasks_completed",
#             "frappetest.background_task_demo.cancel_completed_tasks"
#         ]
#     }
# }


# app_include_js = "/assets/frappetest/js/chart_renderer.js"

# doctype_js = {
#     "TestImport": "public/js/testimport.js"
# }


# doctype_js = {
#     "TestImport": "public/js/testimport.js"
# }


# doc_events = {
#     "Purchase Note": {
#         "after_insert": "frappetest.frappetest.note_api.send_note_realtime"
#     }
# }


# app_include_js = "/assets/frappetest/js/samosa.js"


# # doctype_js = {
# #     "Samosa Shop": "public/js/samosa_shop.js"
# # }


# page_js = {
#     "vehicle-chart": "public/js/vehicle_chart.js"
# }



# ===================================================================================================================================================================================
#*** Important ***

# website_context = {
#     "favicon": "/assets/frappetest/images/favicon.png"
# }


# home_page = "Homepage"

web_form_include_js = {
    "flight-ticket-booking": "public/js/flight_ticket_booking.js"
}

app_include_js = [
    "https://checkout.razorpay.com/v1/checkout.js"
]

doctype_js = {
    "Airplane Ticket": "public/js/airplane_ticket.js"
}

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Desk app_include_js 

