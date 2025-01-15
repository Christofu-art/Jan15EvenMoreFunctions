def Max_Of_Three(a, b, c):
    if a >= b:
        if a >= c :
            return a
    if b >= c:
        return b
    return c

result = Max_Of_Three(50, 43, 100)
print("the largest number out of three: ", result)

def RectPerimeter(l, w):
    return l*2 + w*2

result = RectPerimeter(5, 20)
print("The perimeter of that rectangle are: ", result)

def SumUpNums(a):
    sum = 0
    for i in range (a+1):
        sum += i
    return sum

result = SumUpNums(5)
print("the sum of a bunch of numbers", result)

def dogwoof(num, name):
    for i in range(num, 0, -1):
        print(name, "says woof")
        
dogwoof(3, "Luna/Recess")