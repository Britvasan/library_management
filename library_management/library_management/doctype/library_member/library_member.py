# Copyright (c) 2025, britvasan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	# def before_save(self):
	# 	self.full_name = f'{self.first_name} {self.last_name or ""}'
		# self.validate_phone()
		# self.validate_email()
  
  
	def validate_email(self):
		if not self.email or "@" not in self.email:
			frappe.throw("Please enter a valid email address.")

	def validate_phone(self):
		if not self.phone.isdigit() or len(self.phone) != 10:
			frappe.throw("Phone number must be a 10-digit number.")
   
	
   
   

 
		