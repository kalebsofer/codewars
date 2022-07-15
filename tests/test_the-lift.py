import pytest
from kata.classes._3_the_lift import Dinglemouse

testdata = [
         (( (),(),(5,5,5),(),(),(),()), 5, [0, 2, 5, 0]),
         (( (),(),(1,1),(),(),(),()), 5, [0, 2, 1, 0]),
         (( (),(3,),(4,),(),(5,),(),()), 5, [0, 1, 2, 3, 4, 5, 0]),
         (( (),(0,),(),(),(2,),(3,),()), 5, [0, 5, 4, 3, 2, 1, 0]),
         (( (),(),(4,4,4,4),(),(2,2,2,2),(),()), 2, [0, 2, 4, 2, 4, 2, 0]) # [0, 2, 4, 2, 0]
            ]

  
@pytest.mark.parametrize(('queues', 'capacity', 'expected_result'), testdata)
def test_lift(queues, capacity, expected_result):
    lift = Dinglemouse(queues, capacity)
    assert lift.theLift() == expected_result



