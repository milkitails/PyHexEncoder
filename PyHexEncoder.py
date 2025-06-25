import binascii
import argparse
import os

parser = argparse.ArgumentParser(description='PyHexInterpreter')
parser.add_argument('file', type=str, help='file')
args = parser.parse_args()

with open(args.file, "r", encoding="utf-8") as file:
	with open(f"{os.path.basename(args.file).replace('.py', '')}.bin", "a", encoding="utf-8") as bin_file:
		bin_file.write(binascii.hexlify(file.read().encode()).decode())
