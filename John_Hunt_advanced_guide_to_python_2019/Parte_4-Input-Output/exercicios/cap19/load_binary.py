from pathlib import Path
import io

ROOT_PATH = Path(__file__).parent

with io.FileIO(ROOT_PATH / "Stream_text.txt", "r") as f:
    binary_reader = io.BufferedReader(f)
    print(binary_reader.read())
