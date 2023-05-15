import frappe



class validater:
    def __init__(self,record:dict,keys:list=[]):
        for key in keys:
            if key not in record:
                frappe.throw(f"{key} is missing")