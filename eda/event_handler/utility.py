import frappe

class json_validater:    
    def __init__(self,payload) -> None:
        self.module = payload["module"]
        self.function = payload["function"]
        self.argument = payload["argument"]
        self.doc_uuid = payload["doc_uuid"]
        self.hash = payload["hash"]

    def get_module(self):
        return self.module
    def get_function(self):
        return self.function
    def get_argument(self):
        return self.argument
    def get_doc_uuid(self):
        return self.doc_uuid
    def get_hash(self):
        return self.hash
