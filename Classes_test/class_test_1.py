class A:
    class_var="sooraj"

    def test(self):
        self.a="value"
        print("a")

    def statmeth(a):
        A.class_var="pappu"
        return a+30



#A.statmeth=staticmethod(A.statmeth)
print(A.statmeth(10))
print(A.class_var)


