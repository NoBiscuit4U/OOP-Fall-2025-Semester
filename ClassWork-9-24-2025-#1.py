options=["Area of Rectangle","Volume of Cube","Area of Circle","Volume of Circle","Volume of a Sphere"]
r=0

def area_rectangle(length,width):
    return length*width

def volume_cube(side_length):
    return side_length**3

def area_circle(radius):
    return (radius**2)*3.14

def circumference_circle(radius):
    return 2*radius*3.14

def volume_sphere(radius):
    return (4/3)*(3.14*(radius**3))

while 1:
    for i in range(0,len(options)):
        print(i," "+options[i])

    selection=int(input("Enter Desired Operation: "))

    if 2 <= selection <= 4:
        r=float(input("Enter Radius: "))

    if selection==0:
        values=input("Enter Values for Length and Width, format l,w: ").split(",")
        l=float(values[0])
        w=float(values[1])

        print("Area of Rectangle is: ",area_rectangle(l,w))

    elif selection==1:
        s_l = float(input("Enter Values for Side Length: "))
        print("Volume of Cube is : ",volume_cube(s_l))

    elif selection==2:
        print("Area of Circle is: ", area_circle(r))

    elif selection==3:
        print("Circumference of Circle is: ", circumference_circle(r))

    elif selection==4:
        print("Volume of Sphere is: ", volume_sphere(r))