# Copyright (c) 2025, britvasan and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Article(WebsiteGenerator):
	
	def before_save(self):
		self.validate_isbn()

	def validate_isbn(self):
		if not self.isbn or len(self.isbn) not in [8, 10]:
			frappe.throw("Please enter a valid ISBN number (8 or 10 digits).")