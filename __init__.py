from .polytope import Polytope
from .camera   import OrbitalRig
from .shapes   import Cylinder
from .shapes   import Arrow
from .studio   import Table
from .materials import WhiteMaterial
from .materials import ShadowCatcherMaterial
from .materials import PolishedSteelMaterial
from .animation import begin_animation
from .animation import end_animation

import bpy

if "Cube" in bpy.data.objects:
    bpy.data.objects["Cube"].select_set(True)
    bpy.ops.object.delete()
