import bpy
# from mathutils import Vector
# from utils import rotate_to_vector

# def look_at(obj, target):
#     direction = Vector(target) - obj.location
#     rot_quat = direction.to_track_quat('-Z', 'Y')
#     obj.rotation_euler = rot_quat.to_euler()

# class CameraRig:
#     def obj_rotate(self):
#         return None

class OrbitalRig:

    def __init__(self, x=0, y=0, z=0, length=1, height=1, name="OrbitalRig"):
        bpy.ops.object.empty_add(location=(x,y,z))          # create an empty object as target (i.e., the center of the rig)
        self.center = bpy.context.object
        self.center.name = name + "_center"
        self.camera = bpy.context.scene.camera
        self.camera.parent = self.center
        self.camera.location = (0, 1, height)
        self._scale = 1
        self.scale = length
        lock = self.camera.constraints.new(type='TRACK_TO')
        lock.target = self.center
        lock.track_axis = 'TRACK_NEGATIVE_Z'
        lock.up_axis = 'UP_Y'
        self.blender_object = self.center

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self.center.scale.x = value
        self.center.scale.y = value
        self.center.scale.z = value

