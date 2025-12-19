# Asteroids Game

A classic Asteroids arcade game implementation built with Python and Pygame.

## Description

This is a recreation of the classic Asteroids arcade game where you control a spaceship navigating through an asteroid field. Your objective is to survive by shooting and destroying asteroids while avoiding collisions.

## Features

- Classic arcade-style gameplay with vector graphics
- Smooth player controls with rotation and movement
- Dynamic asteroid splitting mechanics
- Collision detection system
- Continuous asteroid spawning from screen edges
- Event logging system for game analytics

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone this repository or download the source files
2. Install the required dependencies:

```bash
pip install pygame
```

## How to Play

Run the game with:

```bash
python main.py
```

### Controls

- **W** - Move forward
- **S** - Move backward
- **A** - Rotate left
- **D** - Rotate right
- **SPACE** - Shoot

### Gameplay

- Avoid colliding with asteroids - any collision ends the game
- Shoot asteroids to destroy them
- Large asteroids split into smaller ones when hit
- Smaller asteroids are destroyed completely
- Asteroids continuously spawn from the edges of the screen

## Project Structure

- `main.py` - Main game loop and initialization
- `player.py` - Player spaceship class with controls and shooting mechanics
- `asteroid.py` - Asteroid class with splitting behavior
- `asteroidfield.py` - Manages asteroid spawning system
- `shot.py` - Projectile class for player shots
- `circleshape.py` - Base class for circular game objects with collision detection
- `constants.py` - Game configuration and constants
- `logger.py` - Event logging system for tracking game events

## Game Constants

You can modify game behavior by editing values in `constants.py`:

- Screen dimensions (1280x720 by default)
- Player speed and rotation speed
- Asteroid spawn rate and sizes
- Shot speed and cooldown

## Technical Details

The game uses Pygame's sprite system for efficient rendering and collision detection. All moving objects inherit from the `CircleShape` base class, which provides collision detection using circle-based hitboxes.

The asteroid field continuously spawns new asteroids from random edges of the screen with randomized velocities, creating an endless gameplay experience.

## License

This project is available for educational and personal use.
