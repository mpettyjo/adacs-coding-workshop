'''
This program simulates the distribution of foreground stars toward the Andromeda Galaxy.
'''

# import python packages for use in this program
import math # pi, cos
import random # uniform

# Determine Andromeda location in ra/dec degrees
# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'

# convert to decimal degrees
d, m, s = DEC.split(':')
DEC = int(d)+int(m)/60+float(s)/3600

h, m, s = RA.split(':')
RA = 15*(int(h)+int(m)/60+float(s)/3600)
RA = RA/math.cos(DEC*math.pi/180)

NSRC = 1_000_000

# make 1000 stars within 1 degree of Andromeda
RAs = []
DECs = []
for i in range(NSRC):
    RAs.append(RA + random.uniform(-1, 1))
    DECs.append(DEC + random.uniform(-1, 1))


# now write these to a csv file for use by my other program
f = open('/Users/mpettyjo/Documents/ADACS Workshop/data/processed/catalog.csv', 'w')
print("id,ra,dec", file=f)
for i in range(NSRC):
    print("{0:07d}, {1:12f}, {2:12f}".format(i, RAs[i], DECs[i]), file=f)
f.close()
