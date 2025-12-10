from pathlib import Path
import io

ROOT_PATH = Path(__file__).parent

with io.FileIO(ROOT_PATH / "Stream_text.txt", "wb") as f:
    binary_writer = io.BufferedWriter(f)
    print(binary_writer.write(b"Algum texto de exemplo para se escrever em binario."))
    binary_writer.flush()
