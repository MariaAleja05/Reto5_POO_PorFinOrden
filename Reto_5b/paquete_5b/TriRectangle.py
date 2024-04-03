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