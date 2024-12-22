import bpy

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 64

bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 720
bpy.context.scene.render.resolution_percentage = 50

bpy.context.scene.render.fps = 30