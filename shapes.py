import bpy
from mathutils import Vector

class Cylinder:
    def __init__(self, x=0, y=0, z=0, radius=1, height=1, name='cylinder'):
        self.name = name
        bpy.ops.mesh.primitive_cylinder_add(
            radius=1,
            depth=1,
            location=(x, y, z),
            rotation=(0, 0, 0)
        )

        self.obj = bpy.context.object
        self.obj.name = self.name
        self._height = 1
        self._radius = 1
        self.height = height
        self.radius = radius

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self.obj.scale.z = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.obj.scale.x = value
        self.obj.scale.y = value
    # def set_material(self, material):
    #     if self.obj.data.materials:
    #         self.obj.data.materials[0] = material
    #     else:
    #         self.obj.data.materials.append(material)

    # def delete(self):
    #     bpy.data.objects.remove(self.obj, do_unlink=True)