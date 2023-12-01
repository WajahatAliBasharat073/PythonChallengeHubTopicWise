# Exercise 4: Area of a Field
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.
def area(len,width):
    area_in_feet=len*width
    areaInAcre=area_in_feet/43560
    return areaInAcre
def takeInpu():
    length=float(input("Enter the length of the field in feet: "))
    width=float(input("Enter the width of the field in feet: "))
    return length,width
def main():
    length,width=takeInpu()
    acre=area(length,width)
    print("The area of the field is",acre,"acres.")
main()