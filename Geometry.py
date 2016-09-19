#  File: Geometry.py

#  Description: This program reads Geometry.txt file and determines volume, area, and intersections

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: February 19, 2015

#  Date Last Modified:February 20, 2015
import math

def is_equal (a, b):
  tol = 1.0e-16
  return (abs (x - y) < tol)

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z


  # create a string representation of a Point (x, y, z)
  def __str__ (self):
    s = '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    return s

  # get distance to another Point object
  def distance (self, other):
    x2 = (self.x - other.x) * (self.x - other.x)
    y2 = (self.y - other.y) * (self.y - other.y)
    z2 = (self.z - other.z) * (self.z - other.z)
    return ((x2 + y2 + z2) ** 0.5)

  # test for equality between two points
  def __eq__ (self, other):
    if is_equal (self.x, other.x) and is_equal (self.y, other.y) and (self.z, other.z):
      return True
    else: 
      return False


class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.center = Point (x, y, z)
    self.radius = radius

  # string representation of a Sphere: Center: (x, y, z), Radius: value
  def __str__ (self):
    s = "Center: " + str(self.center) + ", Radius: " + str(self.radius)
    return s

  # compute surface area of Sphere
  def area (self):
    return 4 * math.pi * self.radius * self.radius

  # compute volume of a Sphere
  def volume (self):
    return (4 / 3) * math.pi * ((self.radius) ** 3)

  # determines if a Point is strictly inside the Sphere
  def is_inside_point (self, p):
    dist = p.distance (self.center)
    return (dist < self.radius)

  # determine if another Sphere is strictly inside this Sphere
  def is_inside_sphere (self, other):
    dist = self.center.distance (other.center)
    return (self.radius > (dist + other.radius))

  # determine if a Cube is strictly inside this Sphere
  #distance of center of sphere + 1/2 diagonal 
  def is_cube_inside_sphere(self, a_cube):
    x = a_cube.center.x
    y = a_cube.center.y
    z = a_cube.center.z
    s = a_cube.side/2
    vertex = []
    vertex.append(Point(x+s, y+s, z+s))
    vertex.append(Point(x-s, y+s, z+s))
    vertex.append(Point(x+s, y+s, z-s))
    vertex.append(Point(x-s, y-s, z+s))
    vertex.append(Point(x-s, y-s, z-s))
    vertex.append(Point(x-s, y+s, z-s))
    vertex.append(Point(x-s, y-s, z-s))
    vertex.append(Point(x+s, y-s, z+s))

    for i in (vertex):
      if not self.is_inside_point(i):
        return False
    return True

  # determine if a Cylinder is strictly inside this Sphere
  def is_cylinder_inside_sphere (self, a_cyl):
    diagonal_cylinder = math.sqrt(((a_cyl.radius*2)**2) + (a_cyl.height**2))
    return (diagonal_cylinder <= (self.radius*2))

  # determine if another Sphere intersects this Sphere
  # there is a non-zero volume of intersection
  def does_intersect_sphere (self, other):
    dist = self.center.distance (other.center)
    return (dist < (self.radius + other.radius))


  # determine if a Cube intersects this Sphere
  # there is a non-zero volume of intersection
  def does_intersect_cube (self, a_cube):
    x = a_cube.center.x
    y = a_cube.center.y
    z = a_cube.center.z
    s = a_cube.side/2
    vertex = []
    vertex.append(Point(x+s, y+s, z+s))
    vertex.append(Point(x-s, y+s, z+s))
    vertex.append(Point(x+s, y+s, z-s))
    vertex.append(Point(x-s, y-s, z+s))
    vertex.append(Point(x-s, y-s, z-s))
    vertex.append(Point(x-s, y+s, z-s))
    vertex.append(Point(x-s, y-s, z-s))
    vertex.append(Point(x+s, y-s, z+s))

    for i in (vertex):
      if self.is_inside_point(i):
        return True
    dist = self.center.distance (a_cube.center)
    return (dist < (self.radius + a_cube.side))

  # return the largest Cube object that is circumscribed
  # by this Sphere
  #diaganol of cube = diameter of sphere
  def circumscribe_cube (self):
    diagonal_cube = self.radius * 2
    side = diagonal_cube/ (3**.5)
    return Cube(self.center.x, self.center.y, self.center.z, side)

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.center = Point (x, y, z)
    self.side = side

  # string representation of a Cube: Center: (x, y, z), Side: value
  def __str__ (self):
    s = "Center: " + str(self.center) + ", Side: " + str(self.side)
    return s

  # compute surface area of Cube
  def area (self):
    return 6 * (self.side**2)

  # compute volume of a Cube
  def volume (self):
    return self.side**3

  # determines if a Point is strictly inside this Cube
  # if point has coor x,y,z, x between x1 and x2 and y between y1 and y2
  def is_inside_point (self, p):
    dist = p.distance (self.center)
    return (dist < self.side)

  # determine if a Sphere is strictly inside this Cube
  def is_inside_sphere (self, a_sphere):
    #dist = self.center.distance (a_sphere.center)
    #diagonal_cube = self.side*(3**(1/2))
    #diameter_sphere = (a_sphere.radius)*2
    return(self.center.x - a_sphere.center.x < self.side/2 - a_sphere.radius) and (self.center.y - a_sphere.center.y < self.side/2 - a_sphere.radius) and (self.center.z - a_sphere.center.z < self.side/2 - a_sphere.radius)

  # determine if another Cube is strictly inside this Cube
  def is_inside_cube (self, other):
    dist = self.center.distance (other.center)
    return (self.side/2 > (dist + other.side))

  # determine if a Cylinder is strictly inside this Cube
  def is_inside_cylinder (self, a_cyl):
    diagonal_cylinder = math.sqrt(((a_cyl.radius*2)**2) + (a_cyl.height**2))
    diagonal_cube = self.side**(1/3)
    return (diagonal_cylinder < diagonal_cube)

  # determine if another Cube intersects this Cube
  # there is a non-zero volume of intersection
  def does_intersect_cube (self, other):
    dist = self.center.distance (other.center)
    return (dist < (self.side/2) + (other.side/2))

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  def intersection_volume (self, other):
    if self.is_inside_cube(other) == True:
      return str(other.side**3)
    elif self.does_intersect_cube(other) == True: 
      return ((self.side/2 + other.side/2 - abs(self.center.x - other.center.x)) * (self.side/2 + other.side/2 - abs(self.center.y - other.center.y)) * (self.side/2 + other.side/2 - abs(self.center.z - other.center.z)))
    
  # return the largest Sphere object that is inscribed
  # by this Cube
  def inscribe_sphere (self):
    radius_sphere = self.side/2
    return Sphere(self.center.x, self.center.y, self.center.z, radius_sphere)
    


