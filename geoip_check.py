from geoip import geolite2

FILE_NAME = ''
file1 = open(FILE_NAME, 'r') 
Lines = file1.readlines() 

for line in Lines: 
    match = geolite2.lookup(line.strip())
    print(match)
