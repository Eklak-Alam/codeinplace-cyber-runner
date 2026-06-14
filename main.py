import pygame
import sys
import random
import os

# 1. Initialization
pygame.init()
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Runner")
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.SysFont("Arial", 22, bold=True)
title_font = pygame.font.SysFont("Arial", 50, bold=True)

# Colors
BG_COLOR = (10, 10, 15)  # Cinematic dark vibe
NEON_BLUE = (0, 255, 255)
DANGER_RED = (255, 50, 50)
TEXT_COLOR = (220, 220, 220)

# --- IMAGE LOADING SYSTEM ---
def load_image(name, size):
    try:
        # Tries to load the image and scale it to the exact size we need
        img = pygame.image.load(name).convert_alpha()
        return pygame.transform.scale(img, size)
    except:
        return None # Returns None if you haven't added the image file yet

# Load your custom assets here
player_img = load_image("player.png", (40, 40))
obstacle_img = load_image("obstacle.png", (30, 40))
bg_img = load_image("background.jpg", (WIDTH, HEIGHT))

# File I/O
high_score = 0
if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as file:
        try: high_score = int(file.read())
        except ValueError: high_score = 0

# Game Variables
game_active = False
score = 0
player = {"x": 50, "y": 300, "width": 40, "height": 40, "velocity_y": 0}
gravity = 0.6
jump_strength = -12
floor_y = 300
obstacles = []
base_speed = 6
spawn_timer = 0
bg_x = 0 # For scrolling background effect

# 2. Main Game Loop
running = True
while running:
    
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active and player["y"] >= floor_y:
                    player["velocity_y"] = jump_strength
            
            # Press ENTER to start from the Intro Screen
            if event.key == pygame.K_RETURN and not game_active:
                game_active = True
                obstacles.clear()
                score = 0
                player["y"] = floor_y
                player["velocity_y"] = 0

    if game_active:
        # --- GAME LOGIC ---
        score += 1 

        # PROGRESSIVE DIFFICULTY: Speed increases based on score
        current_speed = base_speed + (score / 300) 

        # Physics
        player["velocity_y"] += gravity
        player["y"] += player["velocity_y"]
        if player["y"] >= floor_y:
            player["y"] = floor_y
            player["velocity_y"] = 0

        # Dynamic Obstacle Spawning (Spawns faster as game speeds up)
        spawn_timer += 1
        current_spawn_rate = max(40, 80 - int(score / 100)) # Gets harder over time
        
        if spawn_timer > current_spawn_rate:
            obs_height = random.choice([30, 40, 50])
            obstacles.append({"x": WIDTH, "y": floor_y + 40 - obs_height, "width": 30, "height": obs_height})
            spawn_timer = 0

        player_rect = pygame.Rect(player["x"], player["y"], player["width"], player["height"])

        # --- RENDERING ---
        
        # 1. Cinematic Scrolling Background
        if bg_img:
            bg_x -= 2 # Move background left
            if bg_x <= -WIDTH: bg_x = 0 # Loop background
            screen.blit(bg_img, (bg_x, 0))
            screen.blit(bg_img, (bg_x + WIDTH, 0))
        else:
            screen.fill(BG_COLOR)
            pygame.draw.rect(screen, (30,30,40), (0, floor_y+40, WIDTH, HEIGHT))

        # 2. Move & Draw Obstacles
        for obs in obstacles:
            obs["x"] -= int(current_speed)
            obs_rect = pygame.Rect(obs["x"], obs["y"], obs["width"], obs["height"])
            
            if obstacle_img:
                # Scale the image dynamically if the obstacle height changes
                scaled_obs = pygame.transform.scale(obstacle_img, (obs["width"], obs["height"]))
                screen.blit(scaled_obs, (obs["x"], obs["y"]))
            else:
                pygame.draw.rect(screen, DANGER_RED, obs_rect)
            
            # Collision Detection
            if player_rect.colliderect(obs_rect):
                game_active = False
                if score > high_score:
                    high_score = score
                    with open("highscore.txt", "w") as file:
                        file.write(str(high_score))

        obstacles = [obs for obs in obstacles if obs["x"] > -50]

        # 3. Draw Real Player
        if player_img:
            screen.blit(player_img, (player["x"], player["y"]))
        else:
            pygame.draw.rect(screen, NEON_BLUE, player_rect)

        # 4. Draw UI (Showing Speed increase)
        score_surf = font.render(f"Score: {score}  |  Speed: {round(current_speed, 1)}x", True, TEXT_COLOR)
        screen.blit(score_surf, (10, 10))

    else:
        # --- INTRO / TUTORIAL SCREEN ---
        screen.fill(BG_COLOR)
        
        title = title_font.render("CYBER RUNNER", True, NEON_BLUE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 40))
        
        # Tutorial Instructions
        instructions = [
            "HOW TO PLAY:",
            "- Press SPACE to Jump",
            "- Avoid the incoming obstacles",
            "- The game gets FASTER the longer you survive!",
            "",
            f"HIGH SCORE: {high_score}",
            "",
            "> PRESS ENTER TO START <"
        ]
        
        y_pos = 120
        for text in instructions:
            # Color coding the text for a premium feel
            color = DANGER_RED if "HIGH SCORE" in text else NEON_BLUE if "ENTER" in text else TEXT_COLOR
            line = font.render(text, True, color)
            screen.blit(line, (WIDTH//2 - line.get_width()//2, y_pos))
            y_pos += 30

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()