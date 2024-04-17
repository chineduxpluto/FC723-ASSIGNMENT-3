class EuclideanAlgorithm:
    def __init__(self):
        """
        Initializes the Euclidean Algorithm

        """
        self.a = None
        self.b = None

    def get_input(self, number):
        """
        Prompts the user for input and valides it.
        """
        while True:
            try:
                value = int(input(number))
                if value < 0:
                    raise ValueError("Please enter a positive integer.")
                return value
            except ValueError as e:
                print(f"Invalid input: {e}")

    def calculate_gcd(self):
        """
        Calculates the  greatest common divisor of the two integers using the recursive euclidean algorithm
        :return: The greatest common divisor of the two integers
        """
        self.a = self.get_input("Enter the first positive number:  ")
        self.b = self.get_input(("Enter the second positive number: "))
        return self.gcd_recursive(self.a, self.b)

    def gcd_recursive(self, a, b):
        """
        A helper method that computes the GCD of two integers using recursion
        :param a: first integer
        :param b: second integer
        :return: the greatest common divisor (GCD) of a and b
        """
        if b == 0:
            return a
        else:
            return self.gcd_recursive(b, a % b)




if __name__ == "__main__":
    gcd_calculator = EuclideanAlgorithm()  # Create an instance of the class
    result = gcd_calculator.calculate_gcd()  # This method will handle input and calculation
    print(f"The GCD is: {result}")