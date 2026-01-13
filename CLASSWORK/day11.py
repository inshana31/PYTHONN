import tripdate as t
from datetime import datetime
import json


details = [
    t("Paris", "12-jan-2026", "Beautiful evening by the Seine!"),
    t("Tokyo", "05-mar-2025", "Loved the cherry blossoms."),
    t("New York", "15-dec-2023", "Broadway show was amazing!")
]
obj = datetime.strftime("%d-%m-%Y")
print(obj)


print(details)