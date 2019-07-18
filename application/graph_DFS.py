#!/usr/bin/python
# coding:utf-8
'''  graph-DFS '''

def DFS_graph(graph,v0):
    vnum = graph.vertex_num()
    visited = [0]*vnum
    visited[v0] = 1
    DFS_seq = [v0]
    st = SStack()
    st.push((0,graph.out_edge(v0)))
    while not st.is_empty():
        i,edges = st.pop()
        if i < len(vnum):
            v,e = edges[i]
            st.push((i+1,edges))
            if not visited[v]:
                DFS-seq.append(v)
                visited[v]=1
                st.push((0,graph.out_edges(v)))
    return DFS_seq



                   
