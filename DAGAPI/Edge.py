#!/usr/bin/env python
# -*-coding:utf-8 -*-
#RoBinZ @ chtc.wisc.edu
#06.27 2017
#The Edge class, The directed edges connect different nodes.
class Edge(object):
    #define a Edge class, a edge must have parent and child
    def __init__(self,parents, children):
        '''

        :param parents: a list of the **Node.name** of parents nodes,['A','B']
        :param children: a list of the **Node.name** of children nodes,['A']
        '''
        self.parents = parents
        self.children = children

