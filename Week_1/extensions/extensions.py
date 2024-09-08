def main():
    fname = input("File name: ").strip().lower()
    suf = fname.split(".")[-1]

    content(suf)



def content(suffix):
    app = ["zip","pdf"]
    img = ["gif","jpg","jpeg","png"]
    txt = ["txt"]

    if suffix in app:
        print("application/" + suffix)
    elif suffix in img :
        if suffix == "jpg":
            print("image/jpeg")
        else:
            print("image/"+suffix)
    elif suffix in txt:
        print("text/plain")
    else:
        print("application/octet-stream")


main()
