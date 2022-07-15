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
        self.elevator = []
        self.people_waiting = True

    def theLift(self):

        res = [0]

        while self.people_waiting:
            self.people_waiting = False

            res = self._run_lift(res, 'up')
            res = self._run_lift(res, 'down')

        if res[-1] != 0:
            res.append(0)

        return res

    def _run_lift(self, stops, direction):
        f_order = range(len(self.queues) -1, -1, -1) if direction == 'down' else range(0, len(self.queues))
        for floor in f_order:
            exits = self._people_exit(floor)
            enters = self._people_enter(floor, direction)
            if exits or enters and not stops[-1] == floor:
                stops.append(floor)
        return stops

    def _people_exit(self, floor):
        stop = False

        for person in self.elevator[:]:
            if person == floor:
                self.elevator.remove(person)
                stop = True

        return stop

    def _people_enter(self, floor, direction):
        stop = False

        for person in self.queues[floor][:]:
            person_enters = person < floor if direction == 'down' else person > floor

            if person_enters:
                stop = True

                if self.capacity > len(self.elevator):
                    self.elevator.append(person)
                    self.queues[floor].remove(person)
                else:
                    self.people_waiting = True

        return stop
