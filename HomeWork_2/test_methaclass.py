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
        flag = False
        try:
            self.sample_class.type_
        except:
            flag = True
        self.assertTrue(flag)
        flag = False
        try:
            self.sample_class.custom_type_
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.seria_
        except:
            flag = True
        self.assertTrue(flag)
        flag = False
        try:
            self.sample_class.custom_seria_
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.code_
        except:
            flag = True
        self.assertTrue(flag)
        flag = False
        try:
            self.sample_class.custom_code_
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.date
        except:
            flag = True
        self.assertTrue(flag)
        flag = False
        try:
            self.sample_class.custom_date
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.time
        except:
            flag = True
        self.assertTrue(flag)
        flag = False
        try:
            self.sample_class.custom_time
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.reg
        except:
            flag = True
        self.assertTrue(flag)
        flag = False
        try:
            self.sample_class.custom_reg
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.__init__
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.custom___init__
        except:
            flag = True
        self.assertTrue(flag)
        flag = False
        try:
            self.sample_class.deletion
        except:
            flag = True
        self.assertTrue(flag)
        flag = False
        try:
            self.sample_class.custom_deletion
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.change
        except:
            flag = True
        self.assertTrue(flag)
        flag = False
        try:
            self.sample_class.custom_change
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.__add__
        except:
            flag = True
        self.assertTrue(not flag)
        flag = False
        try:
            self.sample_class.custom___add__
        except:
            flag = True
        self.assertTrue(flag)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
