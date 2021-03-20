import halfedge_mesh

mesh = halfedge_mesh.HalfedgeMesh("cube.off")



mesh.halfedges[10]

for v in mesh.vertices:
        print(v.halfedge.get_angle_normal())