class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.center = Point (x, y, z)
    self.radius = radius
    self.height = height

  # string representation of a Cylinder: Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    s = "Center: " + str(self.center) + ", Radius: " + str(self.radius) + ", Height: " + str(self.height)
    return s

  # compute surface area of Cylinder
  def area (self):
    return (2*math.pi*self.radius*self.height) + (2*math.pi*(self.radius**2))

  # compute volume of a Cylinder
  def volume (self):
    return math.pi*(self.radius ** 2)*self.height

  # determine if a Point is strictly inside this Cylinder
  def is_inside_point (self, p):
    return (abs(self.center.x - p.x) < self.radius and abs(self.center.y - p.y) < self.radius and abs(self.center.z - p.z) < self.height/2)   

  # determine if a Sphere is strictly inside this Cylinder
  def is_inside_sphere (self, a_sphere):
    return (abs(self.center.x - a_sphere.center.x) < self.radius and abs(self.center.y - a_sphere.center.y) < self.radius and abs(self.center.z - a_sphere.center.z) < self.height/2)

  # determine if a Cube is strictly inside this Cylinder
  def is_inside_cube (self, a_cube):
    diagonal_cylinder = self.radius*2 
    diagonal_cube = self.side**(1/3)
    return (diagonal_cylinder >= diagonal_cube)

  # determine if another Cylinder is strictly inside this Cylinder
  def is_inside_cylinder (self, other):
    dist = self.center.distance (other.center)
    return (self.radius > (dist + other.radius) and self.height > other.height)

  # determine if another Cylinder intersects this Cylinder
  # there is a non-zero volume of intersection
  def does_intersect_cylinder (self, other):
    return (abs(self.center.x - other.center.x) < self.radius/2 + other.radius/2 and abs(self.center.y - other.center.y) < self.radius/2 + other.radius/2 and abs(self.center.z - other.center.z) < self.height/2 + other.height/2 )

