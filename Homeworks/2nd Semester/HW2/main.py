class ListMath:
    def __init__(self, values=None):
        self.lst_math = self.filter_values(values) if values != None else []

    @staticmethod
    def filter_values(values):
        filtered_lst = []
        for value in values:
            if isinstance(value,(int, float)) and not isinstance(value, bool):
               filtered_lst.append(value)
        return filtered_lst

    def __add__(self, other):
        if isinstance()
        return ListMath(self.lst_math + ListMath.filter_values(other))

    def __radd__(self, other):
        return ListMath(self.lst_math + ListMath.filter_values(other))

    def __sub__(self, other):
        return ListMath(self.lst_math - ListMath.filter_values(other))

    def __rsub__(self, other):
        return ListMath(ListMath.filter_values(other) - self.lst_math)

    def __mul__(self, other):
        return ListMath(self.lst_math * ListMath.filter_values(other))

    def __rmul__(self, other):
        return ListMath(ListMath.filter_values(other) * self.lst_math)

    def __truediv__(self, other):
        return ListMath(self.lst_math / ListMath.filter_values(other))

    def __rtruediv__(self, other):
        return ListMath(ListMath.filter_values(other) / self.lst_math)

    def __repr__(self):
        return f"{self.__class__.__name__}([{', '.join(map(str, self.lst_math))}])"

lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)
print(lst2)
assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"
assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"
res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"
lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"
lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="
lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"
lst = lst / 2
lst /= 13.0