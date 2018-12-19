nodes = list('abcdefghij')
links = 'ab ac ad ea ef eb eg ec ed fa fb fg fc fd bc bd ga gb gc gd ha hd ia id ja jd dc'.split()
mtx = [[0 for x in nodes] for y in nodes]

for i in links:
    lnk = list(i)
    mtx[nodes.index(lnk[0])][nodes.index(lnk[1])] = 1
    mtx[nodes.index(lnk[1])][nodes.index(lnk[0])] = 1

def get_loops(idx, path = [], cycles = []):
    row = mtx[idx]
    path.append(idx)
    #print path, "=>", np.where(row)[0]
    for i in [j for j, x in enumerate(row) if x]:
        #print idx, "->", i
        if i not in path:
            get_loops(i, path[:], cycles)
        else:
            if path[0] == i and len(path) > 2:
                cyc = path[:] + [i]
                edges = [sorted([cyc[j], cyc[j+1]]) for j in range(len(cyc)-1)]
                loop = sorted(edges)
                if not loop in cycles:
                    cycles.append(loop)
                    print [map(lambda j: nodes[j].capitalize(), e) for e in edges]

get_loops(nodes.index('d'))
