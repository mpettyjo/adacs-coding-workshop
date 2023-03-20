#! /usr/bin/env python3

'''
This program simulates the distribution of foreground stars
toward the Andromeda Galaxy in ra/dec.
'''

# import python packages for use in this program
import math # pi, cos
import random # uniform

# global variables
NUM_STARS = 1_000_000

def get_radec():
    ''' Determine Andromeda location in ra/dec degrees.

    Function that computes the location of Andromeda in 
    right ascension, `ra` and declination, `dec`, both in degrees.
    Both `ra` and `dec` are converted from HMS and DMS forms.
    
    Parameters
    ----------
    RA : string
    DEC : string
    D, M, S : floats
    H, M, S : floats

    Returns
    -------
    Tuple
        Explanation of anonymous return value of type ``tuple``.
    (ra, dec) : tuple
        Tuple of the right ascension and declination in degrees.
    '''
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees
    D, M, S = DEC.split(':') # degrees, minutes, seconds
    dec = int(D)+int(M)/60+float(S)/3600

    H, M, S = RA.split(':') # hours, minutes, seconds
    ra = 15*(int(H)+int(M)/60+float(S)/3600)
    ra = ra/math.cos(dec*math.pi/180)
    return (ra, dec)

def make_stars(ra:float, dec:float, NUM_STARS:int) -> Tuple(List(float),List(float)):
    ''' Make 1000 stars within 1 degree of Andromeda's position on the sky.
    
        Function that computes the location of `NUM_STARS` around 1 degree of 
        Andromeda's position on the sky in right ascension `ra` and 
        declination `dec`.
        
        Parameters
        ----------
        ra: float
            Right ascension of Andromeda's position on the sky in degrees.
        dec: float
            Declination of Andromeda's position on the sky in degrees.
        NUM_STARS: int
            Number of stars to compute the location of within 1 degree of
            Andromeda's position.

        Returns
        -------
        Tuple
            Explanation of anonymous return value of type ``tuple``.
        (ras, decs) : tuple
            Tuple of the right ascension and declination in degrees.
        '''
    ras = []
    decs = []
    for i in range(NUM_STARS):
        ras.append(ra + random.uniform(-1, 1))
        decs.append(dec + random.uniform(-1, 1))
    return (ras, decs)

def main():
    ''' run get_radec and make_stars functions and save the ra/dec of 
    the stars to a catalog csv file '''
    ra, dec = get_radec()
    ras, decs = make_stars(ra, dec, NUM_STARS)

    # now write these to a csv file for use by my other program
    f = open('/Users/mpettyjo/Documents/ADACS Workshop/data/processed/catalog.csv', 'w', 
             encoding='utf-8')
    print("id,ra,dec", file=f)
    for i in range(NUM_STARS):
        print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    f.close()

if __name__ == '__main__':
    main()
