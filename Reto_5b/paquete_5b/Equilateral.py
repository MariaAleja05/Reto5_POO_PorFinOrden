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