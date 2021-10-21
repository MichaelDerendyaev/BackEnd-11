class CustomList(list):
    def __add__(self, other):
        a = len(self)
        b = len(other)
        ans = CustomList([])
        if a < b:
            for i in range(a):
                ans.append(self[i] + other[i])
            for i in range(a, b):
                ans.append(other[i])
        else:
            for i in range(b):
                ans.append(self[i] + other[i])
            for i in range(b, a):
                ans.append(self[i])
        return ans

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        a = len(self)
        b = len(other)
        ans = CustomList([])
        if a < b:
            for i in range(a):
                ans.append(self[i] - other[i])
            for i in range(a, b):
                ans.append(-other[i])
        else:
            for i in range(b):
                ans.append(self[i] - other[i])
            for i in range(b, a):
                ans.append(self[i])
        return ans

    def __rsub__(self, other):
        a = len(self)
        b = len(other)
        ans = CustomList([])
        if a < b:
            for i in range(a):
                ans.append(-self[i] + other[i])
            for i in range(a, b):
                ans.append(other[i])
        else:
            for i in range(b):
                ans.append(-self[i] + other[i])
            for i in range(b, a):
                ans.append(-self[i])
        return ans

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)


if __name__ == "__main__":
    a = CustomList([1, 2, 3, 4, 5])
    b = CustomList([3, 4, 5])
    c = [-1, -2, -3, -4]
    print(a+b)
    print(a+c)
    print(b+c)
    print(c+a)
    print(c+b)
    print(a-b)
    print(a-c)
    print(b-c)
    print(c-a)
    print(c-b)
    print(a >= b)
