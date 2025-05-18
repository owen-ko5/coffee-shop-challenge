class order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
    

        if type(customer) != customer:
          print("customer muast be ann object")
          return
        
        if type(coffee) != coffee:
           print("coffee must be an object")
           return
        
        if type(price) != price:
           print("price must me a number")

    def get_coffee(self):
       return self._coffee
    
    def get_customer(self):
       return self._customer
    
    def get_price(self):
       return self._customer
