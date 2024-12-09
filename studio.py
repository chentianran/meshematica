import bpy
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
        self.obj.cycles.is_shadow_catcher = True

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value
        if self.obj:
            self.obj.location.z = value

    # The delete method can be removed as it's now inherited from BlenderObject


# world = bpy.context.scene.world
# world.use_nodes = True
# tree = world.node_tree
# tree.nodes.clear()

# out = tree.nodes.new(type='ShaderNodeOutputWorld')

# bg1 = tree.nodes.new(type='ShaderNodeBackground')
# bg1.inputs[0].default_value = (0, 0, 0, 1)          # world color

# bg2 = tree.nodes.new(type='ShaderNodeBackground')   
# bg2.inputs[0].default_value = (1, 1, 1, 1)          # pure white

# mix = tree.nodes.new(type='ShaderNodeMixShader')

# lp1 = tree.nodes.new(type='ShaderNodeLightPath')

# tree.links.new(bg1.outputs[0], mix.inputs[1])
# tree.links.new(bg2.outputs[0], mix.inputs[2])

# tree.links.new(lp1.outputs[0], mix.inputs[0])
# tree.links.new(mix.outputs[0], out.inputs[0])

####
world = bpy.context.scene.world
world.use_nodes = True
tree = world.node_tree
tree.nodes.clear()

# Create Background and Output nodes
background = tree.nodes.new(type='ShaderNodeBackground')
output = tree.nodes.new(type='ShaderNodeOutputWorld')

# Set pure white color and strength
background.inputs['Color'].default_value = (1, 1, 1, 1)
background.inputs['Strength'].default_value = 1.0  # Adjust strength as needed

# Link Background to Output
tree.links.new(background.outputs['Background'], output.inputs['Surface'])
