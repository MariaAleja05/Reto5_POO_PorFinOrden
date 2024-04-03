# shape_package/shape.py
from .Rectangle import Rectangle

class Square(Rectangle):             
    def __init__(self, is_regular:bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular, vertices, edges, inner_angles)
    
    # Hereda todas las funciones de Rectangle