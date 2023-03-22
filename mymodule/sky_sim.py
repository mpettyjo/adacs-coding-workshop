#! /usr/bin/env python3

'''
This program simulates the distribution of foreground stars
toward the Andromeda Galaxy in ra/dec.
'''

# import python packages for use in this program
import math # pi, cos
import random # uniform
import argparse
import pandas as pd
import numpy as np

# global variables
NUM_STARS = 1_000_000

def get_radec():
    ''' Determine Andromeda location in ra/dec degrees.

    Function that computes the location of Andromeda in 
    right ascension, `ra` and declination, `dec`, both in degrees.
    Both `ra` and `dec` are converted from HMS and DMS forms.

    Returns
    -------
    (ra, dec) : (float, float)
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

def make_stars(ra:float, dec:float, NUM_STARS:int):
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
        (ras, decs) : (list(float), list(float))
            Tuple of the right ascension and declination in degrees.
        '''
    ras = []
    decs = []
    for i in range(NUM_STARS):
        ras.append(ra + random.uniform(-1, 1))
        decs.append(dec + random.uniform(-1, 1))
    return (np.array(ras), np.array(decs))

def main():
    ''' Make and save right ascension and declination catalog of stars to csv.

    Function that runs the get_radec and make_stars functions and 
    saves the right ascension and declination of the stars to a catalog 
    csv file named catalog.csv. 
    '''
    ra, dec = get_radec()
    ras, decs = make_stars(ra, dec, NUM_STARS)

    # now write these to a csv file for use by my other program
    data = []
    for i in range(NUM_STARS):
        data.append([int(i),np.round(ras[i],12),np.round(decs[i],12)])
    df = pd.DataFrame(data, columns=['id','ra','dec'])

    df.to_csv('/Users/mpettyjo/Documents/ADACS Workshop/mymodule/catalog.csv') 

def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser

if __name__ == '__main__':
    parser = skysim_parser()
    options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.ra, options.dec]:
        ra, dec = get_radec()
    else:
        ra = options.ra
        dec = options.dec
    
    ras, decs = make_stars(ra, dec, NUM_STARS)

    # now write these to a csv file for use by my other program
    data = []
    for i in range(NUM_STARS):
        data.append([int(i),np.round(ras[i],12),np.round(decs[i],12)])
    df = pd.DataFrame(data, columns=['id','ra','dec'])
    df.to_csv('/Users/mpettyjo/Documents/ADACS Workshop/mymodule/catalog.csv') 

    print(f"Wrote {options.out}")
