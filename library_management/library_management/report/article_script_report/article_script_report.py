# Copyright (c) 2025, britvasan and contributors
# For license information, please see license.txt

import frappe
from frappe import _ 

def execute(filters=None):
    columns, data = get_colums(), get_values(filters)
    chart = get_chart_data(data)
    return columns, data, None, chart

def get_colums():
    columns = [
        {
            "fieldname":"article_name",
            "label": _("Article Name"),
            "fieldtype":"Data",
            "width": 250
        },
        {
            "fieldname":"author",
            "label": _("Author"),
            "fieldtype":"Data",
            "width": 200
        },
        {
            "fieldname":"isbn",
            "label": _("ISBN"),
            "fieldtype":"Data",
            "width": 200
        },
        {
            "fieldname":"status",
            "label": _("Status"),
            "fieldtype":"Select",
            "width": 150
        },
        {
            "fieldname":"publisher",
            "label": _("Publisher"),
            "fieldtype":"Data",
            "width": 200
        },
    ]

    return columns


def get_values(filters):
    condition = "1=1"

    if filters.get('article_name'):
        condition += f" AND A.article_name = '{filters.get('article_name')}'"
    if filters.get('author'):
        condition += f" AND A.author = '{filters.get('author')}'"
    if filters.get('isbn'):
        condition += f" AND A.isbn = '{filters.get('isbn')}'"
    if filters.get('status'):
        condition += f" AND A.status = '{filters.get('status')}'"
    if filters.get('publisher'):
        condition += f" AND A.publisher = '{filters.get('publisher')}'"

    query = f"""
        SELECT 
            A.article_name,
            A.author,
            A.isbn,
            A.status,
            A.publisher
        FROM
            `tabArticle` A
        WHERE
            {condition}
    """

    return frappe.db.sql(query, as_dict=1)


def get_chart_data(data):

    labels = ['Available', 'Issued']

    sts_count = {
        'Available': 0,
        'Issued': 0
    }
    

    for i in data:
        status = i.status
        if status == 'Available':
            sts_count['Available'] += 1
        else:
            sts_count['Issued'] += 1

        
    chart = {
        'data': {
            'labels':labels,
            'datasets':[
                {
                    'name':'Article Status',
                    'values':[
                        sts_count['Available'],
                        sts_count['Issued']
                    ]
                }
            ]
        },
        'type':'pie',
        'height':300
    }

    return chart



"""
# def get_values(filters):
#     condition = "1=1"
#     values = {}

#     if filters.get('article_name'):
#         condition += " AND A.article_name = %(article_name)s"
#         values['article_name'] = filters['article_name']

#     if filters.get('author'):
#         condition += " AND A.author = %(author)s"
#         values['author'] = filters['author']

#     if filters.get('isbn'):
#         condition += " AND A.isbn = %(isbn)s"
#         values['isbn'] = filters['isbn']

#     if filters.get('status'):
#         condition += " AND A.status = %(status)s"
#         values['status'] = filters['status']

#     if filters.get('publisher'):
#         condition += " AND A.publisher = %(publisher)s"
#         values['publisher'] = filters['publisher']

#     query = f"""
"""
#         SELECT 
#             A.article_name,
#             A.author,
#             A.isbn,
#             A.status,
#             A.publisher
#         FROM
#             `tabArticle` A
#         WHERE
#             {condition}
#     """
"""
#     return frappe.db.sql(query, values, as_dict=1)"""
