"""
A CLI tool to read a .fits files, extract some metadata and median luminosity.
"""

import sys
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
from astropy.io import fits


def read_fits(filename: Path)-> Tuple[Dict, np.ndarray]:
    """Given a valid path to a FITS image, returns header and data"""
    with fits.open(str(filename)) as hdul:
        hdul.verify('fix')
        header, data = hdul[0].header, hdul[0].data
    return header, data


def get_parameters(value):
    pass


def get_median(value):
    pass


def main(filename: Path)-> None:
    """Main function"""
    header, data = read_fits(str(filename))
    get_parameters(header)
    get_median(data)

if __name__ == "__main__":
    file = Path(sys.argv[1])

    if file.exists() and file.suffix == '.fits':
        main(file)
    else:
        msg = f"""ERROR: {file} does not look to be valid.
        Please, the first argument needs to be a FITS file"""
        sys.exit(msg)

