class Item:
    pay_rate = 0.8 #Pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #run validations to the received args
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        #Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity #encapsulation

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property #Read-only attribute
    def name(self):
        print("You are trying to get name")
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name is too long!")
        else:
            self.__name = value
    
    def calculate_total_price(self):
        return self.__price * self.quantity

    @staticmethod
    def is_int(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    def connect(self, smpt_server):
        pass

    def prepare_body(self):
        return f"""
        Hi.
        We have {self.name} {self.quantity} times.
        Regards, Drancy"""
    
    def send():
        pass

    def send_email(self):
        self.connect()
        self.prepare_body()
        self.send()