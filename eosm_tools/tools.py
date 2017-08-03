import os
import subprocess
import shutil
import tempfile
import pkg_resources

def raw2dng(raw_path, out_dir, dng_prefix='eosm_', stdout_path=None):
    """
    Convert a Canon raw video to a dng image series

    Parameters
    ----------
    raw_path

    out_dir

    stdout_path     [None] If None, stdout and stderr is printed.
    """   
    raw_path = os.path.abspath(raw_path)
    out_dir = os.path.abspath(out_dir)
    raw2dng_path = pkg_resources.resource_filename(
        'eosm_tools', 
        os.path.join('resources','raw2dng')
    )
    os.makedirs(out_dir, exist_ok=True)
    if stdout_path is not None:
        stdo = open(stdout_path+'.o', 'w')
        stde = open(stdout_path+'.e', 'w')

        rc = subprocess.call(
            [raw2dng_path, raw_path, dng_prefix], 
            cwd=out_dir,
            stdout=stdo, 
            stderr=stde,
        )

        stdo.close()
        stde.close()
    else:
        rc = subprocess.call(
            [raw2dng_path, raw_path, dng_prefix], 
            cwd=out_dir
        )
    return rc


def dng2jpg(dng_dir, out_dir, config_path=None, stdout_path=None):
    """
    Convert a series of dng files into JPG files

    Parameters
    ----------
    dng_dir

    out_dir
    """   
    if config_path is None:
        config_path = pkg_resources.resource_filename(
            'eosm_tools', 
            'resources/fade.pp3'
        )

    rawtherapee_call = [
        'rawtherapee',
        '-o', out_dir, # capital letter 'O' saves the input pp3 config in the output dir
        '-p', config_path,
        '-c', dng_dir,
        '-j1' # JPEG Compression 1 - 100
    ]

    dng_dir = os.path.abspath(dng_dir)
    out_dir = os.path.abspath(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    if stdout_path is not None:
        stdo = open(stdout_path+'.o', 'w')
        stde = open(stdout_path+'.e', 'w')

        rc = subprocess.call(
            rawtherapee_call, 
            stdout=stdo, 
            stderr=stde,
        )

        stdo.close()
        stde.close()
    else:
        rc = subprocess.call(
            rawtherapee_call,
        )
    return rc


def jpg2mp4(jpg_dir, jpg_prefix, out_path, threads='auto', stdout_path=None):
    '''
    possible input basename pattern: prefix+'%06d.jpg'
    '''

    if threads != 'auto':
        threads = str(threads)
    avconv_command = [
        'avconv',
        '-y',  # force overwriting of existing output file
        '-framerate', str(int(25)),  # Frames per second
        '-f', 'image2',
        '-i', os.path.join(jpg_dir, jpg_prefix+'%06d.jpg'),
        '-c:v', 'h264',
        '-s', '1920x1080',  # sample images to FullHD 1080p
        '-crf', '16',  # high quality 0 (best) to 53 (worst)
        '-crf_max', '20',  # worst quality allowed
        '-threads', threads,
        out_path,
    ]

    if stdout_path is not None:
        stdo = open(stdout_path+'.o', 'w')
        stde = open(stdout_path+'.e', 'w')

        rc = subprocess.call(
            avconv_command, 
            stdout=stdo, 
            stderr=stde,
        )

        stdo.close()
        stde.close()
    else:
        rc = subprocess.call(
            avconv_command,
        )
    return rc


def raw2mp4(
    raw_path, 
    out_dir, 
    dng2jpg_config_path=None, 
    av_conv_threads='auto'
):
    print('EOS M raw video processing ...')
    raw_path = os.path.abspath(raw_path)
    out_dir = os.path.abspath(out_dir)
    dng2jpg_config_path = os.path.abspath(dng2jpg_config_path)

    # Prepare out_dir
    # ---------------
    print('lnk raw to out_dir', out_dir, ' ... ', end='', flush=True)
    os.makedirs(out_dir, exist_ok=True)
    std_dir = os.path.join(out_dir,'std')
    os.makedirs(std_dir, exist_ok=True)
    raw_basename = os.path.basename(raw_path)
    raw_prefix = os.path.splitext(raw_basename)[0]
    new_raw_path = os.path.join(out_dir, raw_basename)
    os.link(raw_path, new_raw_path) # hard link
    raw_path = new_raw_path
    print('done.')

    # RAW to DNG
    # ----------
    print('raw2dng ... ', end='', flush=True)
    dng_dir = os.path.join(out_dir, 'dng')
    raw2dng_rc = raw2dng(
        raw_path=raw_path, 
        out_dir=dng_dir, 
        dng_prefix=raw_prefix+'_',
        stdout_path=os.path.join(std_dir,'raw2dng')
    )
    if raw2dng_rc == 0:
        print('done.')
    else:
        with open(os.path.join(std_dir,'raw2dng.e')) as fout:
            print(fout.read())

    # DNG to JPG
    # ----------
    print('dng2jpg ... ', end='', flush=True)
    jpg_dir = os.path.join(out_dir, 'jpg')

    if dng2jpg_config_path is None:
        dng2jpg_config_path = pkg_resources.resource_filename(
            'eosm_tools', 
            'resources/fade.pp3'
        )
    os.makedirs(jpg_dir, exist_ok=True)
    dng2jpg_config_basename = os.path.basename(dng2jpg_config_path)
    new_dng2jpg_config_path = os.path.join(jpg_dir, dng2jpg_config_basename)
    shutil.copy(dng2jpg_config_path, new_dng2jpg_config_path)
    dng2jpg_config_path = new_dng2jpg_config_path

    dng2jpg_rc = dng2jpg(
        dng_dir=dng_dir, 
        out_dir=jpg_dir, 
        config_path=dng2jpg_config_path,
        stdout_path=os.path.join(std_dir,'dng2jpg')
    )
    if dng2jpg_rc == 0:
        print('done.')
    else:
        with open(os.path.join(std_dir,'dng2jpg.e')) as fout:
            print(fout.read())

    # JPG to MP4
    # ----------
    print('jpg2mp4 ... ', end='', flush=True)
    jpg2mp4_rc = jpg2mp4(
        jpg_dir=jpg_dir,
        jpg_prefix=raw_prefix+'_',
        out_path=os.path.join(out_dir, raw_prefix+'.mp4'),
        threads=av_conv_threads,
        stdout_path=os.path.join(std_dir,'jpg2mp4')
    )
    if jpg2mp4_rc == 0:
        print('done.')
    else:
        with open(os.path.join(std_dir,'jpg2mp4.e')) as fout:
            print(fout.read())

    # Return
    # ------
    if raw2dng_rc == 0 and dng2jpg_rc == 0 and jpg2mp4_rc == 0:
        return 0
    else:
        return 1