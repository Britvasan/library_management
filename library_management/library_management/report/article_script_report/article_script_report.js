// Copyright (c) 2025, britvasan and contributors
// For license information, please see license.txt

frappe.query_reports["Article Script Report"] = {
	"filters": [
		{
			"fieldname":"article_name",
			"label": __("Article Name"),
			"fieldtype":"Link",
			"options" : "Article"
		},
		{
			"fieldname":"author",
			"label": __("Author"),
			"fieldtype":"Data",
		},
		{
			"fieldname":"isbn",
			"label": __("ISBN"),
			"fieldtype":"Data",
		},
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype":"Select",
			"options": ["", "Issued", "Available"]
		},
		{
			"fieldname":"publisher",
			"label": __("Publisher"),
			"fieldtype":"Data",
		}
	],

	// get_chart_data(columns, data) {
    //     const status_count = {};

    //     // Count each status
    //     data.forEach(row => {
    //         const status = row.status || "Unknown";
    //         if (!status_count[status]) {
    //             status_count[status] = 0;
    //         }
    //         status_count[status]++;
    //     });

    //     return {
    //         data: {
    //             labels: Object.keys(status_count),
    //             datasets: [
    //                 {
    //                     name: "Articles",
    //                     values: Object.values(status_count)
    //                 }
    //             ]
    //         },
    //         type: 'pie' // You can also use 'donut'
    //     };
    // }
};









