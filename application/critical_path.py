#!/usr/bin/python
# coding:utf-8
''' critical_path '''
def critical_path(graph):
    def event_earliest_time(vnum,graph,toposeq):
        ee = [0]*vnum                #ee——最早可能时间
            for i in toposeq:
                for j,w in graph.out_edges(i):
                    if ee[i]+w > ee[j]:     #事件j更晚结束
                        ee[j] = ee[i] + w
        return ee
    def event_latest_time(vnum,graph,toposeq,eelast):
        le = [eelast]*vnum                   #le——最晚可能时间
            for k in range(vnum-2,-1,-1):        #逆拓扑顺序
                i = toposeq[k]
                for j,w in graph.out_edges(i):
                    if le[j]-w<le[i]:          #事件i更早开始
                        le[i]=le[j]-w
        return le
    def crt_paths(vnum,graph,ee,le):
        crt_actions=[]
        for i in range(vnum):
            for j,w in graph.out_edges(i):
                if ee[i] == le[j] - w:            #关键活动--关键路径
                    crt_actions.append((i,j,ee[i]))
        return crt_actions
    toposeq = toposort(graph)
    if not toposeq:
        return False
    vnum = graph.vertex_num()
    ee = event_earliest_time(vnum,graph,toposeq)
    le = event_latest_time(vnum,graph,toposeq,ee[vnum-1])
    return crt_paths(vnum,graph,ee,le)

                   
