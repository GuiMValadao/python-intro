import dialogues

from config import KEY_SIGNATURES
from entities import MovingBlock, NPCGeneric


# TODO: implement dialogues after it's written; test the npcs; add new NPCs
class TownNPC(NPCGeneric):
    """Beginner opponent — no interference, just plays the song straight."""

    pass  # inherits do-nothing defaults


class DistractingBusker(NPCGeneric):
    """Periodically spawns a fake block on a random lane to confuse the player."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._distract_timer = 0

    def on_battle_update(self, battle_event):
        self._distract_timer += 1
        if self._distract_timer >= 120:  # every 2 seconds
            self._distract_timer = 0
            self._spawn_decoy(battle_event)

    def _spawn_decoy(self, battle_event):
        import random

        button = random.choice(battle_event.staff.buttons)
        decoy = MovingBlock(battle_event.game, button, note_key=None)
        decoy.is_decoy = True  # BattleEvent skips scoring for decoys
        battle_event.moving_blocks.append(decoy)


class PressureMusician(NPCGeneric):
    """Speeds up block movement when the player hits notes successfully."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._speed_multiplier = 1.0

    def on_player_hit(self, battle_event):
        self._speed_multiplier = min(2.0, self._speed_multiplier + 0.05)
        for block in battle_event.moving_blocks:
            block.speed = 3 * self._speed_multiplier

    def on_player_miss(self, battle_event):
        self._speed_multiplier = max(1.0, self._speed_multiplier - 0.1)


class KeyChangeBoss(NPCGeneric):
    """Forces sudden key changes when the player misses, adding disorientation."""

    def on_player_miss(self, battle_event):
        import random

        new_key = random.choice(list(KEY_SIGNATURES.keys()))
        battle_event._trigger_key_change(new_key)
