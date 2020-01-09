class ItemData:

    user = "Alex"
    job = "QA"
    url = 'http://localhost:5002/items'

    def __init__(self, user=user, job=job):
        self.user = user
        self.job = job

    def generate_new_item(self):
        item = {"user": self.user, "job": self.job}
        return item