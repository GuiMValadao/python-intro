from datetime import datetime

opcoes = {
    "DATE": datetime.now().strftime("%d/%m/%Y"),
    "TIME": datetime.now().strftime("%H:%M:%S"),
    "DATE AND TIME": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
}

print(opcoes["DATE AND TIME"])
