APPROVED_JOBS = [
    "Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal",
    "Finance", "Sales", "General Management", "Research & Development",
    "Marketing", "Purchasing"
]

class Person:
    def __init__(self, name="Not provided", job="Admin"):
        self._name = None
        self._job = None

        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            return  # Stop here if name is invalid

        if job in APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
