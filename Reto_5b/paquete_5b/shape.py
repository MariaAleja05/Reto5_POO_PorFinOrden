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