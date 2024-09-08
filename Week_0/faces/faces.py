def main():
    entry = input()
    convert(entry)

def convert(text):
    print(text.replace(":)","🙂").replace(":(","🙁"))

main()
