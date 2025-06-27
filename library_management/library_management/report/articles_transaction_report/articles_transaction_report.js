	// Copyright (c) 2025, britvasan and contributors
	// For license information, please see license.txt



	frappe.query_reports["Articles Transaction Report"] = {
		"filters": [
			{
				'fieldname': 'article',
				'label': __('Article'),
				'fieldtype': 'Link',
				'options': 'Article',
			},

			{
				'fieldname': 'library_member',
				'label': __('Library Member'),
				'fieldtype': 'Link',
				'options': 'Library Member',
			},	

			{
				'fieldname': 'type',
				'label': __('Type'),
				'fieldtype': 'Select',
				'options': ['', 'Issue', 'Return'],
			},

			{
				'fieldname' : 'date',
				'label' : __('Date'),
				'fieldtype': 'Date',
			},

			{
				'fieldname': 'from_date',
				'label': __('From Date'),
				'fieldtype': 'Date',
			
			},
			{
				'fieldname': 'to_date',
				'label': __('To Date'),
				'fieldtype': 'Date',
			
			},

		]
	};
