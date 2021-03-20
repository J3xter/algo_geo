import halfedge_mesh
from halfedge_mesh.halfedge_mesh import distance

mesh = halfedge_mesh.HalfedgeMesh("cube.off")


#def dijkstra(mesh, s):
    # création d'une liste distance
    #d = [ None for v in mesh.vertices ]
    # le premier point est à zéro
    #d[s.index] = 0
    # les précédesseurs ne sont pas encore connus
    #pred = [ None for v in mesh.vertices]

    #openVerts = [ [d.index, d[s.index]] ]

    #while len(openVerts) != 0:
        # prendre le point v le plus proche dans openVerts
        # TODO

        # on parcours ses voisins
        # si ce voisin n'est pas fermé
        # alors on calcule la distance à la source
        # pour ce voisin en passant par le point v
        # on met à jour d, pred, et on ajoute à openVerts ce
        # nouvel élément
        # TODO



# v: sommet
v = mesh.vertices[0]
h = v.halfedge
first = True
print("on part du point " + str(v.index))
 
# parcours tous les voisins de v
while first or h != v.halfedge:
   first = False
   v2 = h.opposite.vertex
   print(v2.index)

   h = h.next_around_vertex()