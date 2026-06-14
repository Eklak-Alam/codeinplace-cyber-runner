# Cyber Runner 🏃‍♂️💨

**Cyber Runner** is a high-octane, endless 2D survival game built entirely in Python using Pygame. This project was developed as a final submission for **Stanford's Code in Place 2026**. 

The goal of the game is simple: survive as long as possible by jumping over incoming obstacles. The catch? The longer you survive, the faster the game gets. 

## 🎮 Gameplay Features
* **Progressive Difficulty:** The movement speed dynamically scales up based on the player's survival time.
* **Smooth Physics Engine:** Custom-built gravity and jump mechanics ensuring fluid 60 FPS gameplay.
* **Cinematic Parallax Background:** Continuous scrolling background for a premium visual experience.
* **Persistent High Score:** Utilizes local File I/O to save the highest score across different sessions.

## 🛠️ Core Technical Concepts (Code in Place Requirements)
This project implements several fundamental computer science concepts:
1. **File I/O:** Reading and writing to `highscore.txt` to maintain persistent state.
2. **Dictionaries:** Player state (X/Y coordinates, velocity, dimensions) is managed cleanly within a structured dictionary.
3. **Lists & Memory Management:** Obstacles are generated dynamically, appended to a list, and cleared from memory once they leave the screen to optimize performance.
4. **Control Flow & Game Loop:** An infinite `while` loop combined with event listeners and precise condition checks controls the game state (Menu vs. Active gameplay).

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/cyber-runner.git](https://github.com/yourusername/cyber-runner.git)
   cd cyber-runner
   ```

2. **Install Dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install pygame
   ```

3. **Run the Game:**
   ```bash
   python main.py
   ```

## 📂 Asset Requirements
To run the game with full visual fidelity, ensure the following asset files are present in the root directory:
* `player.png` (The main character sprite, 40x40 transparent PNG recommended)
* `obstacle.png` (The enemy/obstacle sprite, 30x40 transparent PNG recommended)
* `background.jpg` (A seamless cinematic/sci-fi background image)

*Note: The game features a fallback rendering system. If images are missing, it will automatically render standard brutalist neon geometric shapes instead.*

---
**Developed by Eklak Alam**