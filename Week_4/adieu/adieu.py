quote = "Adieu, adieu, to"
c = 0

while True:
    try:
        prompt = input("")
        if c == 0:
            quote = quote + " " + prompt
            c += 1
        else:
            quote = quote + ", " + prompt
    except EOFError:
        if quote.count(",") == 3:
            temp = quote.rsplit(",",1)
            quote = " and".join(temp)
        elif quote.count(",") > 2 and quote.count(",") != 3:
            temp = quote.rsplit(",",1)
            quote = ", and".join(temp)
        print(quote,sep="")
        break

