fits_to_ascii
=============
This is a small code to convert fits files (IRAF format) to ascii.
The code recognizes the 'CRVAL1' and 'CDELT1' in the fits header.

To  run (replace filename with fits file):

  python fits_ascii.py filename
  
Dependencies
============
You need these modules: * [numpy](http://numpy.org)
                        * [Astropy](http://astropy.org)
                        * [argparse](https://docs.python.org/3/library/argparse.html)
                        * [pyfits](http://www.astropython.org/) 

