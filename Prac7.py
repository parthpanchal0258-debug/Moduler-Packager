
import datetime
import time
import math
import random
import string
import uuid
import os

def date_time():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Difference between two dates")
        print("3. Format date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        ch=input("Enter your choice: ")
        if ch=="1":
            print("Current Date and Time:",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif ch=="2":
            try:
                d1=datetime.date.fromisoformat(input("Enter first date (YYYY-MM-DD): "))
                d2=datetime.date.fromisoformat(input("Enter second date (YYYY-MM-DD): "))
                print("Difference:",abs((d2-d1).days),"days")
            except ValueError:
                print("Invalid date")
        elif ch=="3":
            print(datetime.datetime.now().strftime(input("Enter format (e.g. %d/%m/%Y): ")))
        elif ch=="4":
            input("Press Enter to start")
            start=time.time()
            input("Press Enter to stop")
            print("Elapsed time:",round(time.time()-start,2),"seconds")
        elif ch=="5":
            try:
                n=int(input("Enter seconds: "))
                while n>0:
                    print(n)
                    time.sleep(1)
                    n-=1
                print("Time's up!")
            except ValueError:
                print("Enter a valid number")
        elif ch=="6":
            break
        else:
            print("Invalid choice")

def mathematics():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        ch=input("Enter your choice: ")
        if ch=="1":
            try:
                n=int(input("Enter a number: "))
                if n<0:
                    print("Enter a non-negative number")
                else:
                    print("Factorial:",math.factorial(n))
            except ValueError:
                print("Invalid number")
        elif ch=="2":
            try:
                p=float(input("Enter principal amount: "))
                r=float(input("Enter rate of interest (%): "))
                t=float(input("Enter time (years): "))
                print("Compound Interest:",round(p*(1+r/100)**t,2))
            except ValueError:
                print("Invalid input")
        elif ch=="3":
            try:
                degree=float(input("Enter angle in degrees: "))
                angle=math.radians(degree)
                print("Sin:",round(math.sin(angle),2))
                print("Cos:",round(math.cos(angle),2))
                print("Tan:",round(math.tan(angle),2))
            except ValueError:
                print("Invalid angle")
        elif ch=="4":
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")
            shape=input("Enter your choice: ")
            try:
                if shape=="1":
                    r=float(input("Enter radius: "))
                    print("Area:",round(math.pi*r*r,2))
                elif shape=="2":
                    l=float(input("Enter length: "))
                    w=float(input("Enter width: "))
                    print("Area:",l*w)
                elif shape=="3":
                    b=float(input("Enter base: "))
                    h=float(input("Enter height: "))
                    print("Area:",0.5*b*h)
                else:
                    print("Invalid choice")
            except ValueError:
                print("Invalid input")
        elif ch=="5":
            break
        else:
            print("Invalid choice")

def random_data():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        ch=input("Enter your choice: ")
        if ch=="1":
            print("Random Number:",random.randint(1,100))
        elif ch=="2":
            try:
                n=int(input("Enter list length: "))
                if n<0:
                    print("Enter a positive length")
                else:
                    print("Random List:",[random.randint(1,100) for i in range(n)])
            except ValueError:
                print("Invalid number")
        elif ch=="3":
            try:
                n=int(input("Enter password length: "))
                if n<1:
                    print("Length must be positive")
                else:
                    chars=string.ascii_letters+string.digits+"@#$!"
                    password="".join(random.choice(chars) for i in range(n))
                    print("Generated Password:",password)
            except ValueError:
                print("Invalid length")
        elif ch=="4":
            print("Generated OTP:","".join(random.choices(string.digits,k=6)))
        elif ch=="5":
            break
        else:
            print("Invalid choice")

def generate_uuid():
    print("\nGenerated Unique Identifier:")
    print(uuid.uuid4())

def file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        ch=input("Enter your choice: ")
        if ch=="1":
            name=input("Enter file name: ")
            try:
                with open(name,"x") as f:
                    pass
                print("File created successfully!")
            except FileExistsError:
                print("File already exists")
        elif ch=="2":
            name=input("Enter file name: ")
            data=input("Enter data to write: ")
            try:
                with open(name,"w") as f:
                    f.write(data)
                print("Data written successfully!")
            except OSError:
                print("Unable to write file")
        elif ch=="3":
            name=input("Enter file name: ")
            try:
                with open(name,"r") as f:
                    print("File Content:")
                    print(f.read())
            except FileNotFoundError:
                print("File not found")
        elif ch=="4":
            name=input("Enter file name: ")
            data=input("Enter data to append: ")
            try:
                with open(name,"a") as f:
                    f.write("\n"+data)
                print("Data appended successfully!")
            except OSError:
                print("Unable to append data")
        elif ch=="5":
            break
        else:
            print("Invalid choice")

def explore_modules():
    modules={"math":math,"random":random,"time":time,"datetime":datetime,"uuid":uuid,"os":os,"string":string}
    name=input("Enter module name to explore: ")
    if name in modules:
        print("Available Attributes in",name,"module:")
        print(dir(modules[name]))
    else:
        print("Module not found. Try math, random, time, datetime, uuid, os or string.")

def main():
    while True:
        print("Welcome to Multi-Utility Toolkit")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        ch=input("Enter your choice: ")
        if ch=="1":
            date_time()
        elif ch=="2":
            mathematics()
        elif ch=="3":
            random_data()
        elif ch=="4":
            generate_uuid()
        elif ch=="5":
            file_operations()
        elif ch=="6":
            explore_modules()
        elif ch=="7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
