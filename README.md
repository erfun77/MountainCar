# MountainCar using gym library

This project contains the code to train an agent to solve the OpenAI Gym Mountain Car environment with Q-Learning.
## The Mountain Car Environment

[![Mountain-Car.png](https://i.postimg.cc/1Xr2DbTT/Mountain-Car.png)](https://postimg.cc/QKVf3Yjk)

The environment is two-dimensional and it consists of a car between two hills. The goal of the car is to reach a flag at the top of the hill on the right.

## Observation Space:
There are two variables that determine the current state of the environment:

- The car position on the track, from -1.2 to 0.6
- The car velocity, from -0.07 to 0.07. 

## Actions:
There are 3 discrete deterministic actions:

- 0: Accelerate to the left
- 1: Don't accelerate
- 2: Accelerate to the right

## Reward:

The goal is to reach the flag placed on top of the right hill as quickly as possible, as such the agent is penalised with a reward of -1 for each timestep.

## Q-Learning

Run the following line to render a pre-trained agent with Q-learning:
```
python3 car.py
```
The agent was trained for 3500 episodes. Its Q-values are saved in the file 'mountain_car.pkl'.

 hyperparameters:
- learning rate (alpha) = 0.1
- discount factor (gamma) = 0.95


## Reference
OpenAI MountainCar-v0 retrieved from https://gymnasium.farama.org/environments/classic_control/mountain_car/#mountain-car
