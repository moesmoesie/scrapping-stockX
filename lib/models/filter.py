class Filter:
    def __init__(self, name, value,amount = None):
        self.name = name
        self.value = value
        self.amount = amount

    def __eq__(self,other):
        return (self.name == other.name) and (self.value == other.value)
    
    def __ne__(self,other):
        return not ((self.name == other.name) and (self.value == other.value))

if __name__ == "__main__":
    f1 = Filter("name",23,123)
    f2 = Filter("name",22,312312)
    print(f1 == f2)