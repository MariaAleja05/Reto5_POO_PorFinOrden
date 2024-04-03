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