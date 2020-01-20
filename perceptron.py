import pygame as pg
import random

from percmath import *
from numpy import arange

pg.init()
win = pg.display.set_mode((640, 640))
win.fill((190, 190, 190))
# Learning Rate
lr = 0.00001
run = True

points = []
possible_numbers = []
for i in arange(float(-1.00), float(1.01), float(0.01)):
    possible_numbers.append(i)

# Class for defining points on the surface by their coordinates

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.px = int(mapping(self.x, float(1), float(-1), 640, 0))
        self.py = int(mapping(self.y, float(1), float(-1), 640, 0))
        self.lineY = f(self.x)
        if self.lineY < self.y:
            self.label = 1
        else:
            self.label = -1

    def show(self):
        if self.label == 1:
            pg.draw.circle(win, pg.Color("White"), (self.px, self.py), 10)
        else:
            pg.draw.circle(win, pg.Color("Black"), (self.px, self.py), 10)

# Creates 100 points.
for i in range(100):
    i = Point(random.choice(possible_numbers), random.choice(possible_numbers))
    points.append(i)

# Class for perceptron. Guess and train function work together
class Perceptron:
    def __init__(self):
        possible_weight = [-1,1]
        self.weights = [0,0,0]
        for i in range(len(self.weights)):
            self.weights[i] = random.choice(possible_weight)

    def guess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        output = sign(sum)
        return output
    # Train function tunes the weights based on error
    def train(self, inputs, target, guess, x, y):
        error = target - guess

        if error == 0:
            pg.draw.circle(win, pg.Color("Green"), (x, y), 6)
        else:
            pg.draw.circle(win, pg.Color("Red"), (x, y), 6)

        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * lr
    # Guess function is used to display the line being predicted
    def guessY(self, x):

        w0 = self.weights[0]
        w1 = self.weights[1]
        w2 = self.weights[2]
        return -(w2/w1) - (w0/w1) * x

# Create a perceptron object
brain = Perceptron()

# Establish endpoints for the "real" line
sx = float(-1)
sy = f(sx)
ex = float(1)
ey = f(ex)

# Create endpoints
begin_point = Point(sx, sy)
end_point = Point(ex, ey)


# Option to show endpoints
'''
begin_point.show()
end_point.show()
'''

# Main Loop
while run:
    win.fill((190, 190, 190))
    # Check for cancellation
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Draws each point, as well as lines and the correct color of guessed points
    for i in points:
        pg.draw.line(win, pg.Color("White"), (begin_point.px, begin_point.py), (end_point.px, end_point.py), 2)
        i.show()

        # Sends inputs and an attempt with its results to the train function
        inputs = [i.x, i.y, 1]
        attempt = brain.guess(inputs)
        brain.train(inputs, i.label, attempt, i.px, i.py)
        
    # Draws the predicted line.
    p3 = Point(-1, brain.guessY(-1))
    p4 = Point(1, brain.guessY(1))
    pg.draw.line(win, pg.Color("Black"), (p3.px, p3.py), (p4.px, p4.py), 2)
    pg.display.update()

