"""
En el mundo de la banca, la seguridad de las
 transacciones y la confiabilidad de
   las operaciones son vitales. 
   La programación orientada a objetos (POO) 
   puede ser una herramienta poderosa para 
   modelar cuentas bancarias y sus operaciones
   de una manera segura y fiable.
Problema:
Estás encargado de implementar un sistema 
simple pero seguro para manejar cuentas bancarias.
 Tu objetivo es crear una clase BankAccount
   que permita las siguientes operaciones: 
    - depósitos
    - retiros
    - consultar el balance
    aseguráte que todas las operaciones son 
        válidas y seguras. 

    La clase debe impedir que usuarios externos 
    accedan directamente y modifiquen el balance 
    de la cuenta, mientras que permitirá
    operaciones válidas a través de métodos 
    específicos.


Creando una instancia de BankAccount
account = BankAccount(1000)
Operaciones
account.deposit(500)         # Balance esperado: 1500
account.withdraw(200)        # Balance esperado: 1300
print(account.get_balance()) # Output esperado: 1300
Validaciones
account.set_balance(-1500)   # Mensaje esperado: "El balance no puede ser negativo."
account.withdraw(2000)       # Mensaje esperado: "El monto a retirar es inválido."
account.deposit(-200)        # Mensaje esperado: "El monto a depositar debe ser positivo."

"""

class BankAccount:
    """
    getters -> GET -> OBTIENE
    setters -> SET -> SETEA - CONFIGURA- ESTABLECE
    """

    def __init__(self, balance=0) -> None:
        self.__balance = balance

    def deposit(self, amount):
        # self.__balance = self.__balance + amount
        if amount <= 0:
            print("El monto a depositar debe ser positivo")
            return
        self.__balance += amount

    def withdraw(self, amount):
        """
        Realizar un retiro de dinero
        """
        # self.__balance = self.__balance - amount
        if self.__balance <= 0:
            print("No tienes fondos en tu cuenta")
            return
        if self.__balance < amount:
            print("No tienes fondos suficientes para hacer este retiro")
            return
        self.__balance -= amount
    
    @property
    def get_balance(self):
        return f"La cuenta tiene $ {self.__balance}"

    def set_balance(self, new_balance):
        self.__balance = new_balance

account = BankAccount()
print(account.get_balance)
account.deposit(1)
print(account.get_balance)
account.withdraw(10)
print(account.get_balance)

# account.set_balance(-1500)

# # Con el uso de un decorador.... 

# account.set_balance = 1000