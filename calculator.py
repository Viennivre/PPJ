from stat import IO_REPARSE_TAG_APPEXECLINK


name=input("what is your name?: ")
year_of_birth=input("What year were you born?: ")
current_year=input("What year are we in?: ")
age=int(current_year)-int(year_of_birth)
print(" ")
print(f"Dear {name} you are {age} years old")
print("  ")
females=input("How many number of females are in your class? ")
males=input("How many number of males are in your class? ")
percentage_of_females=(int(females)/(int(females)+int(males)))*100
print(f"If there are {females} women and {males} men in your class, that means the percentage of women in your class is {percentage_of_females}% ")