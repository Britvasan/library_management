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
            'fieldname': 'article',
            'fieldtype': 'Link',
            'label': _('Article'),
            'options': 'Article',
        },

        {
            'fieldname': 'library_member',
            'fieldtype': 'Link',
            'label': _('Library Member'),
            'options': 'Library Member',
        },

        {
            "fieldname": "type",
            "label": _("Type"),
            "fieldtype": "Select",
        },
        {
            "fieldname": "date",
            "label": _("Date"),
            "fieldtype": "Date",
        },
        {
            "fieldname": "from_date",
            "label": _("From Date"),
            "fieldtype": "Date",
        },
        {
            "fieldname": "to_date",
            "label": _("To Date"),
            "fieldtype": "Date",
        },
        

    ]
    return columns




def get_values(filters):
    condition = "1=1"

    if filters.get("article"):
        condition += f" AND L.article = '{filters.get('article')}'"

    if filters.get("library_member"):
        condition += f" AND L.library_member = '{filters.get('library_member')}'"

    if filters.get("type"):
        condition += f" AND L.type = '{filters.get('type')}'"
    
    if filters.get("date"):
        condition += f" AND L.date = '{filters.get('date')}'"

    if filters.get("from_date"):
          condition += f" AND LMS.from_date >= '{filters.get('from_date')}'"

    if filters.get("to_date"):
          condition += f" AND LMS.to_date <= '{filters.get('to_date')}'"

    query = f"""
        SELECT 
            L.article, 
            L.library_member, 
            L.type, 
            L.date,
            LMS.from_date,
            LMS.to_date
        FROM 
            `tabLibrary Transaction` L
        JOIN 
            `tabLibrary Membership` LMS
        ON 
            L.library_member = LMS.library_member
        WHERE 
            {condition}
        ORDER BY L.date DESC
    """

    return frappe.db.sql(query)

"""Alter Code"""
# def get_values(filters):
#     condition = ""

#     if filters.get("article"):
#         condition += f"L.article = '{filters.get('article')}'"

#     if filters.get("library_member"):
#         if condition:
#             # condition += " AND "
#             condition += f" AND L.library_member = '{filters.get('library_member')}'"

#     if not condition:
#         condition = "1=1"

#     query = f"""
#         SELECT 
#             L.article, 
#             L.library_member, 
#             L.`type`, 
#             L.date
#         FROM 
#             `tabLibrary Transaction` L
#         WHERE 
#             {condition}
#         ORDER BY L.date DESC
#     """

#     return frappe.db.sql(query, as_dict=True)


"""Example code"""

# a = frappe.db.sql(
#     """
#         SELECT name,
#         From 
#             `tabTest` as T
#         WHERE
#             T.name = %(equal)s
                
#     """,
#     {"equal" : filters}
#     return a
# )


