 #lets make a calculator which can be used to calculate values of desired 
print("choose a shape for further procedures: square, rectangle, circle, cube, cuboid - exit to exit the program")
while True:
    shape_data = input("what shape are we gonna calculate for: ").strip().lower()
    if shape_data == "exit":
        print("exiting..")
        break
    elif shape_data == "square":
        cal_square = input("what are we gonna calculate for the square: ")
        if cal_square == "area":
            square_edge = int(input("what is the length of edge of square: "))
            area_square = square_edge**2
            print("the value of area of the square is: ", area_square)   #area of square
        elif cal_square == "perimeter":
            square_edge = int(input("what is the perimeter of the square is: "))
            perimeter_square = 4*square_edge
            print("the vale of perimeter of the square is:", perimeter_square)  #perimeter of square
        else:
            print("invalid command")
    elif shape_data == "rectangle":
        cal_rectangle = input("what are we gonna calculate for the rectangle: ")
        if cal_rectangle == "area":
            length_rectangle = int(input("what is length of the rectangle: "))
            breadth_rectangle = int(input("what is the breadth of the rectangle: "))
            area_rectangle = length_rectangle*breadth_rectangle
            print("the value of area of the rectangle is: ", area_rectangle) #area of rectangle
        elif cal_rectangle == "perimeter":
            length_rectangle = int(input("what is length of the rectangle: "))
            breadth_rectangle = int(input("what is the breadth of the rectangle: "))
            perimeter_rectangle = 2*(length_rectangle + breadth_rectangle)
            print("the value of perimeter of the rectangle in cm is: ", perimeter_rectangle) #perimeter of rectangle
        else:
            print("invalid command")
    elif shape_data == "circle":
        cal_circle = input("what are we gonna calculate for the circle: ")
        if cal_circle == "area":
            radius_circle = int(input("what is the radius of circle: "))
            area_circle = 3.14*(radius_circle**2)
            print("the area of circle is: ", area_circle)    #area of circle
        elif cal_circle == "circumference" or cal_circle == "perimeter":
            radius_circle = int(input("what is the radius of circle: "))
            circumference_circle = 6.28*radius_circle
            print("the circumference of the circle in cm is: ", circumference_circle)    #circumference of circle
        else:
            print("invalid command")
    elif shape_data == "triange":
        cal_triangle = input("what are we gonna calculate for triangle: ")
        if cal_triangle == "perimeter":
            triangle_a = int(input("what is value of side A of triangle: "))
            triangle_b = int(input("what is value of side B of triangle: "))
            triangle_c = int(input("what is value of side C of triangle: "))
            perimeter_triangle = triangle_a + triangle_b + triangle_c
            print("the perimeter of the triangle in cm is ", perimeter_triangle)    #perimeter of triangle
        elif cal_triangle == "area":
            triangle_base = int(input("what is the value of base of the triangle: "))
            triangle_height = int(input("what is the value of height of the triangle: "))
            area_triangle = 0.5*triangle_base*triangle_height
            print("the area of the triangle is ", area_triangle)    #area of triangle
        else:
            print("invalid command")
    elif shape_data == "parallelogram":
        cal_parallelogram = input("what are we gonna calculate for parallelogram: ")
        if cal_parallelogram == "perimeter":
            side_a = int(input("what is value of side A of parallelogram: "))
            side_b = int(input("what is value of side B of parallelogram: "))
            side_c = int(input("what is value of side c of parallelogram: "))
            perimeter_parallelogram = side_a+side_b+side_c
            print("the perimeter of the parallelogram in cm is: ", perimeter_parallelogram) #perimeter of parallelogram
        elif cal_parallelogram == "area":
            base_parallelogram = int(input("what is the base of parallelogram: "))
            height_parallelogram = int(input("what is heigh of the parallelogram: "))
            area_parallelogram = base_parallelogram*height_parallelogram
            print("the area of the parallelogram is: ", area_parallelogram) #area of the parallelogram
        else:
            print("invalid command")  
    else:
        print("invalid function")
else:
    print("the program is still under development to calculate for that shape.. try again for something else from - circle, square, triangle, rectangle and parallelogram")
