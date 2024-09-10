import argparse
import pyfiglet
import random

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--font", help="specify font")

args = parser.parse_args()
fonts = pyfiglet.FigletFont.getFonts()
r_font = random.choice(fonts)
if args.font == None:
    prompt = input("Input: ")

    x = pyfiglet.Figlet(font=r_font)
    print(x.renderText(prompt))

elif args.font != None and args.font in fonts:
    prompt = input("Input: ")

    x = pyfiglet.Figlet(font=args.font)
    print(x.renderText(prompt))
else:
    exit(1)
