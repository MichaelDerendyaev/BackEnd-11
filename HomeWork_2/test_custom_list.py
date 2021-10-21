import unittest
import custom_list


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cl1 = custom_list.CustomList([1, 2, 3, 4, 5])
        self.cl2 = custom_list.CustomList([1, 2, 3, 4])
        self.ul1 = [1, 2, 3, 4, 5]
        self.ul2 = [1, 2, 3, 4]
        self.sample_cl1_add_cl2 = custom_list.CustomList([2, 4, 6, 8, 5])
        self.sample_cl1_add_ul2 = custom_list.CustomList([2, 4, 6, 8, 5])
        self.sample_ul1_add_cl2 = self.sample_cl1_add_ul2
        self.sample_cl1_sub_cl2 = custom_list.CustomList([0, 0, 0, 0, 5])
        self.sample_cl1_sub_ul2 = custom_list.CustomList([0, 0, 0, 0, 5])
        self.sample_ul1_sub_cl1 = custom_list.CustomList([0, 0, 0, 0, 0])
        self.sample_cl2_sub_cl1 = custom_list.CustomList([0, 0, 0, 0, -5])
        self.sample_ul2_sub_cl2 = custom_list.CustomList([0, 0, 0, 0])
        self.sample_cl2_sub_ul1 = custom_list.CustomList([0, 0, 0, 0, -5])
        self.sample_comparisons = (True, True, True, False, False, False)

    def test_add(self):
        self.assertEqual(self.cl1 + self.cl2, self.sample_cl1_add_cl2)
        self.assertEqual(self.cl1 + self.ul2, self.sample_cl1_add_ul2)
        self.assertEqual(self.ul1 + self.cl2, self.sample_ul1_add_cl2)

    def test_sub(self):
        self.assertEqual(self.cl1 - self.cl2, self.sample_cl1_sub_cl2)
        self.assertEqual(self.cl1 - self.ul2, self.sample_cl1_sub_ul2)
        self.assertEqual(self.ul1 - self.cl1, self.sample_ul1_sub_cl1)
        self.assertEqual(self.cl2 - self.cl1, self.sample_cl2_sub_cl1)
        self.assertEqual(self.ul2 - self.cl2, self.sample_ul2_sub_cl2)
        self.assertEqual(self.cl2 - self.ul1, self.sample_cl2_sub_ul1)

    def test_comparison(self):
        self.assertEqual((self.cl1 > self.cl2,
                          self.cl1 >= self.cl2,
                          self.cl1 != self.cl2,
                          self.cl1 < self.cl2,
                          self.cl1 <= self.cl2,
                          self.cl1 == self.cl2),
                         self.sample_comparisons)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
