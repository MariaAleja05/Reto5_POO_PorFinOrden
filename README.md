# Reto número 5 repo POO

 ### **Fecha:** 01-04-2024

**1.** Módulo único dentro del paquete

* Mirar carpeta

```
Reto_5a/
├── paquete_5a/
│   ├── __init__.py
│   └── shape.py
└── Reto_5_a.py
```

```python
# shape_package/shape.py
import math

class Point:
    definition = "Abstract geometric entity that represents a location in space."

    def __init__(self, x:float, y:float):
        self._x = x  # Coordenada x del punto
        self._y = y  # Coordenada y del punto
    
    def get_x(self):  # Getter x
        return self._x

    def set_x(self, x: float):  # Setter x
        self._x = x

    def get_y(self):  # Getter y
        return self._y

    def set_y(self, y: float):  # Setter y
        self._y = y

    def compute_distance(self, start_point, end_point):
        # Calcula la distancia entre dos puntos utilizando la fórmula de distancia euclidiana
        distance = math.sqrt((start_point.get_x() - end_point.get_x()) ** 2 + (start_point.get_y() - end_point.get_y()) ** 2)
        return distance
    
class Line:
    def __init__(self, start_point:Point, end_point:Point):
        self.start_point = start_point  # Punto inicial de la línea
        self.end_point = end_point  # Punto final de la línea
        self.length = start_point.compute_distance(start_point, end_point)  # Longitud de la línea
        
        delta_x = self.end_point.get_x() - self.start_point.get_x()
        delta_y = self.end_point.get_y() - self.start_point.get_y()
        
        if delta_x != 0: 
            self.slope = delta_y / delta_x  # Pendiente de la línea si no es vertical

class Shape:
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        self.is_regular = is_regular  # Indica si la forma es regular
        self.vertices = vertices  # Lista de puntos que forman la forma
        self.edges = edges  # Lista de longitudes de los lados
        self.inner_angles = inner_angles  # Lista de ángulos interiores

    def compute_edges(self):
        # Calcula las longitudes de los lados de la forma
        self.edges = []
        for i in range(len(self.vertices)):
            start_point = self.vertices[i]
            end_point = self.vertices[(i+1) % len(self.vertices)]  # Conecta el último punto con el primero
            line = Line(start_point, end_point)
            self.edges.append(line.length)
        return self.edges
    
    def compute_inner_angles(self):
        pass  # Método para calcular los ángulos interiores de la forma (a implementar en las subclases)

    def compute_perimeter(self):
        pass  # Método para calcular el perímetro de la forma (a implementar en las subclases)

    def compute_area(self):
        pass  # Método para calcular el área de la forma (a implementar en las subclases)

class Triangle(Shape):                
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    def compute_inner_angles(self):
        if len(self.edges) == 3:
            a, b, c = self.edges  # Lados del triángulo
            angulo_a = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
            angulo_b = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
            angulo_c = math.pi - angulo_a - angulo_b  # Ángulo restante
            self.inner_angles = [math.degrees(angulo_a), math.degrees(angulo_b), math.degrees(angulo_c)]
        return self.inner_angles

    def compute_perimeter(self):
        if len(self.edges) == 3:
            self.perimeter = sum(self.edges)  # Suma de los lados del triángulo
        return self.perimeter

    def compute_area(self):
        pass  # Método para calcular el área del triángulo (a implementar)

class Rectangle(Shape):                  
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)

    def compute_inner_angles(self):
        if len(self.edges) == 4:
            self.inner_angles = [90, 90, 90, 90]  # Ángulos interiores de un rectángulo
        return self.inner_angles
    
    def compute_perimeter(self):
        if len(self.edges) == 4:
            self.perimeter = sum(self.edges)  # Suma de los lados del rectángulo
        return self.perimeter

    def compute_area(self):
        if len(self.edges) == 4:
            base = max(self.edges)  # Lado más largo (base)
            altura = min(self.edges)  # Lado más corto (altura)
            self.area = base * altura  # Área del rectángulo
        return self.area

class Square(Rectangle):             
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # Hereda todas las funciones de Rectangle
    
class Isosceles(Triangle):              # Hereda de Triangle
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # La función compute_inner_angles se hereda y funciona
    # La función compute_perimeter se hereda y funciona
    
    def compute_area(self):
        if len(self.edges) == 3:
            # Calcula el área de un triángulo isósceles utilizando la fórmula de altura
            altura = math.sqrt((self.edges[0])**2 - ((self.edges[1])**2/4))
            self.area = 0.5 * self.edges[1] * altura
        return self.area

class Equilateral(Triangle):              # Hereda de Triangle
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # La función compute_inner_angles se hereda y funciona
    # La función compute_perimeter se hereda y funciona
    
    def compute_area(self):
        if len(self.edges) == 3:
            # Calcula el área de un triángulo equilátero utilizando la fórmula específica
            area = (math.sqrt(3) / 4) * (self.edges[0] ** 2)
        return area

class Scalene(Triangle):
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # La función compute_inner_angles se hereda y funciona
    # La función compute_perimeter se hereda y funciona
    
    def compute_area(self):
        if len(self.edges) == 3:
            semiperimeter = sum(self.edges) / 2  # Semiperímetro del triángulo
            # Calcula el área de un triángulo escaleno utilizando la fórmula de Herón
            area = math.sqrt(semiperimeter * (semiperimeter - self.edges[0]) * 
                             (semiperimeter - self.edges[1]) * (semiperimeter - self.edges[2]))
        return area

class TriRectangle(Triangle):
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # La función compute_inner_angles se hereda y funciona
    # La función compute_perimeter se hereda y funciona
    
    def compute_area(self):
        if len(self.edges) == 3:
            base = self.edges[0]  # El lado que se toma como base del rectángulo
            altura = self.edges[1]  # La altura del rectángulo
            self.area = 0.5 * base * altura  # Fórmula del área de un rectángulo
        return self.area
```

