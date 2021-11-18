class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    # add vertex
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    # add edge
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    #remove edge
    def remove_dege(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            # edge가 없는 2개의 vertex에 사용시 에러발생 => try/except사용
            except ValueError:
                pass
            return True
        return False

    #remode vertex
my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)

# 1 : [2, 3]
# 2 : [1, 3]
# 3 : [2, 1]

my_graph.add_edge(1,2)
my_graph.add_edge(2,3)
my_graph.add_edge(1,3)

#1 : [3]
# 2 : [3]
# 3 : [2, 1]

my_graph.remove_dege(1,2)

my_graph.print_graph()

