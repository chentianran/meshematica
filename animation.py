import bpy
from math import pi

class Shot:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.obj = None
        self.data_path = None

    def _begin_action(self,obj=None):
        if not obj:
            obj = self.obj
        if isinstance(obj,list):
            for elem in obj:
                self._begin_action(elem)
        else:
            obj.keyframe_insert(data_path=self.data_path, frame=self.start)

    def _end_action(self,obj=None):
        if not obj:
            obj = self.obj
        if isinstance(obj,list):
            for elem in obj:
                self._end_action(elem)
        else:
            obj.keyframe_insert(data_path=self.data_path, frame=self.end)

    def do_nothing(self):
        return None

    def move(self, obj):
        self.obj = obj
        self.data_path = "location"
        return self

    def rotate(self, obj):
        if hasattr(obj, "blender_object"):
            self.obj = obj.blender_object
        else:
            self.obj = obj
        self.data_path = "rotation_euler"
        return self

    def scale(self, obj):
        if hasattr(obj, "blender_object"):
            self.obj = obj.blender_object
        else:
            self.obj = obj
        self.data_path = "scale"
        return self

    def transluscentize(self, obj):
        self.obj = obj
        self.data_path = "material_slots[0].material.transparency"
        return self
    
    def from_current_position(self):
        self._begin_action()
        return self

    def from_point(self, x, y, z):
        self.obj.location.x = x
        self.obj.location.y = y
        self.obj.location.z = z
        self._begin_action()
        return self

    def to_point(self, x, y, z):
        self.obj.location.x = x
        self.obj.location.y = y
        self.obj.location.z = z
        self._end_action()
        return self

    def via_function(self, func):
        _do_move_by_function(self.obj, func)
        self._end_action()
        return self

    def with_center(self, center):
        bpy.ops.object.empty_add(location=center)
        empty = bpy.context.object
        self.obj.parent = empty
        self.obj = empty
        return self

    def about_z(self, angle):
        self._begin_action()
        self.obj.rotation_euler.x = 0
        self.obj.rotation_euler.y = 0
        self.obj.rotation_euler.z = pi * (angle / 180)
        self._end_action()
        return self
    
    def from_factor(self, factor):
        _do_scale(self.obj, factor)
        # self.obj.scale.x = factor
        # self.obj.scale.y = factor
        # self.obj.scale.z = factor
        self._begin_action()
        return self

    def from_xfactor(self, factor):
        _do_scale(self.obj, factor, key=0)
        self._begin_action()
        return self

    def from_yfactor(self, factor):
        _do_scale(self.obj, factor, key=1)
        self._begin_action()
        return self

    def from_zfactor(self, factor):
        _do_scale(self.obj, factor, key=2)
        self._begin_action()
        return self

    def to_factor(self, factor):
        _do_scale(self.obj, factor)
        # self.obj.scale.x = factor
        # self.obj.scale.y = factor
        # self.obj.scale.z = factor
        self._end_action()
        return self

    def to_xfactor(self, factor):
        _do_scale(self.obj, factor, key=0)
        self._end_action()
        return self
    
    def to_yfactor(self, factor):
        _do_scale(self.obj, factor, key=1)
        self._end_action()
        return self
    
    def to_zfactor(self, factor):
        _do_scale(self.obj, factor, key=2)
        self._end_action()
        return self

    def to_uniform_factor(self, factor):
        self._begin_action()
        self.obj.scale.x = factor
        self.obj.scale.y = factor
        self.obj.scale.z = factor
        self._end_action()
        return self

def _do_scale(obj, factor, key=None):
    if isinstance(obj, list):
        for elem in obj:
            _do_scale(elem, factor, key)
        return
    if hasattr(obj, "blender_object"):
        obj = obj.blender_object
    if key:
        obj.scale[key] = factor
    else:
        obj.scale.x = factor
        obj.scale.y = factor
        obj.scale.z = factor

def _do_move_by_function(obj, func):
    if isinstance(obj, list):
        for elem in obj:
            _do_move_by_function(elem, func)
        return
    if hasattr(obj, "blender_object"):
        obj = obj.blender_object
    x = obj.location.x
    y = obj.location.y
    z = obj.location.z
    obj.location = func(x,y,z)
    

def begin_animation(duration):
    fps = bpy.context.scene.render.fps
    frames = int(duration * fps)
    if not hasattr(begin_animation, "current_frame"):
        begin_animation.current_frame = 1
    shot = Shot(begin_animation.current_frame, begin_animation.current_frame + frames)
    begin_animation.current_frame += frames
    return shot

def end_animation():
    bpy.context.scene.frame_end = begin_animation.current_frame - 1
    return bpy.context.scene.frame_end