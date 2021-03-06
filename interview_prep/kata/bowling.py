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



class bowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        ridx = 0
        for frame in range(10):
            if self.isStrike(ridx) == True:
                # 10 + next 2 rolls
                score += self.strikeScore[ridx]
                ridx += 1
            elif self.isSpare(ridx) == True:
                # 10 + next roll
                score += self.spareScore[ridx]
                ridx += 2
            else:
                score += self.normalScore[ridx]
                ridx += 2
        return score

    def isStrike(self, ridx):
        return self.rolls[ridx] == 10 
    
    def isSpare(self, ridx):
        return self.rolls[ridx] + self.rolls[ridx + 1] == 10

    def strikeScore(self, ridx):
        return 10 + self.rolls[ridx + 1] + self.rolls[ridx + 2]

    def spareScore(self, ridx):
        return 10 + self.rolls[ridx + 2]

    def normalScore(self, ridx):
        return self.rolls[ridx] + self.rolls[ridx + 1]



# score_str = 'X X X' # 30
# score_str = 'X X 4' # 24
# score_str = 'X -2' # 12
# score_str = 'X 4/' # 20

