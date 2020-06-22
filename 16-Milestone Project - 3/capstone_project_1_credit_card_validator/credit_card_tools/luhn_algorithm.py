"""
Basic implementation of Luhn's algorithm.

Takes in a number and returns if the number is valid
or not according to Luhn's Algorithm:
https://en.wikipedia.org/wiki/Luhn_algorithm

"""
class LuhnAlgorithm():

    def __init__(self, number):
        """
        Init method.
        """
        # Original number.
        self.number = number

        # Generate reversed list of original number.
        self.numlist = []
        self.convert_num_to_list_arithmetic()

        # Luhn's algorithm processes numbers from right to left.
        # In order to keep things easier, reverse the list of numbers
        # and process them from left to right.
        self.numlist.reverse()

        # Calculate normalized numbers.
        self.normlist = []
        self.generate_normalized_list()

        # If the total modulo 10 is equal to 0 (if the total ends in zero)
        # then the number is valid according to the Luhn formula; else it is not valid.
        self.sum = sum(self.normlist)
        self.is_valid = self.sum % 10 == 0

    def generate_normalized_list(self):
        """
        Generate a list of normalized numbers following this logic:
        If doubling of a number results in a two digits number i.e
        greater than 9(e.g., 6 × 2 = 12), then add the digits of the
        product (e.g., 12: 1 + 2 = 3, 15: 1 + 5 = 6),
        to get a single digit number.
        """
        for index, num in enumerate(self.numlist):
            if index % 2 == 0:
                self.normlist.append(num)
            else:
                if num * 2 > 9:
                    prod_list = [int(x) for x in str(num * 2)]
                    self.normlist.append(sum(prod_list))
                else:
                    self.normlist.append(num * 2)

    def convert_num_to_list_arithmetic(self):
        """
        Convert a number of any length to a list of all of its digits.
        """
        abs_number = abs(self.number)

        while abs_number != 0:
            # Append the remainder of dividing the number by 10.
            self.numlist.append(abs_number % 10)
            # Divide the number by 10 and round down.
            abs_number = abs_number // 10

        # Correct last item in list if number was negative.
        if self.number < 0:
            self.numlist[-1] = -abs(self.numlist[-1])

        # Reverse the list.
        self.numlist.reverse()

    @staticmethod
    def convert_positive_num_to_list_pythonic(number):
        """
        Convert a positive number of any length to a list of all of its digits.
        """
        # Using maps.
        # return list(map(int, str(number)))

        # Using list comprehension.
        return [int(x) for x in str(number)]
