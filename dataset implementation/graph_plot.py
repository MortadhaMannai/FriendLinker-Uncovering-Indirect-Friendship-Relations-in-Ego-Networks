import networkx as nx
import matplotlib.pyplot as plot
import random_graph as rgraph
import snap

print "============= Plotting the Ego-Network Created ============= "
print '\n'
g = nx.Graph()  #creating an undirected graph to be plotted

for node_iterator in rgraph.variables.G1.Nodes():
    g.add_node(node_iterator.GetId(),name = rgraph.variables.h_map[node_iterator.GetId()])

for edge_iterator in rgraph.variables.G1.Edges():
    g.add_edge(edge_iterator.GetSrcNId(),edge_iterator.GetDstNId())

nx.draw(g)
plot.savefig("Ego-Network.png")
print '\n'
print "============== Plotting Completed! ================="
print '\n'
