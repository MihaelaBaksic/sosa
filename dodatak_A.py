from cmath import nan
import getpass
import math


class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        return self.a / self.b

    def calculate_circumference(self) -> float:
        """Calculates circumference of rectangle, if a or b are negative, returns NaN"""
        if self.a < 0 and self.b < 0:
            return nan

        return self.a*self.b*2

    def calculate_log(x: float) -> float:
        """Calculate logarithm of given number, return NaN if x not positive"""
        if x < 0:
            return nan

        return math.log(x)




if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if user != "root" or password != "123":
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        a = float(input("A = "))
        b = float(input("B = "))
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_division())