```python
from paquete_5a.shape import Point
from paquete_5a.shape import Isosceles
from paquete_5a.shape import Equilateral
from paquete_5a.shape import Scalene
from paquete_5a.shape import TriRectangle
from paquete_5a.shape import Square


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
```

**2.** Modulos individuales

* Mirar carpeta

```
Reto_5b/
├── paquete_5b/
│   ├── __init__.py
│   ├── Equilateral.py
│   ├── Isosceles.py
│   ├── Rectangle.py
│   ├── Scalene.py
│   ├── shape.py
│   ├── Square.py
│   ├── Triangle.py
│   └── TriRectangle.py
└── Reto_5_b.py
```


```python
# shape_package/shape.py
import math

from .Triangle import Triangle

class Equilateral(Triangle):              # Hereda de Triangle
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # La función compute_inner_angles se hereda y funciona
    # La función compute_perimeter se hereda y funciona
    
    def compute_area(self):
        if len(self.edges) == 3:
            # Calcula el área de un triángulo equilátero utilizando la fórmula específica
            area = (math.sqrt(3) / 4) * (self.edges[0] ** 2)
        return area
```

```python
# shape_package/shape.py
import math

from .Triangle import Triangle
    
class Isosceles(Triangle):              # Hereda de Triangle
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # La función compute_inner_angles se hereda y funciona
    # La función compute_perimeter se hereda y funciona
    
    def compute_area(self):
        if len(self.edges) == 3:
            # Calcula el área de un triángulo isósceles utilizando la fórmula de altura
            altura = math.sqrt((self.edges[0])**2 - ((self.edges[1])**2/4))
            self.area = 0.5 * self.edges[1] * altura
        return self.area
```

```python
# shape_package/shape.py
from .shape import Shape

class Rectangle(Shape):                  
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)

    def compute_inner_angles(self):
        if len(self.edges) == 4:
            self.inner_angles = [90, 90, 90, 90]  # Ángulos interiores de un rectángulo
        return self.inner_angles
    
    def compute_perimeter(self):
        if len(self.edges) == 4:
            self.perimeter = sum(self.edges)  # Suma de los lados del rectángulo
        return self.perimeter

    def compute_area(self):
        if len(self.edges) == 4:
            base = max(self.edges)  # Lado más largo (base)
            altura = min(self.edges)  # Lado más corto (altura)
            self.area = base * altura  # Área del rectángulo
        return self.area
```

