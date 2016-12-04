import os
import subprocess
import tempfile
import pkg_resources

def raw2dng(raw_path, out_path):
    """
    Convert a Canon raw video to a dng image series

    Parameters
    ----------
    raw_path

    out_path
    """   
    raw_path = os.path.abspath(raw_path)
    out_path = os.path.abspath(out_path)
    raw2dng_path = pkg_resources.resource_filename(
        'eosm_tools', 
        'resources/raw2dng')
    os.mkdir(out_path)
    dng_prefix = 'eosm'
    raw2dng_return_value = subprocess.call(
        [raw2dng_path, raw_path, dng_prefix], 
        cwd=out_path
    )
    return raw2dng_return_value


def dng2jpg(dng_path, out_path, config_path=None):
    """
    Convert a series of dng files into JPG files

    Parameters
    ----------
    dng_path

    out_path
    """   
    if config_path is None:
        config_path = pkg_resources.resource_filename(
            'eosm_tools', 
            'resources/fade.pp3')
    dng_path = os.path.abspath(dng_path)
    out_path = os.path.abspath(out_path)
    os.mkdir(out_path)
    rawtherapee_rc = subprocess.call([
        'rawtherapee',
        '-o', out_path,
        '-p', config_path,
        '-c', dng_path])   
    return rawtherapee_rc


def raw2jpg(raw_path, out_path, config_path=None):
    """
    Convert a Canon raw video into a series of JPG files

    Parameters
    ----------
    raw_path

    out_path
    """   
    with tempfile.TemporaryDirectory(prefix='eosm_raw2jpg_') as tmp_path:
        dng_path = os.path.join(tmp_path, 'dng')
        raw2dng(raw_path=raw_path, out_path=dng_path)
        dng2jpg(dng_path=dng_path, out_path=out_path, config_path=config_path)
