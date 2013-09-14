# -*- coding: utf-8 -*-

from node import Node
import random

class Graph():
	
    def __init__(self):
    	self.nodes = {}
    	pass

    def success_method(self):
    	self.test_node()    
    	self.print_graph()
        self.add_node(5)
        self.print_graph()
        # self.remove_node(10)
        # self.print_graph()
        self.connect_nodes(5,10,50)
        self.print_graph()
        self.disconnect_nodes(5,10)
        self.print_graph()
        # self.get_nodes()
        # print self.get_random_node()
        # print self.get_adj_nodes(10)
        # print self.size(10)

    def add_node(self, node_value):
        if node_value not in self.nodes:
        	node = Node(node_value)
        	self.nodes.update({node.value:node})
        else:
            print "Error adding: The node " + str(node_value) + " is already on graph."

    def remove_node(self, node_value):
    	if node_value in self.nodes:
            del self.nodes[node_value]
            for node in self.nodes.values():
                if node_value in node.adjacent_nodes:
                    node.remove_adj_node(node_value)
        else:
            print "Error removing: There is no node " + str(node_value) + " on Graph"

    def connect_nodes(self, node_value1, node_value2, weight) :
        if node_value1 in self.nodes and node_value2 in self.nodes:
            node1 = self.nodes[node_value1]
            node2 = self.nodes[node_value2]

            node1.add_adj_node(node_value2,weight)
            node2.add_adj_node(node_value1,weight)
        else:
            print "Error connecting: The two nodes must be on graph"

    def disconnect_nodes(self, node_value1, node_value2) :
        if node_value1 in self.nodes and node_value2 in self.nodes:
            node1 = self.nodes[node_value1]
            node2 = self.nodes[node_value2]

            node1.remove_adj_node(node_value2)
            node2.remove_adj_node(node_value1)
        else:
            print "Error disconnecting: The two nodes must be on graph"

    def order(self):
        return len(self.nodes)

    def get_nodes(self):
        return set(self.nodes.keys())        

    def get_random_node(self):
        return random.choice(self.nodes.keys())

    def get_adj_nodes(self, node_value):
        if node_value in self.nodes:
            node = self.nodes[node_value]
            return set(node.adjacent_nodes.keys())
        print "Error getting adjacent nodes: There is no node " + str(node_value) + " on Graph"

    def size(self, node_value):
        if node_value in self.nodes:
            node = self.nodes[node_value]
            return node.qnt_adj_nodes()
        print "Error getting size: There is no node " + str(node_value) + " on Graph"            

    def print_graph(self):
        print "Graph: \n  {"
        for node_value in self.nodes:
    		print '    ', node_value, self.nodes[node_value].adjacent_nodes
        print "  }"
        print "  order:", str(self.order()), "\n" 

    def test_node(self):
        node = Node(10)
        self.nodes.update({node.value:node})
        # self.print_graph()
        node.add_adj_node(2,3)
        # self.print_graph()
        node.add_dict_adj_nodes({6:9,7:1})
        # self.print_graph()
        node.remove_adj_node(6)
        # self.print_graph()