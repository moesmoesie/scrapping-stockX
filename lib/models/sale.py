sale_id = "chainId"
timestamp = "createdAt"
shoe_size = "shoeSize"
amount = "amount"

class Sale:
    def __init__(self, json,product_id):
        self.id = json[sale_id]
        self.timestamp = json[timestamp]
        self.shoe_size = json[shoe_size]
        self.amount = json[amount]
        self.product_id = product_id

    def get_attributes_tuple(self):
            return (
                self.id,
                self.timestamp,
                self.shoe_size,
                self.amount,
                self.product_id
            )