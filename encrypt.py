f = open("RISE OF EV.txt",'r')
data = f.read()
# Encryption functions for uppercase letters
def bets1(i):
    if i == 'A':
        return '123'
    elif i == 'B':
        return '141'
    elif i == 'C':
        return '124'
    elif i == 'D':
        return '139'
    elif i == 'E':
        return '156'
    elif i == 'F':
        return '166'
    elif i == 'G':
        return '002'
    elif i == 'H':
        return '111'
    elif i == 'I':
        return '174'
    elif i == 'J':
        return '768'
    elif i == 'K':
        return '679'
    elif i == 'L':
        return '660'
    elif i == 'M':
        return '049'
    elif i == 'N':
        return '598'
    elif i == 'O':
        return '069'
    elif i == 'P':
        return '128'
    elif i == 'Q':
        return '024'
    elif i == 'R':
        return '379'
    elif i == 'S':
        return '380'
    elif i == 'T':
        return '666'
    elif i == 'U':
        return '989'
    elif i == 'V':
        return '116'
    elif i == 'X':
        return '247'
    elif i == 'Y':
        return '050'
    else:
        return '701'

# Encryption function for lowercase letters
def bets2(i):
    if i == 'a':
        return '167'
    elif i == 'b':
        return '112'
    elif i == 'c':
        return '121'
    elif i == 'd':
        return '192'
    elif i == 'e':
        return '123'
    elif i == 'f':
        return '167'
    elif i == 'g':
        return '010'
    elif i == 'h':
        return '230'
    elif i == 'i':
        return '229'
    elif i == 'j':
        return '779'
    elif i == 'k':
        return '230'
    elif i == 'l':
        return '023'
    elif i == 'm':
        return '199'
    elif i == 'n':
        return '197'
    elif i == 'o':
        return '012'
    elif i == 'p':
        return '128'
    elif i == 'q':
        return '067'
    elif i == 'r':
        return '240'
    elif i == 's':
        return '241'
    elif i == 't':
        return '676'
    elif i == 'u':
        return '239'
    elif i == 'v':
        return '611'
    elif i == 'x':
        return '742'
    elif i == 'y':
        return '049'
    else:
        return '103'

# Encryption function for digits
def git(d):
    if d == '0':
        return '047'
    elif d == '1':
        return '031'
    elif d == '2':
        return '303'
    elif d == '3':
        return '269'
    elif d == '4':
        return '449'
    elif d == '5':
        return '056'
    elif d == '6':
        return '043'
    elif d == '7':
        return '078'
    elif d == '8':
        return '761'
    elif d == '9':
        return '191'

# Encryption function for space
def space(s):
    return '723'

# Encryption function for special characters
def special(s):
    if s == '~':
        return '007'
    elif s == '`':
        return '271'
    elif s == '!':
        return '986'
    elif s == '@':
        return '097'
    elif s == '#':
        return '008'
    elif s == '$':
        return '447'
    elif s == '%':
        return '230'
    elif s == '*':
        return '117'
    elif s == '&':
        return '118'
    elif s == '^':
        return '421'
    elif s == '(':
        return '496'
    elif s == ')':
        return '423'
    elif s == '-':
        return '550'
    elif s == '_':
        return '545'
    elif s == '+':
        return '222'
    elif s == '=':
        return '333'
    elif s == '{':
        return '865'
    elif s == '}':
        return '720'
    elif s == '[':
        return '624'
    elif s == ']':
        return '244'
    elif s == ';':
        return '346'
    elif s == ':':
        return '421'
    elif s == "'":
        return '040'
    elif s == ',':
        return '881'
    elif s == '.':
        return '391'
    elif s == '<':
        return '753'
    elif s == '>':
        return '087'
    elif s == '/':
        return '412'
    elif s == '?':
        return '904'
    elif "\n" == s:
        pass
    else:
        return '785'

# Main encryption function
def text(filedata):
    encrypted_text = ''
    for i in filedata:
        if i.isalpha():
            code = bets1(i) if i.isupper() else bets2(i)
        elif i.isdigit():
            code = git(i)
        elif i.isspace():
            code = space(i)
        else:
            code = special(i)
        encrypted_text += code
    return encrypted_text

op = text(data)

f2 = open("RISE OF EV ENCRYPTED.txt",'w')
f2.write(op)
f2.close()