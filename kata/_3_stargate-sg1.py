'''
Given a string containing the current state of the control crystals inner pathways (labeled as "X") 
and its gaps (labeled as "."), generate the shortest path from the start node (labeled as "S") 
to the goal node (labeled as "G") and return the new pathway (labeled with "P" characters).

If no solution is possible, return the string "Oh for crying out loud..." (in frustration).

.S...             .SP..
XXX..             XXXP.
.X.XX      =>     .XPXX
..X..             .PX..
G...X             G...X

'''


def wire_DHD_SG1(existing_wires):

    return "Oh for crying out loud..."


# take doc string, split on /n


'''
Dijkstra’s

XX.S.XXX..      XX.S.XXX..   
XXXX.X..XX      XXXXPX..XX
...X.XX...      ...XPXX...
XX...XXX.X      XX.P.XXX.X
....XXX...      ...PXXX...
XXXX...XXX  =>  XXXXPP.XXX
X...XX...X      X...XXP..X
X...X...XX      X...X..PXX
XXXXXXXX.X      XXXXXXXXPX
G........X      GPPPPPPP.X    
'''

'''
Represent as a graph

S = starting node
Distance from S to all other nodes = float('inf')
Distance to S = 0

Node with min value = 'current_node'

Visit all neighbouring nodes, update their distance from start

Once we visit all of the current node’s neighbors and update their distances, we mark the current node as “visited.” 
Marking a node as “visited” means that we’ve arrived at its final cost.

We go back to step one. The algorithm loops until it visits all the nodes in the graph. 
'''
ew = '''
XX.S.XXX.. 
XXXX.X..XX 
...X.XX... 
XX...XXX.X 
....XXX... 
XXXX...XXX 
X...XX...X 
X...X...XX 
XXXXXXXX.X 
G........X 
'''
ew = ew.split('\n')
ew = ew[1:]
distance = 0 

cnode = ew[0].index('S')
'''
iterate all neighbouring nodes
for each node create master list e.g [[left], [downleft], [down]]
mark each node (visited)

for each new node, visit all neighbouring nodes. If visited, ignore
e.g from [left]:
    [[left], [leftdown], [right (visited)]
new list becomes: [[left, left], [left, downleft]]
master list is now [[left, left], [left, downleft], [downleft], [down]]

repeat this until master list is no longer updated
take minimum step list with final pos G at answer
'''

cnode
nnode = 
l = ew[cnode-1]
r = ew[cnode+1]
dl = 

[i for i, x in enumerate(ew[2]) if x == '.']



