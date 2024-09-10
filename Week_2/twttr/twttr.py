post = input("Input: ")
print(
    "Output:",
    "".join(
        [
            i if not (i in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]) else ""
            for i in post
        ]
    ),
)
