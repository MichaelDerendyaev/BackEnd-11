import unittest
import custom_list


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cl1 = custom_list.CustomList([1, 2, 3, 4, 5])
        self.cl2 = custom_list.CustomList([1, 2, 3, 4])
        self.ul1 = [1, 2, 3, 4, 5]
        self.ul2 = [1, 2, 3, 4]

    def test_add(self):
        self.assertEqual(self.cl1 + self.cl2, [2, 4, 6, 8, 5])
        self.assertEqual(self.cl1 + self.ul2, [2, 4, 6, 8, 5])
        self.assertEqual(self.ul1 + self.cl2, [2, 4, 6, 8, 5])

    def test_sub(self):
        self.assertEqual(self.cl1 - self.cl2, [0, 0, 0, 0, 5])
        self.assertEqual(self.cl1 - self.ul2, [0, 0, 0, 0, 5])
        self.assertEqual(self.ul1 - self.cl1, [0, 0, 0, 0, 0])
        self.assertEqual(self.cl2 - self.cl1, [0, 0, 0, 0, -5])
        self.assertEqual(self.ul2 - self.cl2, [0, 0, 0, 0])
        self.assertEqual(self.cl2 - self.ul1, [0, 0, 0, 0, -5])

    def test_comparison(self):
        self.assertTrue(self.cl1 > self.cl2)
        self.assertTrue(self.cl1 >= self.cl2)
        self.assertTrue(self.cl1 != self.cl2)
        self.assertFalse(self.cl1 < self.cl2)
        self.assertFalse(self.cl1 <= self.cl2)
        self.assertFalse(self.cl1 == self.cl2)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
