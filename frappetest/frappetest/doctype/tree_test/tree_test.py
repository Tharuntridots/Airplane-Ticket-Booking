# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet


class TreeTest(NestedSet):
	pass

@frappe.whitelist()
def get_children(parent=None, is_root=False):
    if is_root:
        parent = ""
    return frappe.get_list("Tree Test", 
        fields=["name as value", "is_group", "name1"],
        filters={"parent_tree_test": parent},
        order_by="name"
    )

@frappe.whitelist()
def add_node(parent, name1, is_group):
    new_node = frappe.get_doc({
        "doctype": "Tree Test",
        "parent_tree_test": parent,
        "name1": name1,
        "is_group": is_group
    })
    new_node.insert()
    return new_node

@frappe.whitelist()
def make_child(source_name):
    doc = frappe.get_doc("Tree Test", source_name)
    child = frappe.new_doc("Tree Test")
    child.parent_tree_test = doc.name
    return child
