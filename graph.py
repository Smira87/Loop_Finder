import numpy as np

def permutations_in_dict(string, words):
    target = sorted(string)
    return sorted(word for word in words if sorted(word) == target)

nodes = list('abcdefghij')
links = 'ab ac ad ea ef eb eg ec ed fa fb fg fc fd bc bd ga gb gc gd ha hd ia id ja jd dc'.split()
mtx = np.zeros((len(nodes),len(nodes)), np.int32)

for i in links:  
    lnk = list(i)
    mtx[nodes.index(lnk[0]), nodes.index(lnk[1])] = 1
mtx += mtx.T
cycles = []

def get_loops(idx, path = []):
    row = mtx[idx]
    path.append(idx)
    #print path, "=>", np.where(row)[0]
    for i in np.where(row)[0]:
        #print idx, "->", i
        if i not in path:
            get_loops(i, path[:])
        else:
            if path[0] == i and len(path) > 2:
                if not permutations_in_dict(path, cycles):
                    cycles.append(path)
                    print [nodes[n].capitalize() for n in path]

get_loops(3)