GRID_SIZE = 100             # Grid will be 50x50
INITIAL_INFECTED = 3        # Start with 3 infected people
INFECTION_PROB = 0.25       # Chance of infecting a neighbor
RECOVERY_TIME = 10          # Days until recovery
MAX_DAYS = 50               # Total simulation time

# Policy toggles
USE_MASKS = False           # If True, lowers infection probability
USE_DISTANCING = False      # If True, limits contact to 4 neighbors instead of 8
