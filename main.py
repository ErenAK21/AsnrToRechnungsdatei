import pandas
import os


def getBemerkung(file):
    parts = file.split("_")
    frist = parts[1]

    if frist == "NS":
        return ["IS 200 Nachschau ausführen", "Nachschau ausführen"]


def getFrznr(file):
    parts = file.split("_")
    return parts[0]


def getWerk(file):
    parts = file.split("_")
    return parts[-2]


def addLine(werk, fahrzeug, bemerkung):
    print(1)

    # get the Date



frist = r"\Br 1.1"

for file in os.listdir(
        r"C:\Users\eaksu\OneDrive - National Express Rail GmbH\Desktop\Ort Kluth Arbeitsscheine2" + frist):

    werk = getWerk(file)
    fahrzeug = getFrznr(file)
    bemerkung = getBemerkung(file)

    print(f"{werk} {fahrzeug}")

    if not werk == "Düsseldorf" or not werk == "Münster":
        continue
