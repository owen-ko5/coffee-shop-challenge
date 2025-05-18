class coffee:
    def __init__(self, name):
        self.name = name
        if type(name) != str:
            print("name is not a string")
            

        if len(name) <3:
            print(" name must be at least 3 characters")
            

    def get_name(self):
        return self._name       