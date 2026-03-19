class Transactions:
    # Constructor
    def __init__(self, taID, category_ID, date, amount, description, type) -> None:
        self.taID = taID
        self.category_ID = category_ID
        self.date = date
        self.amount = amount
        self.description = description
        self.type = type

    # Getter/Setters:
    def get_taID(self):
        return self.taID
    def set_taID(self, taID):
        self.taID = taID

    def get_category_ID(self):
        return self.category_ID
    def set_category_ID(self, category_ID):
        self.category_ID = category_ID

    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date

    def get_amount(self):
        return self.amount
    def set_amount(self, amount):
        self.amount = amount

    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description

    def get_type(self):
        return self.type
    def set_type(self, type):
        self.type = type

    # Formatting string for proper outputs:
    def __str__(self):
        return f"{self.date} | {self.type.upper()} | ${self.amount:.2f} | {self.description}"