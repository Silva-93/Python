from argparse import ArgumentParser

parser = ArgumentParser()

# Recebendo arquimentos
parser.add_argument('-b')
args = parser.parse_args()
print(args.b)