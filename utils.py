import bpy

def rotate_to_vector(obj, target_vector):
    direction = target_vector.normalized()
    rot_quat = direction.to_track_quat('Z', 'Y')
    obj.rotation_euler = rot_quat.to_euler()

def create_empty(x=0,y=0,z=0,name=None):
    bpy.ops.object.empty_add(
        type='PLAIN_AXES', 
        align='WORLD', 
        location=(x, y, z),
        scale=(1, 1, 1)
    )
    obj = bpy.context.object
    if name:
        obj.name = name
    return obj

class BlenderObject:
    def __init__(self, name):
        self.name = name
        self.obj = None
        self._material = None

    @property
    def scale(self):
        return self.obj.scale if self.obj else (1, 1, 1)

    @scale.setter
    def scale(self, value):
        if self.obj:
            if isinstance(value, (int, float)):
                self.obj.scale = (value, value, value)
            elif len(value) == 3:
                self.obj.scale = value
            else:
                raise ValueError("Scale must be a single number or a sequence of 3 numbers")

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material
        if material:
            if self.obj.data.materials:
                self.obj.data.materials[0] = material.material
            else:
                self.obj.data.materials.append(material.material)

    def delete(self):
        if self.obj:
            bpy.data.objects.remove(self.obj, do_unlink=True)
