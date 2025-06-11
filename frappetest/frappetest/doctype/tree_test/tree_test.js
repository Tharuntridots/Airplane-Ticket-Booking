// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Tree Test", {
// 	refresh(frm) {

// 	},
// });


frappe.treeview_settings['Tree Test'] = {
    title: 'Tree Test Hierarchy',
    breadcrumb: 'Frappetest',
    get_tree_nodes: 'frappetest.frappetest.doctype.tree_test.tree_test.get_children',
    add_tree_node: 'frappetest.frappetest.doctype.tree_test.tree_test.add_node',
    
    // Fields required for creating a child
    fields: [
        {
            fieldtype: 'Data',
            fieldname: 'name1',
            label: 'New Node Name',
            reqd: true
        },
        {
            fieldtype: 'Check',
            fieldname: 'is_group',
            label: 'Is Group'
        }
    ],

    // Optional filters (visible at top of treeview)
    filters: [
        {
            fieldname: 'is_group',
            fieldtype: 'Check',
            label: 'Show Groups Only',
            default: 0,
            on_change: function() {
                frappe.treeview_settings['Tree Test'].treeview.reload();
            }
        }
    ],

    extend_toolbar: true,
    toolbar: [
        {
            label: 'Add Child',
            condition: function(node) {
                return node.data && node.data.is_group;
            },
            click: function(node) {
                frappe.model.open_mapped_doc({
                    method: 'frappetest.frappetest.doctype.tree_test.tree_test.make_child',
                    source_name: node.data.name
                });
            }
        }
    ]
};
