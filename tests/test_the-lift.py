import pytest
from kata.classes._3_the_lift import Dinglemouse

testdata = [
         (( (),(),(5,5,5),(),(),(),()), [0, 2, 5, 0]),
         (( (),(),(1,1),(),(),(),()), [0, 2, 1, 0]),
         (( (),(3,),(4,),(),(5,),(),()),[0, 1, 2, 3, 4, 5, 0]),
         (( (),(0,),(),(),(2,),(3,),()), [0, 5, 4, 3, 2, 1, 0])
            ]

  
@pytest.mark.parametrize(('queues', 'expected_result'), testdata)
def test_lift(queues, expected_result):
    lift = Dinglemouse(queues, 5)
    assert lift.theLift() == expected_result



