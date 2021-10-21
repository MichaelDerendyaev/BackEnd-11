class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        newdct = {}
        for k, v in dct.items():
            if k.startswith('__'):
                newdct[k] = v
            else:
                newdct[f"custom_{k}"] = v
        if "__init__" in newdct:
            realInit = newdct["__init__"]
            def newInit(self, *args, **kwargs):
                realInit(self, *args, **kwargs)
                attrs = self.__dict__.copy()
                for k, v in attrs.items():
                    if not k.startswith('__'):
                        self.__dict__[f"custom_{k}"] = self.__dict__.pop(k)
            newdct["__init__"] = newInit
        return super(CustomMeta, cls).__new__(cls, name, bases, newdct)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


if __name__ == "__main__":
    inst = CustomClass()
    inst.custom_x
    inst.custom_val
    inst.custom_line()

    print(inst.__dict__)
    print(inst.__class__.__dict__)