def main():
  # open file "geometry.txt" for reading
  infile = open("geometry.txt","r")             
  # read the coordinates of the first Point p
  the_line = infile.readline().split()
  x_p = float(the_line[0])
  y_p = float(the_line[1])
  z_p = float(the_line[2])

  # create a Point object and print its coordinates
  point_p = Point(x_p, y_p, z_p)

  # read the coordinates of the second Point q
  the_line = infile.readline().split()
  x_q = float(the_line[0])
  y_q = float(the_line[1])
  z_q = float(the_line[2])
  
  # create a Point object and print its coordinates
  point_q = Point(x_q, y_q, z_q)

  
  # read the coordinates of the center and radius of sphereA
  the_line = infile.readline().split()
  sphereA_x = float(the_line[0])
  sphereA_y = float(the_line[1])
  sphereA_z = float(the_line[2])
  sphereA_radius = float(the_line[3])

  # create a Sphere object and print it
  sphereA = Sphere(sphereA_x,sphereA_y,sphereA_z,sphereA_radius)

  # read the coordinates of the center and radius of sphereB
  the_line = infile.readline().split()
  sphereB_x = float(the_line[0])
  sphereB_y = float(the_line[1])
  sphereB_z = float(the_line[2])
  sphereB_radius = float(the_line[3])

  # create a Sphere object and print it
  sphereB = Sphere(sphereB_x,sphereB_y,sphereB_z,sphereB_radius)

  # read the coordinates of the center and side of cubeA
  the_line = infile.readline().split()
  cubeA_x = float(the_line[0])
  cubeA_y = float(the_line[1])
  cubeA_z = float(the_line[2])
  cubeA_side = float(the_line[3])

  # create a Cube object and print it
  cubeA = Cube(cubeA_x, cubeA_y, cubeA_z, cubeA_side)

  # read the coordinates of the center and side of cubeB
  the_line = infile.readline().split()
  cubeB_x = float(the_line[0])
  cubeB_y = float(the_line[1])
  cubeB_z = float(the_line[2])
  cubeB_side = float(the_line[3])

  # create a Cube object and print it
  cubeB = Cube(cubeB_x, cubeB_y, cubeB_z, cubeB_side)

  # read the coordinates of the center, radius and height of cylA
  the_line = infile.readline().split()
  cylA_x = float(the_line[0])
  cylA_y = float(the_line[1])
  cylA_z = float(the_line[2])
  cylA_radius = float(the_line[3])
  cylA_height = float(the_line[4])

  # create a Cylinder object and print it
  cylA = Cylinder(cylA_x,cylA_y,cylA_z,cylA_radius,cylA_height)

  # read the coordinates of the center, radius and height of cylB
  the_line = infile.readline().split()
  cylB_x = float(the_line[0])
  cylB_y = float(the_line[1])
  cylB_z = float(the_line[2])
  cylB_radius = float(the_line[3])
  cylB_height = float(the_line[4])

  # create a Cylinder object and print it
  cylB = Cylinder(cylB_x,cylB_y,cylB_z,cylB_radius,cylB_height)

  # print results
  print("Point p: " + str(point_p))
  print("Point q: " + str(point_q))
  print("sphereA: " + str(sphereA))
  print("sphereB: " + str(sphereB))
  print("cubeA: " + str(cubeA))
  print("cubeB: " + str(cubeB))
  print("cylA: " + str(cylA))
  print("cylB: " + str(cylB))
  print()

  # close file geometry.txt
  infile.close()

  # print distance between p and q
  print("Distance between P and Q: " + str(point_p.distance(point_q)))
  print()
  # print area of sphereA
  print("Area of sphereA: " + str(sphereA.area()))

  # print volume of sphereA
  print("Volume of sphereA: " + str(sphereA.volume()))

  # print if Point p is inside sphereA
  if sphereA.is_inside_point(point_p) == True:
    print ("Point p is inside sphereA")
  else:
    print ("Point p is not inside sphereA")

  # print if sphereB is inside sphereA
  if sphereA.is_inside_sphere(sphereB) == True:
    print ("sphereB is inside sphereA")
  else:
    print ("sphereB is not inside sphereA")

  # print if cubeA is inside sphereA
  if sphereA.is_cube_inside_sphere(cubeA) == True:
    print("cubeA is inside sphereA")
  else:
    print("cubeA is not inside sphereA")
  
  # print if cylA is inside sphereA
  if sphereA.is_cylinder_inside_sphere(cylA) == True:
    print("cylA is inside sphereA")
  else:
    print("cylA is not inside sphereA")

  # print if sphereA intersects with sphereB
  if sphereA.does_intersect_sphere(sphereB) == True:
    print("sphereA does intersect sphereB")
  else:
    print("sphereA does not intersect sphereB")

  # print if cubeB intersects with sphereB
  if sphereB.does_intersect_cube(cubeB) == True:
    print("cubeB does intersect sphereB")
  else:
    print("cubeB does not intersect sphereB")

  # print the largest Cube that is circumscribed by sphereA
  print("Largest Cube circumscribed by sphereA " + str(sphereA.circumscribe_cube()))
  print()

  # print area of cubeA
  print("Area of cubeA " + str(cubeA.area()))

  # print volume of cubeA
  print("Volume of cubeA " + str(cubeA.volume()))

  # print if Point p is inside cubeA
  if cubeA.is_inside_point(point_p) == True:
    print ("Point p is inside cubeA")
  else:
    print ("Point p is not inside cubeA")

  # print if sphereA is inside cubeA
  if cubeA.is_inside_sphere(sphereA) == True:
    print("sphereA is inside cubeA")
  else:
    print("sphereA is not inside cubeA")

  # print if cubeB is inside cubeA
  if cubeB.is_inside_cube(cubeA) == True:
    print("cubeB is inside cubeA")
  else:
    print("cubeB is not inside cubeA")

  # print if cylA is inside cubeA
  if cubeA.is_inside_cylinder(cylA) == True:
    print("cylA is inside cubeA")
  else:
    print("cylA is not inside cubeA")

  # print if cubeA intersects with cubeB
  if cubeA.does_intersect_cube(cubeB) == True:
    print("cubeA does intersect cubeB")
  else:
    print("cubeA does not intersect cubeB")
  
  # print the intersection volume of cubeA and cubeB
  print("Intersection volume of cubeA and cubeB: " + str(cubeA.intersection_volume(cubeB))) 

  # print the largest Sphere object inscribed by cubeA
  print("Largest Sphere inscribed by cubeA: " + str(cubeA.inscribe_sphere()))
  print()
  # print area of cylA
  print("Area of cylA: " + str(cylA.area()))

  # print volume of cylA
  print("Volume of cylA: " + str(cylA.volume()))

  # print if Point p is inside cylA
  if cylA.is_inside_point(point_p) == True:
    print("Point p is inside cylA")
  else:
    print("Point p is not inside cylA")

  # print if sphereA is inside cylA
  if cylA.is_inside_sphere(sphereA) == True:
    print("spehreA is inside cylA")
  else:
    print("spehreA is not inside cylA")

  # print if cubeA is inside cylA
  if cylA.is_inside_cube == True: 
    print("cubeA is inside cylA")
  else:
    print("cubeA is not inside cylA")

  # print if cylB is inside cylA
  if cylA.is_inside_cylinder(cylB) == True:
    print ("cylB is inside cylA")
  else:
    print ("cylB is not inside cylA")

  # print if cylB intersects with cylA
  if cylA.does_intersect_cylinder(cylB) == True:
    print("cylA does intersect cylB")
  else:
    print("cylA does not intersect cylB")

main()