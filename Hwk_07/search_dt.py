
from export_dt import export_dt
from print_dt import print_dt

def search_dt(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None