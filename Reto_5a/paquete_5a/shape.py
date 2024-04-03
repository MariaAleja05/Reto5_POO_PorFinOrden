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