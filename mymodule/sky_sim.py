'''
This program simulates the distribution of foreground stars
toward the Andromeda Galaxy in ra/dec.
'''

# import python packages for use in this program
import math # pi, cos
import random # uniform

# Determine Andromeda location in ra/dec degrees
# from wikipedia
ra = '00:42:44.3'
dec = '41:16:09'

# convert to decimal degrees
D, M, S = dec.split(':')
dec = int(D)+int(M)/60+float(S)/3600

H, M, S = ra.split(':')
ra = 15*(int(H)+int(M)/60+float(S)/3600)
ra = ra/math.cos(dec*math.pi/180)

NSRC = 1_000_000

# make 1000 stars within 1 degree of Andromeda
ras = []
decs = []
for i in range(NSRC):
    ras.append(ra + random.uniform(-1, 1))
    decs.append(dec + random.uniform(-1, 1))


# now write these to a csv file for use by my other program
f = open('/Users/mpettyjo/Documents/ADACS Workshop/data/processed/catalog.csv', 'w')
print("id,ra,dec", file=f)
for i in range(NSRC):
    print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
f.close()

