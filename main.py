import argparse
from comic2epub.convert import convert
from comic2epub.config import MyConfig

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', dest='config', type=str, default='settings.toml')

    args = parser.parse_args()

    cfg = MyConfig()
    cfg.parse_file(args.config)

    convert(cfg)

if __name__ == '__main__':
    main()
