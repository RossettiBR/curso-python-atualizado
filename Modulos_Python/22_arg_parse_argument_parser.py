from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostar Olá mundo na tela',
    type=str,
    metavar='STRING',
    default='Ola mundo',
    required=False,
    action='append',
    nargs='+',
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true',
)

args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

print(args.verbose)