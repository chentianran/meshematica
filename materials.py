import bpy

class WhiteMaterial:

    def __init__(self):
        self.material = bpy.data.materials.new(name="PureWhite")
        self.material.use_nodes = True
        nodes = self.material.node_tree.nodes
        nodes.clear()
        principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        principled.inputs['Base Color'].default_value = (1, 1, 1, 1)
        material_output = nodes.new(type='ShaderNodeOutputMaterial')
        links = self.material.node_tree.links
        links.new(principled.outputs['BSDF'], material_output.inputs['Surface'])

class PolishedSteelMaterial:
    def __init__(self):
        self.material = bpy.data.materials.new(name="PolishedSteel")
        self.material.use_nodes = True
        nodes = self.material.node_tree.nodes
        nodes.clear()

        principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        principled.inputs['Base Color'].default_value = (0.5, 0.5, 0.5, 1)
        principled.inputs['Metallic'].default_value = 1.0
        principled.inputs['Roughness'].default_value = 0.1

        material_output = nodes.new(type='ShaderNodeOutputMaterial')
        
        links = self.material.node_tree.links
        links.new(principled.outputs['BSDF'], material_output.inputs['Surface'])