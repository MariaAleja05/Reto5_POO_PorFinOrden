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