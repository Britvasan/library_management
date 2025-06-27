// Copyright (c) 2025, britvasan and contributors
// For license information, please see license.txt

frappe.query_reports["Article Detailed Report"] = {
	"filters": [
		{
			"fieldname":"article_name",
			"label":__("Article Name"),
			"fieldtype":"Data",
		},
		{
			"fieldname":"status",
			"label":__("Status"),
			"fieldtype":"Select",
			"options": ["", "Issued", "Available"]
		},
		{
			"fieldname":"library_member",
			"label":__("Library Member"),
			"fieldtype":"Link",
			"options":"Library Member"
		},
		{
			"fieldname":"paid",
			"label":__("Paid"),
			"fieldtype":"Check"
		},
		{
			"fieldname": "type",
			"label": __("Type"),
			"fieldtype": "Select",
			"options": ["", "Issue", "Return"]
		},
		{
			"fieldname" : "date",
			"label" : __("Date"),
			"fieldtype": "Date",
		},
		{
			"fieldname":"full_name",
			"label":__("Full Name"),
			"fieldtype":"Data",
		},
		{
			"fieldname":"phone",
			"label":__("Phone"),
			"fieldtype":"Data",
		}
	]
};
