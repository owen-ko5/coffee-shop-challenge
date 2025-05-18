class Customer:
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) != str:
            print("Error: Name must be a string.")
            
        if len(name) < 1 or len(name) > 15:
            print("Error: Name must be between 1 and 15 characters.")

            
        self._name = name