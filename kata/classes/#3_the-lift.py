'''
The Lift always starts on the ground floor 
    (and people waiting on the ground floor may enter immediately)

Never changes direction until there are no more people 
    wanting to get on/off in the direction it is already travelling

When empty, will continue in direction if people waiting ahead

typical route:
define lift: []
define building: ( (), (), (5,5,5), (),(), (), () )
    assign to dict:
    {0:[], 1:[], 2:[5,5,5], 3:[], 4:[], 5:[], 6:[]}

for floor,queue in dict
- check items in lift
    if match floor, remove from lift
- handle direction change (if any people want to get on/off in current direction)
- check capacity 
    if less than capacity, check direction of queue[i]
        if same direction, put queue[i] in lift 
            remove queue[i] from queue
    repeat for queue 
- check direction
- add floor to answer list if action occured (lift[before] != lift[now]) 
- progress next floor 


'''
import itertools

class Dinglemouse(object):

    def __init__(self, queues, capacity, lift, floor, direction, building):
        self.queues == queues
        self.capacity == capacity
        self.lift == lift
        self.floor == floor
        self.direction == direction
        self.building = building
        
    def _listit(self, t):
        return list(map(listit, t)) if isinstance(t, (list, tuple)) else t

    def theLift(self):
        res = []
        # convert building to dict
        self.lift = dict(zip(list(range(len(self.queues))), _listit(self.queues)))

        floor_list = list(range(len(self.lift)))
        

        for floor, queue in self.lift.items():
            checkPeople



        # list of floors stopped at, in order
        return res
    

    def checkPeople(self):
        for i in self.lift:
            if i == self.floor:
                self.floor.remove(i)
        return

    def checkDirection(self):
        # if no one wants to go current direction, check following floors for calls
        if self.direction == 'up' and max(self.lift) < self.floor:
            # count people above
            above = len(list(itertools.chain.from_iterable(
                [self.building[i] for i in self.building if i > self.floor])))
            if above == 0:
                self.direction == 'down'
                return 
        # same for down
        elif self.direction == 'down' and min(self.lift) > self.floor:
            below = len(list(itertools.chain.from_iterable(
                [self.building[i] for i in self.building if i < self.floor])))
            if below == 0:
                self.direction == 'up'
                return
        else:
            return

    def checkCapacity(self):
        if len(self.lift) == self.capacity:
            self.floor += 1
        else:
            return


    
    