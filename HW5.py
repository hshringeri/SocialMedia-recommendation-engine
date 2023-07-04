import random
import sys
import argparse

parser = argparse.ArgumentParser()

z = 1
def convert_matrix_to_list(filename):
    list = []
    f = open(filename, 'r')
    for line in f.readlines():
        line_list = line.split(" ")
        line_list[len(line_list) - 1] = line_list[len(line_list) - 1][0:1]
        list.append(line_list)

    list = list[1:]

    return list

def create_neighbors_dict(list):
    neighbors_dict = {}
    for i in range(0, len(list)):
        neighbors = []
        for j in range(0, len(list[i])):
            if list[i][j] == '1':
                neighbors.append(j)
        neighbors_dict[i] = neighbors

    return neighbors_dict



def pageRank(N, S, E):
    node_count = {}
    og_N = N
    visit(N, og_N, S, E, node_count)
    return node_count

def visit(N, og_N, S, E, node_count):
    global z
    z = z + 1
    if N in node_count:
        node_count[N] += 1/S
    else:
        node_count[N] = 1/S
    curr_node_neighbors = neighbors_dict[N]
    split = E * 100
    a = random.randint(1, 100)
    if z < S:
        if a <= split:
            visit(og_N, og_N, S, E, node_count)
        else:
            if len(curr_node_neighbors) > 0:
                rand_idx = random.randrange(len(curr_node_neighbors))
                random_num = curr_node_neighbors[rand_idx]
                visit(random_num, og_N, S, E, node_count)
            else:
                visit(og_N, og_N, S, E, node_count)



def output(N,S,E):
    list = convert_matrix_to_list('adj_matrix.txt')
    neighbors_dict = create_neighbors_dict(list)
    node_count = pageRank(N,S,E)
    node_count = dict(sorted(node_count.items(), key=lambda item: item[1], reverse=True))
    with open("output.txt", "w") as f:
        count = 0
        for key in node_count:
            count = count + 1
            if count <= 10:
                if key == N:
                    f.write(str(key) + ', ' + str(node_count[key]) + ', ' + 'Node N\n')
                    print(str(key) + ', ' + str(node_count[key]) + ', ' + 'Node N\n')
                elif key in neighbors_dict[N]:
                    f.write(str(key) + ', ' + str(node_count[key]) + ', ' + 'current friend\n')
                    print(str(key) + ', ' + str(node_count[key]) + ', ' + 'current friend\n')
                else:
                    f.write(str(key) + ', ' + str(node_count[key]) + ', ' + 'potential friend\n')
                    print(str(key) + ', ' + str(node_count[key]) + ', ' + 'potential friend\n')







parser.add_argument("-a", "--adj_matrix_file")
parser.add_argument("-N", "--N", type=int)
parser.add_argument("-S", "--S", type=int)
parser.add_argument("-E", "--E", type=float)

args = parser.parse_args()
a_file = args.adj_matrix_file
N = args.N
S = args.S
E = args.E
sys.setrecursionlimit(2000)
adj_list = convert_matrix_to_list(a_file)
neighbors_dict = create_neighbors_dict(adj_list)
output(N, S, E)

