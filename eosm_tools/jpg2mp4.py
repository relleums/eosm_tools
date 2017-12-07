"""
Convert a jpg image sequence into a h264 mp4 video with decent settings for the 
Canon EOS M.

Usage: eosm_jpg2mp4 -i=JPG_DIR -p=JPG_PREFIX -o=OUT_PATH

Options:
    -i --jpg_dir=JPG_DIR          Path to the Canon raw video file.
    -p --jpg_prefix=JPG_PREFIX      Basename prefix of jpg images before 6 digit 
                                    number begins, e.g. 'my_images_'.
    -o --out_path=OUT_PATH            Output directory with dng images.
"""
import docopt
import sys
from . import tools

def main():
    try:
        arguments = docopt.docopt(__doc__)
        rc = tools.jpg2mp4(
            jpg_dir=arguments['--jpg_dir'], 
            jpg_prefix=arguments['--jpg_prefix'], 
            out_path=arguments['--out_path'],
        )
        sys.exit(rc)
    except docopt.DocoptExit as e:
        print(e)

if __name__ == '__main__':
    main()