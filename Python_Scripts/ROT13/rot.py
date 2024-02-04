
#!usr/bin/python

import argparse
import codecs


def rot13(input_string):
    return codecs.encode(input_string, 'rot13')

def main():
    parser = argparse.ArgumentParser(
        description="A ROT13 script made with python\n\n"
                     "Example: python rot.py \"hello\"\n\n"
                     "Result: uryyb ",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )   
    parser.add_argument("input_string", nargs="?", help="String to be encoded with ROT13")
    args = parser.parse_args()
    
    if args.input_string is not None:
        result = rot13(args.input_string)
        print(result)
    else:
        print("Please provide a string to be encoded with ROT13.")
    
if __name__ == "__main__":
    main()