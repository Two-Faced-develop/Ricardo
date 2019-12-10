msg = 'Hello DZ world'
msg += " "
s = ""
words = []

for i in range(len(msg)):
    if msg[i] != " ":
        s += msg[i]
    if msg[i-1] != " " and msg[i] == " ":
        words.append(s)
        s = ''
        print(words)

for j in words:
    if j == "DZ":
        print("DZ was found")