# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class AirplaneFlight(Document):
    def on_submit(self):
        self.status = "Completed"

    def after_insert(self):
        self.route = f"flights/{self.name}"
        self.save()

    def get_page_info(self):
        title = f"{self.source_airport} ➡️ {self.destination_airport} on {self.date_of_depature}"
        return {
            "title": title,
            "route": f"flights/{self.name}",
            "published": self.published,
        }

    def autoname(self):
        self.name = f"{self.airplane}-{self.date_of_depature}"