import frappe



def check_keys(arr:list,record_dict:dict):
    for i in arr:
        if i not in record_dict:
            pass 