import bpy
from math import sqrt


scale = 1
subdiv = 5
name = 'Icosomething'


middle_point_cache = {}


def vertex(x, y, z):

    length = sqrt(x**2 + y**2 + z**2)

    return [(i * scale) / length for i in (x,y,z)]


def middle_point(point_1, point_2):

    smaller_index = min(point_1, point_2)
    greater_index = max(point_1, point_2)

    key = '{0}-{1}'.format(smaller_index, greater_index)

    if key in middle_point_cache:
        return middle_point_cache[key]

    vert_1 = verts[point_1]
    vert_2 = verts[point_2]
    middle = [sum(i)/2 for i in zip(vert_1, vert_2)]

    verts.append(vertex(*middle))

    index = len(verts) - 1
    middle_point_cache[key] = index

    return index

PHI = (1 + sqrt(5)) / 2

verts = [
          vertex(-1,  PHI, 0),
          vertex( 1,  PHI, 0),
          vertex(-1, -PHI, 0),
          vertex( 1, -PHI, 0),

          vertex(0, -1, PHI),
          vertex(0,  1, PHI),
          vertex(0, -1, -PHI),
          vertex(0,  1, -PHI),

          vertex( PHI, 0, -1),
          vertex( PHI, 0,  1),
          vertex(-PHI, 0, -1),
          vertex(-PHI, 0,  1),
        ]


faces = [
         # 5 faces around point 0
         [0, 11, 5],
         [0, 5, 1],
         [0, 1, 7],
         [0, 7, 10],
         [0, 10, 11],

         # Adjacent faces
         [1, 5, 9],
         [5, 11, 4],
         [11, 10, 2],
         [10, 7, 6],
         [7, 1, 8],

         # 5 faces around 3
         [3, 9, 4],
         [3, 4, 2],
         [3, 2, 6],
         [3, 6, 8],
         [3, 8, 9],

         # Adjacent faces
         [4, 9, 5],
         [2, 4, 11],
         [6, 2, 10],
         [8, 6, 7],
         [9, 8, 1],
        ]

mesh = bpy.data.meshes.new(name)
mesh.from_pydata(verts, [], faces)

obj = bpy.data.objects.new(name, mesh)
bpy.context.scene.collection.objects.link(obj)
