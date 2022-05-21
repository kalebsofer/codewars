'''
Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling, 
produces the total score for the game.

The input is a valid sequence of rolls
The output is the resulting score
Example input
For instance, for a game that is partway through, your input might be:

“X 45 4/ 32”

This indicates that:

Four frames have been played
The first frame was a “strike” (all 10 pins knocked over in one roll - symbolised by “X”)
The second frame (“45”) consisted of the maximum two rolls
The first roll knocked down 4 pins
The second roll knocked down 5 pins
The third frame was a “spare” (all 10 pins knocked down in two rolls - symbolised by “/” on the second roll)
The first roll knocked down 4 pins
The second roll knocked down the remaining 6 pins
The fourth frame (“32”) consisted of two rolls
The first roll knocked down 3 pins
The second roll knocked down 2 pins
Example output
For the above input of “X 45 4/ 32”, the score would be 46 - scored as follows:

The first frame is a strike, which scores 10 + (all rolls from the following frame) = 10 + 4 + 5 = 19
The second frame scores 4 + 5 = 9
The third frame is a spare, which scores 10 + (the first roll from the following frame) = 10 + 3 = 13
The fourth frame scores 3 + 2 = 5
For detailed scoring rules, see below.

What your solution will not do
Here are some things that the program will not do:

We will not check for valid rolls.
We will not check for correct number of rolls and frames.
We will not provide scores for intermediate frames.
Depending on the application, this might or might not be a valid way to define a complete story, 
but we do it here for purposes of keeping the kata light. 
I think you’ll see that improvements like those above would go in readily if they were needed for real.

Summarised scoring
We can briefly summarize the scoring for this form of bowling:

Each game, or “line” of bowling, includes ten turns, or “frames” for the bowler.

In each frame, the bowler gets up to two tries to knock down all the pins.
If in two tries, the bowler fails to knock them all down, their score for that frame is the total number of pins knocked down in their two tries.
If “spare”, score for the frame is ten plus the number of pins knocked down on their next throw (in their next turn).
If “strike”, their score for the frame is ten plus the simple total of the pins knocked down in their next two rolls.
If spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. 
    These bonus throws are taken as part of the same turn.  
    If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
    The game score is the total of all frame scores.
'''

def gene2(x):
    return x + 2
    

class game:
    def __init__(self) -> None:
        self.rolls = []
    
    def roll(pins: int) :  
        # called each time roll occurs
        pass
 
    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
            else:
                result += self.frameScore(rollIndex )
            rollIndex += 2
        return result

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
    
    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]
    
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
 
# game has 10 frames
# frame has 1 or 2 rolls
# 10th frame has 2 or 3 rolls



# bowl('X 45 4/ 32')
# 19 + 9 + 13 + 5
# 46

# bowl('X X X X X X X X X X X X')
# 300 

# bowl('9- 9- 9- 9- 9- 9- 9- 9- 9- 9-')
# 90

# bowl('5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5')
# 150
        

class bowlingGame:
    def __init__(self) -> None:
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        return 


    


# score_str = 'X X X' # 30
# score_str = 'X X 4' # 24
# score_str = 'X -2' # 12
# score_str = 'X 4/' # 20

