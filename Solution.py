import unittest

def find_sum(a, b):
    return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = find_sum(num1, num2)
print("The sum is:", result)

class TestFindSum(unittest.TestCase):
    def test_positive_numbers(self):
        result = find_sum(5, 10)
        self.assertEqual(result, 15)

    def test_negative_numbers(self):
        result = find_sum(-8, -3)
        self.assertEqual(result, -11)

    def test_mixed_numbers(self):
        result = find_sum(2.5, -1.5)
        self.assertEqual(result, 1.0)

if __name__ == '__main__':
    unittest.main()