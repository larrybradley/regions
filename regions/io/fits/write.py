# Licensed under a 3-clause BSD style license - see LICENSE.rst
from astropy.io import fits

from ..core import to_shape_list, SkyRegion


__all__ = [
    'write_fits_region',
    'fits_region_objects_to_table',
]


def fits_region_objects_to_table(regions):
    """
    Converts list of regions to FITS region table.

    See :ref:`gs-ds9`

    Parameters
    ----------
    regions : list
        List of `regions.Region` objects

    Returns
    -------
    region_string : `~astropy.table.Table`
        FITS region table
    """
    for reg in regions:
        if isinstance(reg, SkyRegion):
            raise TypeError(f'Every region must be a pixel region')

    shape_list = to_shape_list(regions, coordinate_system='image')
    return shape_list.to_fits()


def write_fits_region(filename, regions, header=None, overwrite=None):
    """
    Converts list of regions to FITS region table and write to a file.

    See :ref:`gs-fits`

    Parameters
    ----------
    filename : str
        Filename in which the table is to be written.
    regions : list
        List of `regions.Region` objects
    header : `~astropy.io.fits.Header`
        The FITS header
    """
    output = fits_region_objects_to_table(regions)

    bin_table = fits.BinTableHDU(data=output, header=header)
    bin_table.writeto(filename, overwrite=overwrite)
