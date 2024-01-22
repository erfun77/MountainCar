# MountainCar using gym library

This project contains the code to train an agent to solve the OpenAI Gym Mountain Car environment with Q-Learning.
## The Mountain Car Environment

[![Mountain-Car.png](https://i.postimg.cc/1Xr2DbTT/Mountain-Car.png)](https://postimg.cc/QKVf3Yjk)

The environment is two-dimensional and it consists of a car between two hills. The goal of the car is to reach a flag at the top of the hill on the right.

## Observation Space:
The are two variables that determine the current state of the environment.

The car position on the track, from -1.2 to 0.6
The car velocity, from -0.07 to 0.07. Negative for left, and positive for right.

## Actions:
The car can take one of three different actions:

Accelerate to the left
Don't accelerate
Accelerate to the right.

## Reward:
At each step, the car receives a reward based on the state it reached after that action:

Reward of 0 is awarded if the agent reached the flag (position = 0.5) on top of the mountain.
Reward of -1 is awarded if the position of the agent is less than 0.5.















[lcd]:https://hackster.imgix.net/uploads/attachments/924857/img_0510_auRlYlz8t3.JPG?auto=compress%2Cformat&w=680&h=510&fit=max
[des]:https://hackster.imgix.net/uploads/attachments/924840/screen_shot_2019-06-13_at_1_17_47_pm_XX6RqU7T6j.png?auto=compress%2Cformat&w=680&h=510&fit=max
[circuit1]:https://hackster.imgix.net/uploads/attachments/924841/lcd.jpg?auto=compress%2Cformat&w=680&h=510&fit=max
[circuit2]:https://hackster.imgix.net/uploads/attachments/924842/screen_shot_2019-06-13_at_1_18_55_pm_DhHtccXH09.png?auto=compress%2Cformat&w=680&h=510&fit=max
