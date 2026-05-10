# BLAPPYFORD

## Demo
Demo Video: [<https://www.youtube.com/watch?v=WmepzyqVxM4>](https://www.youtube.com/watch?v=WmepzyqVxM4)

## GitHub Repository
GitHub Repo: [<https://github.com/ChonkySquirrel/blappyford>](https://github.com/ChonkySquirrel/blappyford)

## Description

Blappyford is a rendition of a Flappy Bird game with a slightly more interactive control scheme 
made as a tribute to the Flappy Bird Hour of Code that many people, including me, started their coding journeys with.

This game was largely made by adapting skills I have picked up over the course of this class and some additional Pygame
research for things that weren't talked about, such as the incorporation of Sound Effects into the game by importing some
outside sound files I made in ChipTone, a software I learned about from Animation and Games Fundamentals last semester.

As largely promised in the proposal, this game has a jump-and-gravity-based control system, with an additional horizontal dimension
that I think allows for more engaging gameplay. The score properly increments when an obstacle is cleared by the player,
and the obstacles themselves become tighter, faster, and more frequent as the the player gains even more score. When the player
does eventually die, they are shown their final score and can restart simply by jumping again.

When it came to adding my own special spice into this admittedly relatively simple game, I thought: 'well, who doesn't love
a little bit of banter and self-referential humour? So, I gave the game a little personality by making the window give you
messages each time the game is started and each time the player dies. These messages are stored in in the 'playmessages'
and 'deathmessages' txt files respectively. This game, similar to its predecessor, is meant to be something that you play
when you have little else to do with your time, so this additional banter (that can be added to or removed one as a user
pleases by editing the respective text files) gives the player an additional voice in their head to make the experience
feel a little less lonely.