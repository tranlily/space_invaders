import random


class Settings():
    # Main class for game settings

    def __init__(self):
        # Static settings.
        # Screen settings.
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (17, 17, 17)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 253,231,236
        self.bullets_allowed = 10

        # Alien settings.
        self.fleet_drop_speed = 10
        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5


        self.last_ufo = None
        self.ufo_min_interval = 10000

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 20
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 2
        self.ufo_speed_factor = 5

        # Scoring.
        self.alien_points = 100
        self.ufo_points = random.randint(1,101)

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
        self.ufo_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
