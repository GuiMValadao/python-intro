import config
import json
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    # Write saves next to the .exe
    _exe_dir = Path(sys.executable).parent
    SAVE_DIR = _exe_dir / "saves"
else:
    SAVE_DIR = config.ROOT_PATH / "saves"

SLOT_COUNT = 3


def _slot_path(slot: int) -> Path:
    return SAVE_DIR / f"slot_{slot}.json"


def _default_save() -> dict:
    """Fresh save data with current config defaults."""
    return {
        "difficulty": config.DIFFICULTY,
        "key_bindings": {
            note: config.NOTES_TO_KEYS[note]
            for note in ("A", "B", "C", "D", "E", "F", "G")
        },
        "songs_played": 0,
        "high_scores": {key: 0 for key in __import__("songs").SONGS},
    }


def list_saves() -> list[dict | None]:
    """
    Return a list of length SLOT_COUNT.
    Each entry is the save dict if the slot exists, or None if empty.
    """
    SAVE_DIR.mkdir(exist_ok=True)
    result = []
    for i in range(SLOT_COUNT):
        path = _slot_path(i)
        if path.exists():
            try:
                with open(path) as f:
                    result.append(json.load(f))
            except (json.JSONDecodeError, OSError):
                result.append(None)  # treat corrupt file as empty
        else:
            result.append(None)
    return result


def load_save(slot: int, game) -> None:
    """
    Load slot data into config and game state.
    Calls _rebuild_note_maps and _rebuild_note_sounds to keep everything in sync.
    """
    SAVE_DIR.mkdir(exist_ok=True)
    path = _slot_path(slot)

    if path.exists():
        try:
            with open(path) as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            data = _default_save()
    else:
        data = _default_save()
        _write_slot(
            slot, data
        )  # create the file immediately so the slot appears filled

    # Apply difficulty
    config.DIFFICULTY = data.get("difficulty", config.DIFFICULTY)

    # Apply key bindings
    bindings = data.get("key_bindings", {})
    for note, key_const in bindings.items():
        if note in config.NOTES_TO_KEYS:
            config.NOTES_TO_KEYS[note] = key_const
    config._rebuild_note_maps()
    game._rebuild_note_sounds()

    # Store high scores and songs played on the game object
    game.high_scores = data.get("high_scores", {})
    game.songs_played = data.get("songs_played", 0)
    game.current_slot = slot


def write_save(slot: int, game) -> None:
    """Write current game state to the given slot."""
    SAVE_DIR.mkdir(exist_ok=True)
    data = {
        "difficulty": config.DIFFICULTY,
        "key_bindings": {
            note: config.NOTES_TO_KEYS[note]
            for note in ("A", "B", "C", "D", "E", "F", "G")
        },
        "songs_played": game.songs_played,
        "high_scores": game.high_scores,
    }
    _write_slot(slot, data)


def _write_slot(slot: int, data: dict) -> None:
    SAVE_DIR.mkdir(exist_ok=True)
    with open(_slot_path(slot), "w") as f:
        json.dump(data, f, indent=2)


def delete_slot(slot: int) -> None:
    """Remove a save slot file if it exists."""
    path = _slot_path(slot)
    if path.exists():
        path.unlink()
