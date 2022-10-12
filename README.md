# SpaceDyS technical interview day

This is my solution to SpaceDyS test. The requirements are
1. create a script (python, fortran, perl, ...) that reags the header of a FITS picture and give back the RA, DEC (both in decimal degrees) and Integration time.
2. Install SExtractor and use it on a FITS picture to extract data. The result should give a list of source point positions and magnitude (light flux)
3. Read the FITS image at extract the median from the matrix of the pixels

# Explanation of the solution

Python was chosen to be the language used in this test. Googling about FITS library the choice fell onto the `astropy` library. This was chosen becaue it was not just focused on handling FITS files, but also added support for astronomical coordinates.

However, skimming through the docs, the needed method to extract RA and DEC in decimal degree were not found. (The other way around, yes. From a SkyCoord object it's possible to store RA and DEC in `HH:MM:SS` format. Maybe it is present, but I couldn't find it). So, those two conversion function were implemented by hand. This allowed point 1 and 3 to be concluded almost simultaneously.

Regarding the SExtractor part, this is conveniently packaged and so installed through `apt-get`. Perusing the docs, a minimal `default.sex` and `catalog.param` were dumped from the tool itself.
The latter file, allows to select the measurable to be extracted from the picture.
Initially, the `X_IMAGE`, `Y_IMAGE` and `FLUX_POINTSOURCE` parameters were selected to be extracted. This generated an error message complaining about a missing `default.psf` file. Removing the `FLUX_POINTSOURCE` parameter, this message was replaced with a missing `default.conv`. A websearch yielded an [example file](example git) which allowed to extract the pixel positions of the sources. Tampering with the parameter files, and from the official docs, lately the `FLUX_ISO` parameter was chosen to successfully extract the magnitude.

## Useful links:
https://fits.gsfc.nasa.gov/fits_libraries.html
https://docs.astropy.org/en/latest/index.html
[example git](https://github.com/astromatic/sextractor/blob/master/config/default.conv)
https://sextractor.readthedocs.io/en/latest/Position.html
