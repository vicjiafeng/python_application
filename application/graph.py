#!/usr/bin/python
# coding:utf-8
''' graph '''

class Graph:
    def __init__(self,mat,unconn=0)
    vnum = len(mat)
    for x in mat:
        if len(x) != vnum:
            raise Value Error
        self._mat=[mat[1][:] for i in range(vnum)]
        self._unconn = unconn
        seld._vnum = vnum
    def vertex_num(self):
        return self._vnum
    def _invalid(self):
        return 0 > v or v >= self._vnum
    def add_vertex(self):
        raise GraphError
    def add_edges(self,vi,vj,val=1):
        self._mat[vi][vj]=val
    def get_edges(self):
        return self._mat[vi][vj]
    def out_edges(self,vi):
        return self._out_edges(self._mat[vi],self._unconn)
    @staticmethod
    def _out_edges(row,unconn):
        edges=[]
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i,row[i]))
        return edges



                   
