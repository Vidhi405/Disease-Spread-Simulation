import numpy as np
import random
from config import *

SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2

def initialize_grid():
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    infection_days = np.zeros_like(grid)

    # Infect initial people randomly
    for _ in range(INITIAL_INFECTED):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        grid[x, y] = INFECTED
        infection_days[x, y] = 1
    return grid, infection_days

def get_neighbors(x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] if USE_DISTANCING else \
                 [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            neighbors.append((nx, ny))
    return neighbors

def step(grid, infection_days):
    new_grid = grid.copy()
    new_infection_days = infection_days.copy()
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x, y] == INFECTED:
                for nx, ny in get_neighbors(x, y):
                    if grid[nx, ny] == SUSCEPTIBLE:
                        prob = INFECTION_PROB * 0.5 if USE_MASKS else INFECTION_PROB
                        if random.random() < prob:
                            new_grid[nx, ny] = INFECTED
                            new_infection_days[nx, ny] = 1
                # Increase infection day count
                new_infection_days[x, y] += 1
                if new_infection_days[x, y] >= RECOVERY_TIME:
                    new_grid[x, y] = RECOVERED
    return new_grid, new_infection_days

def run_simulation():
    grid, infection_days = initialize_grid()
    history = []

    for day in range(MAX_DAYS):
        grid, infection_days = step(grid, infection_days)
        history.append(grid.copy())
    return history
