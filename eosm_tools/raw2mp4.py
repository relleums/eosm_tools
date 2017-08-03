"""
Convert a Canon raw video into a h264 video. Creates an output directory to 
process and keep:
1: DNG images
2: JPG images processed with RawTherapee using a color profile pp3 file.
3: An h264 video

Usage: eosm_raw2mp4 -i=RAW_PATH -o=OUT_DIR [-c=CONFIG_PATH]

Options:
    -i --raw_path=RAW_PATH          Path to the Canon raw video file.
    -o --out_dir=OUT_DIR            Path to the output dng file directory.
    -c --config_path=CONFIG_PATH    Raw Therapee pp3 config file path.
"""
import docopt
import sys
from . import tools

def main():
    try:
        arguments = docopt.docopt(__doc__)
        rc = tools.raw2mp4(
            raw_path=arguments['--raw_path'],
            out_dir=arguments['--out_dir'],
            dng2jpg_config_path=arguments['--config_path']
        )
        sys.exit(rc)
    except docopt.DocoptExit as e:
        print(e)

if __name__ == '__main__':
    main()