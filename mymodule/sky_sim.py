'''
This program simulates the distribution of foreground stars
toward the Andromeda Galaxy in ra/dec.
'''

# import python packages for use in this program
import math # pi, cos
import random # uniform

# Determine Andromeda location in ra/dec degrees
# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'

# convert to decimal degrees
D, M, S = DEC.split(':')
dec = int(D)+int(M)/60+float(S)/3600

H, M, S = RA.split(':')
ra = 15*(int(H)+int(M)/60+float(S)/3600)
ra = ra/math.cos(dec*math.pi/180)

NUM_STARS = 1_000_000

# make 1000 stars within 1 degree of Andromeda
ras = []
decs = []
for i in range(NUM_STARS):
    ras.append(ra + random.uniform(-1, 1))
    decs.append(dec + random.uniform(-1, 1))


# now write these to a csv file for use by my other program
f = open('/Users/mpettyjo/Documents/ADACS Workshop/data/processed/catalog.csv',
         'w', encoding='utf-8')
print("id,ra,dec", file=f)
for i in range(NUM_STARS):
    print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
f.close()
