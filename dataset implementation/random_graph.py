import snap
import names
from tqdm import tqdm
import variables
# creating an instance of an undirected graph
variables.vertices = int(raw_input("Enter number of Nodes in the Ego-Network ==> "))
variables.edges = int(raw_input("Enter number of Edges in the Ego-Network ==> "))

variables.G1 = snap.GenRndGnm(snap.PUNGraph, variables.vertices, variables.edges)

variables.h_map = snap.TIntStrH()

print "Generating Random Ego Network........"
print '\n'
for node_iterator in tqdm(variables.G1.Nodes(),ascii = False,desc = "Ego-Network Setup Progress ===> "):
    random_name = names.get_full_name()
    index = node_iterator.GetId()
    variables.h_map[index] = random_name
    print "node = %d name = %s" % (index,variables.h_map[index])

print '\n'
print "====================================="
print '\n'
print "====================================="
print '\n'

for node_iterator in variables.G1.Nodes() :
    index = node_iterator.GetId()
    print "node =  %d   name = %s" % (index,variables.h_map[index])
    for edge_iterator in node_iterator.GetOutEdges() :
        print " ----> %s" % (variables.h_map[edge_iterator])
print '\n'
print "Random Ego Network Generated!"
print '\n'
