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
                if value < 0: #checks if value is greater than 0
                    raise ValueError("Please enter a positive integer.")
                return value
            except ValueError: #raises value error if number is not positive
                print(f"Invalid input")

    def calculate_gcd(self):
        """
        Calculates the  greatest common divisor of the two integers using the recursive euclidean algorithm
        :return: The greatest common divisor of the two integers
        """
        self.a = self.get_input("Enter the first positive number:  ") # fetch user input a from get_input method
        self.b = self.get_input("Enter the second positive number: ") # fetch user input b from get_input method
        return self.gcd_recursive(self.a, self.b) # compute the GCD using the recursive helper function

    def gcd_recursive(self, a, b): # define helper method
        """
        A helper method that computes the GCD of two integers using recursion
        :param a: first integer
        :param b: second integer
        :return: the greatest common divisor (GCD) of a and b
        """
        if b == 0: # first base case
            return a # return a as GCD
        if a == 0: # second base case
            return b # return b as GCD
        else:
            return self.gcd_recursive(b, a % b) # recursively apply the Euclidean Algorithm




if __name__ == "__main__":
    gcd_calculator = EuclideanAlgorithm()  # Create an instance of the class
    result = gcd_calculator.calculate_gcd()  # store result in a variable
    print(f"The GCD is: {result}") # print result