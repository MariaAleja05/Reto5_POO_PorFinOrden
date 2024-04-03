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