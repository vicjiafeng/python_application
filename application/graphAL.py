#!/usr/bin/python
# coding:utf-8
''' graphAL '''

class GraphAL(Graph):
    def __init__(self,mat=[],unconn=0)
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise Value Error
            self._mat=[Graph.out_edges(mat[i],unconn) for i in range(vnum)]
            self._unconn = unconn
            seld._vnum = vnum
    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1
    def add_edges(self,vi,vj,val=1):
        row = self._mat[vi]
        i=0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i]=(vj,val)
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert = (i,(vj,val))
    def get_edges(self,vi,vj):
        for i,val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn
    def out_edges(self,vi):
        return self._mat[vi]




                   
