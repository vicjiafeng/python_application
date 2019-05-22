#!/usr/bin/python
# coding:utf-8
''' mst 最小生成树 '''
'''Kruskal'''
def Kruskal(graph):
    vnum = graph.vertex_num()
    reps=[i for i in range(vnum)]
    mst, edges = [], []
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w,vi,v))
        edges.sort()
    for w,vi,vj in edges:
        if reps[vi] != reps[vj]:
            mst.append((vi,vj),w)
            if len(mst) == vnum - 1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    return mst

'''Prim'''
def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None]*vnum
    cands = PrioQueue([(0,0,0)])
    count = 0
    while count < vnum and not cands.is_empty():
        w,u,v = cands.dequeue()
        if mst[v]:
            continue
        mst[v]=((u,v),w)
        count += 1
        for vi,w in graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w,v,vi))
    return mst


                   
