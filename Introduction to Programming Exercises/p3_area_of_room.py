# Exercise 3: Area of a Room
# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.
ChooseUnit=input("Enter the width and length of a room. For feet(1) or meters (2): ")
if ChooseUnit=="1":
    width=float(input("Enter the width of the room in feet: "))
    length=float(input("Enter the length of the room in feet: "))
    area=width*length
    print("The area of the room is",area,"square feet.")
elif ChooseUnit=="2":
    width=float(input("Enter the width of the room in meters: "))
    length=float(input("Enter the length of the room in meters: "))
    area=width*length
    print("The area of the room is",area,"square meters.")
    
# Exercise 3: Area of a Room
# **********************************************************************************************************************   
                                                # Method 2 by chatgpt
# **********************************************************************************************************************  
def calculate_area(length, width):
    area = length * width
    return area

def main():
    # Get user input for length, width, and units
    length = float(input("Enter the length of the room in feet or meters: "))
    width = float(input("Enter the width of the room in feet or meters: "))
    unit = input("Enter the unit of measurement (feet or meters): ").lower()

    # Calculate area and display the result
    area = calculate_area(length, width)
    print(f"The area of the room is {area} square {unit}.")

if __name__ == "__main__":
    main()
  
    