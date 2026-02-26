class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __lt__(self, other):
        if self.a < other.a or self.b < other.b or self.c < other.c:
            print("True")
        else:
            print("False")
    
    def __equal__(self, other):
        if self.a == other.a or self.b == other.b or self.c == other.c:
            print("True")
        else:
            print("False")
    
triangl1 = Triangle(4, 7, 9)
triangl2 = Triangle(4, 6, 10)
if triangl1<triangl2:
    print("Triangle 1 is smaller than triangle 2.")
else:
    print("Triangle 1 is greater than triangle 2.")

if triangl1==triangl2:
    print("Triangle 1 is equal to triangle 2.")
else:
    print("Triangle 1 is not equal to triangle 2.")
