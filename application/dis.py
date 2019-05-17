#!/usr/bin/python
# coding:utf-8
''' dis '''
def dis_shortest_path(graph):
    vnum = graph.vertex_num()
    paths = [None]*vnum
    count = 0
    cands=PrioQueue([(0,v0,v0)])
    while count < vnum and not cands.is_empty():
        plen,u,vmin = cands.dequeue()
        if paths[vmin]:
            continue
            paths[vmin]=(u,plen)    #v0到vmin的前一个顶点是u，最短路径是plen
            for v,w in graph.out_edges(vmin):
                if not path[v]:
                    cands.enqueue((plen+w,vmin,v))
            count += 1
    return paths



                   
