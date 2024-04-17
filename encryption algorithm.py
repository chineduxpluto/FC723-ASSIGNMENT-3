class EuclideanAlgorithm:
    def __init__(self, a, b):
        """
        Initializes the Euclidean Algorithm with two integers
        :param a: first integer
        :param b: second integer
        """
        self.a = a
        self.b = b

    def calculate_gcd(self):
        """
        Calculates the  greatest common divisor of the two integers using the recursive euclidean algorithm
        :return: The greatest common divisor of the two integers
        """
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