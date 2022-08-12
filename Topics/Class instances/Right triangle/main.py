class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here

    def area(self):
        print((self.a * self.b) / 2)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here

triangle = RightTriangle

if pow(input_c, 2) == pow(input_a, 2) + pow(input_b, 2):
    triangle(hyp=input_c, leg_1=input_a, leg_2=input_b).area()
else:
    print("Not right")
