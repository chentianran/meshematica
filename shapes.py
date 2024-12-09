import bpy
from mathutils import Vector
from .utils import rotate_to_vector
from .utils import BlenderObject

class Cylinder(BlenderObject):
    def __init__(self, x=0, y=0, z=0, radius=1, height=1, name='cylinder'):
        super().__init__(name)
        self._radius = radius
        self._height = height
        self.create_cylinder(x, y, z)

    def create_cylinder(self, x, y, z):
        bpy.ops.mesh.primitive_cylinder_add(
            radius=self._radius,
            depth=self._height,
            location=(x, y, z),
            rotation=(0, 0, 0)
        )
        self.obj = bpy.context.object
        self.obj.name = self.name

    @property
    def height(self):
        return self._height

    @property
    def radius(self):
        return self._radius

    def delete(self):
        super().delete()



class Arrow(BlenderObject):
    def __init__(self, start_point, end_point, thickness=0.1, head_diameter=0.5, head_length=0.3, name='arrow'):
        super().__init__(name)
        self.start_point = Vector(start_point)
        self.end_point = Vector(end_point)
        self._thickness = thickness
        self._head_diameter = head_diameter
        self._head_length = head_length

        self.create_arrow()

    def create_arrow(self):
        vector = self.end_point - self.start_point
        length = vector.length
        direction = vector.normalized()
        shaft_length = length - self._head_length

        # Create shaft
        bpy.ops.mesh.primitive_cylinder_add(
            location=self.start_point + direction * shaft_length * 0.5,
            depth=shaft_length,
            radius=self._thickness * 0.5
        )
        self.shaft = bpy.context.object
        rotate_to_vector(self.shaft, vector)

        # Create head
        bpy.ops.mesh.primitive_cone_add(
            location=self.end_point - direction * self._head_length * 0.5,
            depth=self._head_length,
            radius1=self._head_diameter * 0.5,
            radius2=0
        )
        self.head = bpy.context.object
        rotate_to_vector(self.head, vector)

        # Create empty as parent
        bpy.ops.object.empty_add(location=self.start_point)
        self.obj = bpy.context.object
        self.obj.name = self.name
        self.shaft.parent = self.obj
        self.head.parent = self.obj

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material
        for part in [self.shaft, self.head]:
            if part.data.materials:
                part.data.materials[0] = material
            else:
                part.data.materials.append(material)

    def delete(self):
        bpy.data.objects.remove(self.shaft, do_unlink=True)
        bpy.data.objects.remove(self.head, do_unlink=True)
        super().delete()