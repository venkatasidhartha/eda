import frappe

class json_validater:    
    def __init__(self,payload) -> None:
        self.module = payload["module"]
        self.function = payload["function"]
        self.argument = payload["argument"]

    def get_module(self):
        return self.module
    def get_function(self):
        return self.function
    def get_argument(self):
        return self.argument
