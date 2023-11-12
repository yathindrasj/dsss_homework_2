import unittest
from math_quiz import limit, math_ops, numericals


class TestMathGame(unittest.TestCase):

    def test_function_random(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = limit(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_operation(self):
        # TODO
        listOps=['+' , '-' , '*' , '/' , '%']
        for i in listOps:
            available_operation = math_ops(random.choice(['+', '-', '*']))
            self.assertTrue(i==available_operation)
        pass

    def test_function_Calculation(self):
        test_cases = [
    (5, 2, '+', '5 + 2', 7),
    (3, 2, '-', '3 - 2', 1),
    (6, 5, '*', '6 * 5', 30),
    (8, 2, '/', '8 / 2', 4)
                     ]

       for num_1, num_2, operator, expected_problem, expected_answer in test_cases:
           calculated_problem, calculated_answer = numericals(num_1, num_2, operator)
           self.assertTrue (calculated_problem == expected_problem)
           self.assertTrue (calculated_answer == expected_answer)
           print(f"Test Passed: {calculated_problem} = {calculated_answer}")


if name == "main":
    unittest.main()
