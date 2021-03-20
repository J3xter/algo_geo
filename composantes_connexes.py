import halfedge_mesh

def dfs(graph, node):
    visited = [node]
    stack = [node]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.extend(node)
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited

def composantes_connexes(mesh):
    drapeau = [ 0 for v in mesh.vertices ]
    composantes = 0
    for v in mesh.vertices:
        if drapeau[v.index] == 0:
            drapeau[v.index] = 1
            



