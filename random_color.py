from turtle import *
import random

random.seed(10)

bgcolor('black')
list = [ 'red', 'purple', 'pink',  'magenta']
hideturtle()
speed(0)
pensize(1)
n = 1
nums = [45,60,75,90]

while n<=400:
    for i in list:
        color(i)
        left(72)
        circle(n, 72)
        #left(nums[list.index(i)])
        #circle(n, 60)
        #left(int(random.random()*100))
        #circle(n, int(random.random()*100))
        n += 1
