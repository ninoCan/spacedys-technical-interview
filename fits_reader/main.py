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


def _hms_to_dd(value: str) -> float:
    """Helper function: convert a HH:MM:SS string to decimal degrees"""
    hh, mm, ss = [float(x) for x in value.strip().split(":")]
    dd = 15 * hh + mm / 4.0 + ss / 240
    return dd


def _deg_to_dd(value:str) -> float:
    """Helper function: convert dg:mn:sc to decimal degrees"""
    dg, mn, sc = [float(x) for x in value.strip().split(":")]
    if dg >= 0:
        dd = dg + mn / 60 + sc / 3600
    else:
        dd = dg - mn / 60 - sc / 3600
    return dd


def get_parameters(header: Dict) -> None:
    """Print RA, DEC, Integration time from a HDU list"""

    params = {
        "RA": [_hms_to_dd(header["RA"]), "°"],
        "DEC":[ _deg_to_dd(header["DEC"]), "°"],
        "Integration_time": [header["EXPTIME"], 'sec'],
    }

    for key, val in params.items():
        print(key, ": ", val[0], val[1])


def get_median(data: np.ndarray)-> int:
    """Print the median of the data matrix"""
    print("Median:", np.median(data))


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

