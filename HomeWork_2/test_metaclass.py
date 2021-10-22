import unittest
import metaclass


class MyTest(unittest.TestCase):
    def setUp(self) -> None:

        class Sample(metaclass = metaclass.CustomMeta):
            type_ = 1
            seria_ = 245
            code_ = 4455578

            def __init__(self, date, time, registration=True):
                self.date = date
                self.time = time
                self.reg = registration

            def deletion(self):
                self.reg = False
                self.date = 0
                self.time = 0

            def change(self):
                self.date, self.time = self.time, self.date

            def __add__(self, other):
                return Sample(self.date+other.date, self.time+other.time, self.reg and other.reg)

        self.sample_class = Sample(1, 45000, True)

    def test_attrs(self):
        self.assertRaises(AttributeError, lambda: self.sample_class.type_)
        self.sample_class.custom_type_
        self.assertRaises(AttributeError, lambda: self.sample_class.seria_)
        self.sample_class.custom_seria_
        self.assertRaises(AttributeError, lambda: self.sample_class.code_)
        self.sample_class.custom_code_
        self.assertRaises(AttributeError, lambda: self.sample_class.date)
        self.sample_class.custom_date
        self.assertRaises(AttributeError, lambda: self.sample_class.time)
        self.sample_class.custom_time
        self.assertRaises(AttributeError, lambda: self.sample_class.reg)
        self.sample_class.custom_reg
        self.assertRaises(AttributeError, lambda: self.sample_class.custom___init__)
        self.sample_class.__init__
        self.assertRaises(AttributeError, lambda: self.sample_class.deletion)
        self.sample_class.custom_deletion
        self.assertRaises(AttributeError, lambda: self.sample_class.change)
        self.sample_class.custom_change
        self.assertRaises(AttributeError, lambda: self.sample_class.custom___add__)
        self.sample_class.__add__

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
