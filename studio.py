import bpy

# def setup_table(size=10,dz=-5):
#     bpy.ops.mesh.primitive_plane_add(size=1)
#     plane = bpy.context.object
#     plane.scale.x = size
#     plane.scale.y = size
#     plane.location.z = dz

# def setup_purewhite(table_dz=None):
#     if table_dz is not None:
#         bpy.ops.mesh.primitive_plane_add()
#         plane = bpy.context.active_object
#         plane.cycles.is_shadow_catcher = True

world = bpy.context.scene.world
world.use_nodes = True
tree = world.node_tree
tree.nodes.clear()

out = tree.nodes.new(type='ShaderNodeOutputWorld')

bg1 = tree.nodes.new(type='ShaderNodeBackground')
bg1.inputs[0].default_value = (0, 0, 0, 1)          # world color

bg2 = tree.nodes.new(type='ShaderNodeBackground')   
bg2.inputs[0].default_value = (1, 1, 1, 1)          # pure white

mix = tree.nodes.new(type='ShaderNodeMixShader')

lp1 = tree.nodes.new(type='ShaderNodeLightPath')

tree.links.new(bg1.outputs[0], mix.inputs[1])
tree.links.new(bg2.outputs[0], mix.inputs[2])

tree.links.new(lp1.outputs[0], mix.inputs[0])
tree.links.new(mix.outputs[0], out.inputs[0])