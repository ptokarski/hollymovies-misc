from argparse import ArgumentParser, FileType

from hollymovies.data import dumpdata, loaddata


def _setup_dumpdata_subparser(subparsers):
    subparser = subparsers.add_parser(
        'dumpdata', description=(
            'Dumps data from the database as json lines to provided file path.'
        )
    )
    subparser.add_argument(
        '--output-file', help='Output file name.',
        type=FileType('w'), required=True
    )
    subparser.set_defaults(subcommand=dumpdata)


def _setup_loaddata_subparser(subparsers):
    subparser = subparsers.add_parser(
        'loaddata',
        description='Loads data from provided json-lines file to the database.'
    )
    subparser.add_argument(
        '--input-file', help='Input file name.',
        type=FileType('r'), required=True
    )
    subparser.set_defaults(subcommand=loaddata)


def _setup_subparsers(main_parser):
    subparsers = main_parser.add_subparsers(dest='subcommand', required=True)
    _setup_dumpdata_subparser(subparsers)
    _setup_loaddata_subparser(subparsers)


def parse_args():
    parser = ArgumentParser(description='Simple app for movies management.')
    _setup_subparsers(parser)
    return vars(parser.parse_args())


def main():
    parsed_args = parse_args()
    subcommand = parsed_args.pop('subcommand')
    subcommand(**parsed_args)


if __name__ == "__main__":
    main()
