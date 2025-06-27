# Copyright (c) 2025, britvasan and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(), get_values(filters or {})
	return columns, data


def get_columns():
	columns = [
		{
			"fieldname":"article_name",
			"label": _("Article Name"),
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"status",
			"label": _("Status"),
			"fieldtype":"Select",
			"width":150
		},
		{
			"fieldname":"library_member",
			"label":_("Library Member"),
			"fieldtype":"Link",
			"options":"Library Member",
			"width":150
		},
		{
			"fieldname":"paid",
			"label":_("Paid"),
			"fieldtype":"Check",
			"width":80
		},
		{
			"fieldname":"type",
			"label":_("Type"),
			"fieldtype":"Select",
			"width":150
		},
		{
			"fieldname":"date",
			"label":_("Date"),
			"fieldtype":"Date",
			"width":150
		},
		{
			"fieldname":"full_name",
			"label":_("Full Name"),
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"phone",
			"label":_("Phone"),
			"fieldtype":"Data",
			"width":150
		}
	]

	return columns

def get_values(filters):
	condition = "1=1"

	if filters.get('article_name'):
		condition += f" AND A.article_name = '{filters.get('article_name')}'"
	
	if filters.get('status'):
		condition += f" AND A.status = '{filters.get('status')}'"
	
	if filters.get('library_member'):
		condition += f" AND LM.library_member = '{filters.get('library_member')}'"
	
	if filters.get('paid'):
		condition += f" AND LM.paid = '{filters.get('paid')}'"
	
	if filters.get('type'):
		condition += f" AND LT.type = '{filters.get('type')}'"
	
	if filters.get('date'):
		condition += f" AND LT.date = '{filters.get('date')}'"

	if filters.get('full_name'):
		condition += f" AND LMR.full_name = '{filters.get('full_name')}'"
	
	if filters.get('phone'):
		condition += f" AND LMR.phone - '{filters.get('phone')}'"


	query = f"""
		SELECT
			A.article_name,
			A.status,
			LM.library_member,
			LM.paid,
			LT.type,
			LT.date,
			LMR.full_name,
			LMR.phone
		FROM
			`tabArticle` A
		LEFT JOIN
			`tabLibrary Transaction` LT
		ON
			LT.article = A.name
		LEFT JOIN
			`tabLibrary Membership` LM
		ON 
			LT.library_member = LM.library_member
		LEFT JOIN
			`tabLibrary Member` LMR
		ON 
			LMR.parent = LM.name
		WHERE
			{condition}
	"""
	return frappe.db.sql(query, as_dict=True)