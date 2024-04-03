from paquete_5b.shape import Point
from paquete_5b.Isosceles import Isosceles
from paquete_5b.Equilateral import Equilateral
from paquete_5b.Scalene import Scalene
from paquete_5b.TriRectangle import TriRectangle
from paquete_5b.Square import Square


# Ahora el código principal que utiliza estas clases para calcular las propiedades de las formas geométricas
if __name__ == "__main__":
    def t_isoceles():       # Para probar triangulo isoceles
        A = Point(0,0)
        B = Point(4,0)
        C = Point(2,3)
        isosceles=Isosceles(True, [A,B,C], [], [])
        edges_isoceles = isosceles.compute_edges()
        inner_angles_isoceles = isosceles.compute_inner_angles()
        perimeter_isosceles = isosceles.compute_perimeter()
        area_isosceles = isosceles.compute_area()
        print("\nTriangulo Isoceles:")
        print("Edges: ", edges_isoceles)
        print("Inner angles: ", inner_angles_isoceles)
        print("Perimeter: ", perimeter_isosceles)
        print("Area: ", area_isosceles)

    def t_equilateral():    # Para probar triangulo equilatero
        A = Point(0,0)
        B = Point(3,0)
        C = Point(1.5,2.598)
        equilateral=Equilateral(True, [A,B,C], [], [])
        edges_equilateral = equilateral.compute_edges()
        inner_angles_equilateral = equilateral.compute_inner_angles()
        perimeter_equilateral = equilateral.compute_perimeter()
        area_equilateral = equilateral.compute_area()
        print("\nTriangulo Equilateral:")
        print("Edges: ", edges_equilateral)
        print("Inner angles: ", inner_angles_equilateral)
        print("Perimeter: ", perimeter_equilateral)
        print("Area: ", area_equilateral)

    def t_scalene():        # Para probar triangulo escaleno
        A = Point(-1,2)
        B = Point(3,0)
        C = Point(0,-3)
        scalene=Scalene(True, [A,B,C], [], [])
        edges_scalene = scalene.compute_edges()
        inner_angles_scalene = scalene.compute_inner_angles()
        perimeter_scalene = scalene.compute_perimeter()
        area_scalene = scalene.compute_area()
        print("\nTriangulo Scalene:")
        print("Edges: ", edges_scalene)
        print("Inner angles: ", inner_angles_scalene)
        print("Perimeter: ", perimeter_scalene)
        print("Area: ", area_scalene)

    def t_trirectangle():   # Para probar triangulo rectangulo
        A = Point(-1,2)
        B = Point(3,0)
        C = Point(0,-3)
        trirectangle=TriRectangle(True, [A,B,C], [], [])
        edges_rectangle = trirectangle.compute_edges()
        inner_angles_trirectangle = trirectangle.compute_inner_angles()
        perimeter_trirectangle = trirectangle.compute_perimeter()
        area_trirectangle = trirectangle.compute_area()
        print("\nTriangulo Rectangle:")
        print("Edges: ", edges_rectangle)
        print("Inner angles: ", inner_angles_trirectangle)
        print("Perimeter: ", perimeter_trirectangle)
        print("Area: ", area_trirectangle)

    def r_square():         # Para probar cuadrado
        A = Point(0,0)
        B = Point(0,4)
        C = Point(4,4)
        D = Point(4,0)
        square=Square(True, [A,B,C,D], [], [])
        edges_square = square.compute_edges()
        inner_angles_square = square.compute_inner_angles()
        perimeter_square = square.compute_perimeter()
        area_square = square.compute_area()
        print("\nRectangle Square:")
        print("Edges: ", edges_square)
        print("Inner angles: ", inner_angles_square)
        print("Perimeter: ", perimeter_square)
        print("Area: ", area_square)


    # Para mostrar resultados
    t_isoceles()
    t_equilateral()
    t_scalene()
    t_trirectangle()
    r_square()