#define a function that checks if the number is positive
def is_positive(a):
    if a > 0:
        return "is positive"
    elif a < 0:
        return "is negative"
        
#calling our function with positive integer
print(is_positive(3))
#calling our function with negative integer
print(is_positive(-1))
#calling our function with null integer
print(is_positive(0))
