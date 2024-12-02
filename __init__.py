from .polytope import Polytope
from .camera   import OrbitalRig
from .shapes   import Cylinder

import bpy

if "Cube" in bpy.data.objects:
    bpy.data.objects["Cube"].select_set(True)
    bpy.ops.object.delete()
