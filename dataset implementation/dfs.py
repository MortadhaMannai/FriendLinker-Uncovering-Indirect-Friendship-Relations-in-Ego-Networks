import graph_plot
# import random_graph as rgraph
import variables
import snap

stack = [ ]
vertex_id = 0
temp_count = 1

def search_node(vertex_id):
    flag = 0
    final_node = 0
    for node_iterator in variables.G1.Nodes():
        if (node_iterator.GetId() == vertex_id):
            flag = 1
            final_node = node_iterator
            break

    if flag == 1:
        return final_node
    else :
        return 0

def depth_first_search(vertex_id,vertex_id2,count) :
    print '\n'
    print variables.h_map[vertex_id]

    if stack == []:
        stack.append(variables.h_map[vertex_id])

    my_node = search_node(vertex_id)
    print "Currently Ego ==> %s" %(variables.h_map[my_node.GetId()])
    if my_node != 0:
        for edge_iterator in my_node.GetOutEdges():
            if (not (variables.h_map[edge_iterator] in stack)):
                print "Alters -----> %s at depth == %d" %(variables.h_map[edge_iterator],count)
                if variables.h_map[edge_iterator] == variables.h_map[vertex_id2] :
                    print '\n' + "%s is an indirect connection of %s" %(variables.h_map[vertex_id],variables.h_map[vertex_id2])
                    return
                stack.append(variables.h_map[edge_iterator])

                global temp_count
                temp_count = temp_count + 1
                depth_first_search(edge_iterator,vertex_id2,count+1)


if __name__ == "__main__":
    # limit = int(raw_input("Enter the limit for the Depth Limit Search Algorithm ==> "))
    while(1) :
        vertex_id = int(raw_input("Enter Initial Vertex Id (0 <= id <= %d ) ==>" %(variables.vertices - 1)))
        vertex_id2 = int(raw_input("Enter Search Vertex Id (0 <= id <= %d ) ==>" %(variables.vertices - 1)))
        if not( vertex_id in range(0,variables.vertices)):
            print '\n'
            print "Error: vertex-id outside boundary conditions"
            print '\n'
            exit()


        depth_first_search(vertex_id,vertex_id2,0)
        print "count of nodes visited = %d" %(temp_count)

        print '\n','\n'
