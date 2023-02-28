class Form:
    def __init__(self, name, email, current_address, permanent_address):
        self.name = name
        self.email = email
        self.current_address = current_address
        self.permanent_address = permanent_address

    def __eq__(self, other):
        if isinstance(other, Form):
            return other.name == self.name and \
                other.email == self.email and \
                other.current_address == self.current_address and \
                other.permanent_address == self.permanent_address
        else:
            return False
