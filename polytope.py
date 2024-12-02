import bpy
import math
from mathutils import Vector

class Polytope:
    pts: list
    name: str = 'polytope'

    def __init__(self, vertices, name='polytope'):
        if isinstance(vertices, list):
            self.pts = vertices
        else:
            self.pts = list(vertices)
        
        self.name = name

        mesh = bpy.data.meshes.new(name=name + '_mesh')
        obj  = bpy.data.objects.new(name, mesh)

        bpy.context.collection.objects.link(obj)

        mesh.from_pydata(self.pts, [], [])
        mesh.update()

        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        bpy.ops.object.mode_set(mode='EDIT')

        bpy.ops.mesh.convex_hull()
        bpy.ops.object.mode_set(mode='OBJECT')

        self.obj = obj

    # def create_edges(self, edges, radius=0.02, name=None, material=None):
    #     if not name:
    #         name = self.name + '_edges'
        
    #     for e in edges:
    #         point1, point2 = self.pts[e[0]], self.pts[e[1]]
    #         vec_start = Vector(point1)
    #         vec_end = Vector(point2)
    #         vec_dir = vec_end - vec_start

    #         midpoint = (vec_start + vec_end) / 2
    #         length = vec_dir.length

    #         vec_dir.normalize()

    #         rot_quat = vec_dir.to_track_quat('Z', 'Y')
    #         eul = rot_quat.to_euler()
    #         # angle = math.acos(vec_dir.dot(Vector((0,0,1))))

    #         bpy.ops.mesh.primitive_cylinder_add(
    #             radius=radius, 
    #             depth=length,
    #             location=midpoint, 
    #             rotation=eul)

    #         obj = bpy.context.object
    #         if name:
    #             obj.name = name
    #         if material:
    #             obj.data.materials.append(material)
