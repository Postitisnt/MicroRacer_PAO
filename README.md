# MicroRacer
## Overview
In this repository you will find my DRL model for the MicroRacer environment, described below and more in details inside this paper: [MicroRacer: a didactic environment for Deep Reinforcement Learning](https://arxiv.org/pdf/2203.10494.pdf).

# PAO Model
The model you find in this repository is the model that achieved the best results (placing first in the standings) in the competition between the model developed by the student of the Machine Learning course of the professor Asperti A., who have defined also some other basic models that you can find [here](https://github.com/asperti/MicroRacer), and that you can test against mine.

## Organization
You will find my model under the file `PAO.py`, while the weights I have saved from the training, and that have been used for the competition can be found in the `PAO` folder.</br>
Inside this repository, you will see also the `tracks.py` and the `lydar.pyx` files, which are used to generate the environment for both racing and training purposes (<b>PAY ATTENTION</b>: there are some problems in running the environment in M1 computers).</br>
Finally, you will find the `race.py` file, with only my model imported. This file could be useful to see how the model has to be imported, and also to see how the competitions have been organized in the final exam. You can use this file to run some models (built by you, or imported from the original repository) against mine and visually see the competition and the scoreboard, have fun!


# MicroRacer
A didactic car-racer micro environment for Deep Reinforcement Learning.
This is the README file from the [original MicroRacer repository](https://github.com/asperti/MicroRacer), and is used to explain the environment.


## Aim and motivation
MicroRacer is a simple environment inspired by car racing and especially meant for the didactics of Deep Reiforcement Learning.
The complexity of the environment has been explicitly calibrated to allow to experiment with many different methods, networks and hyperparameters settings
without the need of sophisticated software and no fear of getting bored by too long training times.

## The MicroRacer environment
MicroRacer generates new random circular tracks at each episode. The Random track is defined by CubicSplines delimiting the inner and outer border; the number of turns and the width of the track are configurable. From this description, we derive a dense matrix of points of dimension 1300x1300 providing information about positions inside the track. This is the actual definition of the track used by the environment.
![micro_racer](https://user-images.githubusercontent.com/15980090/135791705-cd678320-c189-43b5-84fe-1ceb0dd01f0d.png)

## State and actions
MicroRacer **does not** intend to model realistic car dynamics. The model is explicitly meant to be as simple as possible, with the minimal amount of complexity that still makes learning interesting and challenging.

The **state** information available to actors is composed by:
  1. a lidar-like vision of the track from the car's frontal perspective. This is an array of 19 values, expressing the distance of the car from the track's borders along uniformly spaced angles in the range -30°,+30°. 
  2. the car scalar velocity.
  
The actor (the car) has no global knowledge of the track, and no information about its absolute or relative position/direction w.r.t. the track.

The actor is supposed to answer with two actions, both in the range [-1,1]: 
  1. acceleration/deceleration
  2. turning angle
Maximum values for acceleration and turning angles can be configured. 

## Available learning models
We currently equip the code with basic actors trained with DDPG, PPO, SAC and DSAC (weights included). Students are supposed to develop their own models. 

## Requirements
The project just requires basic libraries: tensorflow, numpy, pyplotlib, scipy.interpolate (for Cubic Splines) and cython. 
A requirements file is available so you can easily install all the dependencies just using "pip install -r requirements.txt"

## Plans for future work
We are extremely interested in collaborations, especially with colleagues teaching DRL at other Universities.
We plan to organize soon a Championship.

## Race examples

Racers in the legend in order from top to bottom: DDPG, TD3, SAC, PPO.

https://user-images.githubusercontent.com/93991100/157229341-4240de02-38d6-4aca-b50d-a3b9b998d171.mp4

&nbsp;


Racers in the legend in order from top to bottom: SAC, DSAC.


https://user-images.githubusercontent.com/93991100/157229440-ceb2be76-593c-4c10-9a5e-c4e771f9fdbc.mp4



