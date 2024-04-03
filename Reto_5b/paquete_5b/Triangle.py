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