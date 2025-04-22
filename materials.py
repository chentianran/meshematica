import bpy

class WhiteMaterial:

    def __init__(self):
        self.material = bpy.data.materials.new(name="PureWhite")
        self.material.use_nodes = True
        nodes = self.material.node_tree.nodes
        nodes.clear()
        principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        principled.inputs['Base Color'].default_value = (1, 1, 1, 1)
        principled.inputs['Specular IOR Level'].default_value = 0.0  # Reduce specular highlights
        principled.inputs['Roughness'].default_value = 1.0  # Make it completely matte
        material_output = nodes.new(type='ShaderNodeOutputMaterial')
        links = self.material.node_tree.links
        links.new(principled.outputs['BSDF'], material_output.inputs['Surface'])

class ShadowCatcherMaterial:
    def __init__(self):
        self.material = bpy.data.materials.new(name="ShadowCatcher")
        self.material.use_nodes = True
        # This is the key line - it makes the object only show shadows
        # self.material.shadow_method = 'CLIP'  # Or you can use
        # self.material.use_shadow_catcher = True
        self.material.blend_method = 'BLEND'
        # Enable shadow catching for Cycles
        self.material.cycles.is_shadow_catcher = True

        # The node setup is less important when using shadow catcher,
        # but you can keep it simple:
        # nodes = self.material.node_tree.nodes
        # nodes.clear()

        # principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        # principled.inputs['Base Color'].default_value = (1, 1, 1, 1)
        # principled.inputs['Roughness'].default_value = 1.0

        # material_output = nodes.new(type='ShaderNodeOutputMaterial')
        # links = self.material.node_tree.links
        # links.new(principled.outputs['BSDF'], material_output.inputs['Surface'])

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
