from datetime import datetime

def datefromiso(year, week, day):
    return datetime.strptime("%d%02d%d" % (year, week, day), "%Y%W%w")

print(datefromiso(2012, 7, 4)
