import pygame
import config

from chars import TownNPC


class Camera:
    def __init__(self, map_width, map_height):
        self.offset = pygame.Vector2(0, 0)
        self.map_width = map_width
        self.map_height = map_height

    def follow(self, target):
        """Center the camera on the target, clamped to map bounds."""
        self.offset.x = target.position.x - config.DISPLAY_WIDTH // 2
        self.offset.y = target.position.y - config.DISPLAY_HEIGHT // 2

        # Clamp so we never render outside the map
        self.offset.x = max(
            0, min(self.offset.x, self.map_width - config.DISPLAY_WIDTH)
        )
        self.offset.y = max(
            0, min(self.offset.y, self.map_height - config.DISPLAY_HEIGHT)
        )

    def apply(self, position):
        """Convert a world position to a screen position."""
        return position - self.offset


class Map:
    def __init__(
        self,
        name,
        background_path,
        width,
        height,
        spawn_point,
        npcs=None,
        transitions=None,
    ):
        self.name = name
        self.width = width
        self.height = height
        self.spawn_point = spawn_point  # Vector2 — where the player starts
        self.npcs = npcs or []
        self.transitions = transitions or {}
        # {"map_key": trigger_rect} e.g. {"market": pygame.Rect(2500, 300, 60, 200)}

        background = pygame.image.load(background_path).convert()
        self.background = pygame.transform.scale(background, (width, height))

    def draw(self, display_surface, camera):
        """Draw the visible portion of the map background."""
        # Source rect — the slice of the background that's currently visible
        source_rect = pygame.Rect(
            camera.offset.x,
            camera.offset.y,
            config.DISPLAY_WIDTH,
            config.DISPLAY_HEIGHT,
        )
        display_surface.blit(self.background, (0, 0), source_rect)

    def draw_npcs(self, display_surface, camera):
        for npc in self.npcs:
            screen_pos = camera.apply(npc.position)
            display_surface.blit(npc.image, screen_pos)


def load_maps():

    return {
        "town_square": Map(
            name="Town Square",
            background_path=config.ROOT_PATH / "images/maps/background1.png",
            width=2560,
            height=1440,
            spawn_point=pygame.Vector2(400, 300),
            # Verify how apply this, do I create the instance here or just call the instance created elsewhere?
            npcs=[
                #    TownNPC(...),
            ],
        ),
        "market": Map(
            name="Market",
            background_path=config.ROOT_PATH / "images/maps/market.png",
            width=3840,
            height=720,  # wide and narrow — a street
            spawn_point=pygame.Vector2(100, 360),
        ),
    }
