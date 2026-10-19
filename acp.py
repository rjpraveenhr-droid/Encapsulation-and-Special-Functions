
class Account:
    def __init__(self, name, pin):
        self.name = name
        self.__pin = pin

    def set_pin(self, new_pin):
        if len(str(new_pin)) == 4 and str(new_pin).isdigit():
            self.__pin = str(new_pin)
            print("PIN updated successfully!")
        else:
            print("Invalid PIN! PIN must contain 4 digits.")

    def __str__(self):
        return "Account Holder: " + self.name + "\nPIN: ****"


account1 = Account("Tabitha", "1234")

print(account1)

try:
    print(account1.__pin)
except AttributeError:
    print("Connot access private PIN directly!")

account1.set_pin("5678")
print(account1)