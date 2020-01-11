class my_responce():

    def __init__(self, responce):
        self.res = responce
    
    def raw(self):
        return self.res

    def json(self):
        return self.res.json()

    def status(self):
        return self.res.status_code
