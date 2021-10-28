 

def remove_dead_path(edges):
    # print("st")
    print(edges)
    start_nodes = []
    end_nodes = []
    
    if len(edges) > 1:
        for edge in edges:
            start_node = edge[0]
            start_nodes.append(start_node)
            end_node = edge[1]
            end_nodes.append(end_node)
        for edge in edges:
            start_node = edge[0]
            if start_node not in end_nodes:
                edges.remove(edge)
                if len(edges) > 1:
                    return remove_dead_path(edges)
                else:
                    return []
            end_node = edge[1] 
            if end_node not in start_nodes:
                edges.remove(edge)
                if len(edges) > 1:
                    return remove_dead_path(edges)
                else:
                    return []    

    return edges
 


def solution(node_num,edges):
    res = False
    edge_list = []

    if(len(edges)>3):
        for i in range(0,len(edges),2):
            edge = (edges[i],edges[i+1])
            if edge not in edge_list:
               edge_list.append(edge)
               
        if len(edge_list)>1:
           edge_list = remove_dead_path(edge_list)
    
    if len(edge_list) > 1:
        print(edge_list)
        print("circle")
            
  

  
        
solution(4,[0,1,1,2,2,3,0,3,5,0,3,4]) 
