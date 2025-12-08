from pathlib import Path
from datetime import datetime

PATH = Path(
    "D:/programacao/python-intro/John_Hunt_advanced_guide_to_python_2019/Parte_4-Input-Output/exercicios/cap18/"
)

with open(PATH / "dia.txt", "w", newline="") as dia:
    data = str(datetime.today())
    dia.write(data)
