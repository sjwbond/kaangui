from qt_core import *


def parseDate(date: str) -> QDate:
    y, m, d = date.split("-")
    return QDate(int(y), int(m), int(d))

def formatDate(date: QDate) -> str:
    return f"{date.year()}-{date.month():02}-{date.day():02}"