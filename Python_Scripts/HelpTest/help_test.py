#! usr/bin/python

from colorama import Fore, Back, Style, init
import argparse

def main():
  ascii_art = Fore.GREEN + """
_____         _                 
|_   _|       | |                
  | | ___  ___| |_   _ __  _   _ 
  | |/ _ \/ __| __| | '_ \| | | |
  | |  __/\__ \ |_ _| |_) | |_| |
  \_/\___||___/\__(_) .__/ \__, |
                    | |     __/ |
                    |_|    |___/ 
              
Description: Test samplE 
                    
>>> Made by ZownHori
>>> https://github.com/JayAlvinCVallescas
-----------------------------------------------------
Usage: test.py <flag> <ip>
"""
  init()

  print(ascii_art)

if __name__ == "__main__":
  main()