```python
# shape_package/shape.py
import math

from .Triangle import Triangle

class Scalene(Triangle):
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # La función compute_inner_angles se hereda y funciona
    # La función compute_perimeter se hereda y funciona
    
    def compute_area(self):
        if len(self.edges) == 3:
            semiperimeter = sum(self.edges) / 2  # Semiperímetro del triángulo
            # Calcula el área de un triángulo escaleno utilizando la fórmula de Herón
            area = math.sqrt(semiperimeter * (semiperimeter - self.edges[0]) * 
                             (semiperimeter - self.edges[1]) * (semiperimeter - self.edges[2]))
        return area
```

```python
# shape_package/shape.py
import math

class Point:
    definition = "Abstract geometric entity that represents a location in space."

    def __init__(self, x:float, y:float):
        self._x = x  # Coordenada x del punto
        self._y = y  # Coordenada y del punto
    
    def get_x(self):  # Getter x
        return self._x

    def set_x(self, x: float):  # Setter x
        self._x = x

    def get_y(self):  # Getter y
        return self._y

    def set_y(self, y: float):  # Setter y
        self._y = y

    def compute_distance(self, start_point, end_point):
        # Calcula la distancia entre dos puntos utilizando la fórmula de distancia euclidiana
        distance = math.sqrt((start_point.get_x() - end_point.get_x()) ** 2 + (start_point.get_y() - end_point.get_y()) ** 2)
        return distance
    
class Line:
    def __init__(self, start_point:Point, end_point:Point):
        self.start_point = start_point  # Punto inicial de la línea
        self.end_point = end_point  # Punto final de la línea
        self.length = start_point.compute_distance(start_point, end_point)  # Longitud de la línea
        
        delta_x = self.end_point.get_x() - self.start_point.get_x()
        delta_y = self.end_point.get_y() - self.start_point.get_y()
        
        if delta_x != 0: 
            self.slope = delta_y / delta_x  # Pendiente de la línea si no es vertical

class Shape:
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        self.is_regular = is_regular  # Indica si la forma es regular
        self.vertices = vertices  # Lista de puntos que forman la forma
        self.edges = edges  # Lista de longitudes de los lados
        self.inner_angles = inner_angles  # Lista de ángulos interiores

    def compute_edges(self):
        # Calcula las longitudes de los lados de la forma
        self.edges = []
        for i in range(len(self.vertices)):
            start_point = self.vertices[i]
            end_point = self.vertices[(i+1) % len(self.vertices)]  # Conecta el último punto con el primero
            line = Line(start_point, end_point)
            self.edges.append(line.length)
        return self.edges
    
    def compute_inner_angles(self):
        pass  # Método para calcular los ángulos interiores de la forma (a implementar en las subclases)

    def compute_perimeter(self):
        pass  # Método para calcular el perímetro de la forma (a implementar en las subclases)

    def compute_area(self):
        pass  # Método para calcular el área de la forma (a implementar en las subclases)
```

```python
# shape_package/shape.py
from .Rectangle import Rectangle

class Square(Rectangle):             
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # Hereda todas las funciones de Rectangle
```

```python
# shape_package/shape.py
import math

from .shape import Shape

class Triangle(Shape):                
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    def compute_inner_angles(self):
        if len(self.edges) == 3:
            a, b, c = self.edges  # Lados del triángulo
            angulo_a = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
            angulo_b = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
            angulo_c = math.pi - angulo_a - angulo_b  # Ángulo restante
            self.inner_angles = [math.degrees(angulo_a), math.degrees(angulo_b), math.degrees(angulo_c)]
        return self.inner_angles

    def compute_perimeter(self):
        if len(self.edges) == 3:
            self.perimeter = sum(self.edges)  # Suma de los lados del triángulo
        return self.perimeter

    def compute_area(self):
        pass  # Método para calcular el área del triángulo (a implementar)
```

```python
# shape_package/shape.py
import math

from .Triangle import Triangle

class TriRectangle(Triangle):
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # La función compute_inner_angles se hereda y funciona
    # La función compute_perimeter se hereda y funciona
    
    def compute_area(self):
        if len(self.edges) == 3:
            base = self.edges[0]  # El lado que se toma como base del rectángulo
            altura = self.edges[1]  # La altura del rectángulo
            self.area = 0.5 * base * altura  # Fórmula del área de un rectángulo
        return self.area
```

```python
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
```
