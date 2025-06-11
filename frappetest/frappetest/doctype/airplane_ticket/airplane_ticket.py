# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
    def validate(self):
        total_add_ons = 0
        for item in self.add_ons:
            if item.amount:
                total_add_ons += item.amount

        self.total_amount = (self.flight_price or 0) + total_add_ons

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Cannot submit unless status is 'Boarded'.")

        
    # def before_save(self):
    #     if not self.seat:
    #         number = random.randint(1, 200)
    #         letter = random.choice(["A", "B", "C", "D", "E"])
    #         self.seat = f"{number}{letter}"

        


