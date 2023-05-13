import frappe
from frappe.model.naming import make_autoname


def producer_logs(doc, event=None):
	''' setting naming series for lead '''
	doc.name = make_autoname('P.####')
	
def consumer_logs(doc, event=None):
	''' setting naming series for lead '''
	doc.name = make_autoname('C.####')