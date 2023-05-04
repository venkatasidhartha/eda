import frappe



def eda_settings():
    return frappe.get_doc("EDA Settings")