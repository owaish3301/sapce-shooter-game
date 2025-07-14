# Space Shooter Game

A simple space shooter game built with Python and Pygame.

## Description

Control a spaceship and shoot down incoming meteors to survive and score points. The game features smooth movement controls, laser shooting with cooldown, and collision detection.

## Requirements

- Python 3.6+
- Pygame

## Installation

1. Clone this repository:
```bash
git clone https://github.com/owaish3301/sapce-shooter-game.git
cd SpaceShooter
```

2. Install Pygame:
```bash
pip install pygame-ce
```

## How to Run

```bash
python main.py
```

## Controls

- **Movement**: Arrow keys or WASD
- **Shoot**: Spacebar
- **Quit**: Close window or Alt+F4

## Game Features

- Player movement with boundary collision
- Laser shooting with cooldown system
- Meteor spawning and collision detection
- Real-time score tracking
- Optimized rendering for better performance

## File Structure

```
SpaceShooter/
├── main.py          # Main game loop and initialization
├── Player.py        # Player class with movement and shooting
├── Laser.py         # Laser projectile class
├── Meteor.py        # Meteor enemy class
├── Images/          # Game assets
│   ├── shooter.png  # Player sprite
│   ├── astroid.png  # Meteor sprite
│   └── laser.png    # Laser sprite
└── README.md        # This file
```

## Screenshots

*Add screenshots of your game here*

## License

This project is open source and available under the [MIT License](LICENSE).
