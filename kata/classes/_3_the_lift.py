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


class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = [list(x) for x in queues]
        self.capacity = capacity
        self.lift = []
        self.people_waiting = True

    def _personLeaves(self, floor, stop=False):
        for person in self.lift:
                    if person == floor:
                        self.lift.remove(person)
                        stop = True
        return stop

    def _handleQueue(self, person, floor, stop=True):
        if self.capacity > len(self.lift):
            self.lift.append(person)
            self.queues[floor].remove(person)
        else:
            self.people_waiting = True
        return stop

    def _appendResult(self, stop, res, floor):
        if stop and not res[-1] == floor:
            res.append(floor)


    def _goUp(self, res):
        for floor in range(0, len(self.queues)):
                stop = self._personLeaves(floor, stop=False)
                for person in self.queues[floor]:
                    if person > floor:
                        stop = self._handleQueue(person, floor, stop=True)
                self._appendResult(stop, res, floor)
        return
    
    def _goDown(self, res):
        for floor in range(len(self.queues) -1, -1, -1):
                stop = self._personLeaves(floor, stop=False)
                for person in self.queues[floor]:
                    if person < floor:
                        stop = self._handleQueue(person, floor, stop=True)
                self._appendResult(stop, res, floor)
        return


    def theLift(self):
        res = [0]
        
        while self.people_waiting:
            self.people_waiting = False
            self._goUp(res)
            self._goDown(res)
            
        if res[-1] != 0:
            res.append(0)

        return res
    

