# Blappyford

## Repository
https://github.com/ChonkySquirrel/blappyford

## Description
This program will create a Flappy-Bird Type Game that will have infinite sidescrolling obstacles and tap-to-hop controls.
This game will be a tribute of sorts towards the former mobile game giant.

## Features
- Sidescrolling Obstacles
	- Making obstacle objects that spawn randomly and scroll past the screen that end the game when touched. 
    Ideally, the obstacles should get more difficult at higher scores.
- Tap-To-Hop Control Scheme
	- Making a player object that can hop in response to player clicks.
- Scorekeeping & Restart Features
	- Detecting when a player has cleared an obstacle and allowing players to try again for a high score.

## Challenges
- Adding the illusion of gravity and jumping to the player object.
- Creating obstacle objects that can come in non-overlapping vertical pairs.
- Making the score reliably go up when the player object passes an obstacle pair.

## Outcomes
Ideal Outcome:
- A flappy bird-type game that can continue to play until the player hits an obstacle, and then can be restarted, 
the obstacles getting tighter and/or faster as the score gets higher. Score is counted with each obstacle cleared.

Minimal Viable Outcome:
- A flappy bird-type game that can continue to run until the player hits an obstacle. Score is counted via keeping track of time.

## Milestones

- Week 1
  1. Sidescrolling Obstacle Objects: Getting obstacles to spawn and scroll infinitely.
  2. Non-Intersecting Pairs: Getting these new obstacles to spawn in pairs that do not intersect with each other.

- Week 2
  1. Player Object Input: The player properly moves up in short 'flaps' when a click is registered.
  2. Player Object Gravity: The player object's gravity feels believable yet satisfying.

- Week N (Final)
  1. Scorekeeping: Score properly and consistently keeps track of score whenever an obstacle is cleared by the Player Object.
  2. Score Scaling: The Obstacle Object pairs get progressively tighter and the speed at which they scroll gets progressively faster in respects to the score.