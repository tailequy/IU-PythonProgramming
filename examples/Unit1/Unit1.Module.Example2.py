'''
Packages in Python are used to hierarchically organize module namespace. These packages
are declared using the dot notation or from-import statement at the top of the module
code.
'''
import math_packages.math_library
def main():
    result = math_packages.math_library.area_of_circle(2)
    print("The area of the circle is: {}".format(result))
if __name__ == '__main__':
    main()