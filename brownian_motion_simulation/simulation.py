import pygame
import numpy as np
from .models import Arena, Robot

# Constants
WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOR = (255, 255, 255)
ROBOT_COLOR = (0, 0, 255)
ROBOT_SIZE = 6
SPEED = 2
TOTAL_TIME = 2
TIME_STEP = 0.01
ROTATION_VARIANCE = 0.5


# Simulation functions
def simulate_brownian_motion(robot, arena, total_time, time_step, rotation_variance):
    positions = []
    for _ in range(int(total_time / time_step)):
        robot.update_position(time_step)
        positions.append((robot.x, robot.y))

        if not arena.contains(robot):
            robot.direction += np.random.normal(0, rotation_variance)

    return positions

def update(robot, arena):
    positions = simulate_brownian_motion(robot, arena, TOTAL_TIME, TIME_STEP, ROTATION_VARIANCE)
    return positions[-1]

def run_simmulation():
    use_custom_values = input("Use custom values (yes/no)? ").lower()

    if use_custom_values == 'yes':
        while True:
            print("-"*100)
            print("Default Values: TOTAL_TIME = 2, TIME_STEP = 0.01, ROTATION_VARIANCE = 0.5")
            print("-"*100)
            try:
                TOTAL_TIME = float(input("Enter the total simulation time: "))
                TIME_STEP = float(input("Enter the time step: "))
                ROTATION_VARIANCE = float(input("Enter the rotation variance: "))
                if TOTAL_TIME > 0 and TIME_STEP > 0 and ROTATION_VARIANCE > 0:
                    break
                else:
                    print("Invalid input. Values must be positive.")
            except ValueError:
                print("Invalid input. Please enter numerical values.")
    else:
        TOTAL_TIME = 2
        TIME_STEP = 0.01
        ROTATION_VARIANCE = 0.5

    # run pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brownian Motion Simulation")
    clock = pygame.time.Clock()

    arena = Arena(WIDTH, HEIGHT)
    robot = Robot(WIDTH // 2, HEIGHT // 2, 0, SPEED)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # constanly updating posi
        x, y = update(robot, arena)

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, 'black', (0, 0, WIDTH+2, HEIGHT+2), 2)
        pygame.draw.circle(screen, ROBOT_COLOR, (int(x), int(y)), ROBOT_SIZE)

        pygame.display.flip()
        clock.tick(1 / TIME_STEP)

    pygame.quit()