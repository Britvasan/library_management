// Copyright (c) 2025, britvasan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Order Items', {
    rate(frm, cdt, cdn) {
        calculate_row_total(frm, cdt, cdn);
    },
    quantity(frm, cdt, cdn) {
        calculate_row_total(frm, cdt, cdn);
    }
});

function calculate_row_total(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    row.total = (row.rate) * (row.quantity);
    frm.refresh_field('orders');
    calculate_total_amount(frm);
}

function calculate_total_amount(frm) {
    let total = 0;
    (frm.doc.orders || []).forEach(row => {
        total += row.total;
    });
    frm.set_value('total', total);
}

