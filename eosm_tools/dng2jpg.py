"""
Convert a dng image series into JPG images using Raw Therapee

Usage: eosm_dng2jpg -i=DNG_DIR -o=OUT_DIR [-c=CONFIG_PATH]

Options:    
    -i --dng_dir=DNG_DIR            Input directory with dng images.
    -o --out_dir=OUT_DIR            Output directory with jpg iamges.
    -c --config_path=CONFIG_PATH    Raw Therapee pp3 config path.
"""
import docopt
import sys
from . import tools

def main():
    try:
        arguments = docopt.docopt(__doc__)
        rc = tools.dng2jpg(
            dng_dir=arguments['--dng_dir'],
            out_dir=arguments['--out_dir'],
            config_path=arguments['--config_path']
        )
        sys.exit(rc)
    except docopt.DocoptExit as e:
        print(e)

if __name__ == '__main__':
    main()