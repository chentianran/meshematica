import bpy
import os
from .shapes import BlenderObject

class Table(BlenderObject):
    def __init__(self, size=10, z=-5, name='table'):
        super().__init__(name)
        self.size = size
        self._z = z
        self.create_table()

    def create_table(self):
        bpy.ops.mesh.primitive_plane_add(size=self.size)
        self.obj = bpy.context.object
        self.obj.name = self.name
        self.obj.location.z = self._z
        self.obj.cycles.is_shadow_catcher = True    # old setting, may not be needed for Blender 2.8+
        self.obj.is_shadow_catcher = True           # the new approach

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value
        if self.obj:
            self.obj.location.z = value

    # The delete method can be removed as it's now inherited from BlenderObject

world = bpy.context.scene.world
world.use_nodes = True
tree = world.node_tree
tree.nodes.clear()

# Create nodes
background = tree.nodes.new(type='ShaderNodeBackground')
environment_texture = tree.nodes.new(type='ShaderNodeTexEnvironment')
mix = tree.nodes.new(type='ShaderNodeMixShader')
lightpath = tree.nodes.new(type='ShaderNodeLightPath')
output = tree.nodes.new(type='ShaderNodeOutputWorld')

current_dir = os.path.dirname(os.path.abspath(__file__))
hdri_path = os.path.join(current_dir, "hdri", "sunflowers_puresky_4k.exr")

# Load HDRI image
# Replace this path with the actual path to your HDRI file
environment_texture.image = bpy.data.images.load(hdri_path, check_existing=True)

# Configure nodes
background.inputs['Color'].default_value = (1, 1, 1, 1)  # Pure white background
background.inputs['Strength'].default_value = 1.0

environment_texture.image.colorspace_settings.name = 'Linear Rec.709'  # Set proper color space

lightpath.location = (-300, 200)
environment_texture.location = (-300, 0)
background.location = (-300, -200)
mix.location = (0, 0)
output.location = (300, 0)

# Connect nodes
tree.links.new(lightpath.outputs['Is Camera Ray'], mix.inputs[0])
tree.links.new(environment_texture.outputs['Color'], mix.inputs[1])  # HDRI for reflections
tree.links.new(background.outputs[0], mix.inputs[2])  # White background visible to camera

tree.links.new(mix.outputs[0], output.inputs['Surface'])

scene = bpy.context.scene
scene.view_settings.view_transform = 'Standard'
scene.view_settings.look = 'None'
scene.display_settings.display_device = 'sRGB'
