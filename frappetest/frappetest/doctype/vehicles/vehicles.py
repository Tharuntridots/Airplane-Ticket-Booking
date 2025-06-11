from frappe.website.website_generator import WebsiteGenerator

class Vehicles(WebsiteGenerator):
    def before_save(self):
        self.set_title()

    def set_title(self):
        self.title = f"{self.make} {self.model} {self.year}"




