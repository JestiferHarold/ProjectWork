# f = open("RISE OF EV encrypted.TXT",'r')
# text = f.read()   

def fuck(text):
    l = []
    finaltext = ''

    for i in range(0,len(text),3):
        ele = text[i:i+3]             
        l.append(ele)

    for i in l:
        finaltext += fun(i)

    return finaltext


def fun(i):
    #uppercase alphabets
    if i == '123':
        return 'A'
    elif i == '141':
        return 'B'
    elif i == '124':
        return 'C'
    elif i == '139':
        return 'D'
    elif i == '156':
        return 'E'
    elif i == '166':
        return 'F'
    elif i == '002':
        return 'G'
    elif i == '111':
        return 'H'
    elif i == '174':
        return 'I'
    elif i == '768':
        return 'J'
    elif i == '679':
        return 'K'
    elif i == '660':
        return 'L'
    elif i == '049':
        return 'M'
    elif i == '598':
        return 'N'
    elif i == '069':
        return 'O'
    elif i == '128':
        return 'P'
    elif i == '024':
        return 'Q'
    elif i == '379':
        return 'R'
    elif i == '380':
        return 'S'
    elif i == '666':
        return 'T'
    elif i == '989':
        return 'U'
    elif i == '116':
        return 'V'
    elif i == '247':
        return 'X'
    elif i == '050':
        return 'Y'
    elif i == '799':
        return 'Z'
    
    #lowercase alphabets
    elif i == '167':
        return 'a'
    elif i == '112':
        return 'b'
    elif i == '121':
        return 'c'
    elif i == '192':
        return 'd'
    elif i == '124':
        return 'e'
    elif i == '167':
        return 'f'
    elif i == '010':
        return 'g'
    elif i == '230':
        return 'h'
    elif i == '229':
        return 'i'
    elif i == '779':
        return 'j'
    elif i == '230':
        return 'k'
    elif i == '023':
        return 'l'
    elif i == '199':
        return 'm'
    elif i == '197':
        return 'n'
    elif i == '012':
        return 'o'
    elif i == '128':
        return 'p'
    elif i == '067':
        return 'q'
    elif i == '240':
        return 'r'
    elif i == '241':
        return 's'
    elif i == '676':
        return 't'
    elif i == '239':
        return 'u'
    elif i == '611':
        return 'v'
    elif i == '742':
        return 'x'
    elif i == '049':
        return 'y'
    elif i == '791':
        return 'z'
    
    #digits
    elif i == '047':
        return '0'
    elif i == '031':
        return '1'
    elif i == '303':
        return '2'
    elif i == '269':
        return '3'
    elif i == '449':
        return '4'
    elif i == '056':
        return '5'
    elif i == '043':
        return '6'
    elif i == '078':
        return '7'
    elif i == '761':
        return '8'
    elif i == '191':
        return '9'
    
    #special characters
    elif i == '007':
        return '~'
    elif i == '271':
        return '`'
    elif i == '986':
        return '!'
    elif i == '097':
        return '@'
    elif i == '008':
        return '#'
    elif i == '447':
        return '$'
    elif i == '230':
        return '%'
    elif i == '117':
        return '*'
    elif i == '118':
        return '&'
    elif i == '421':
        return '^'
    elif i == '496':
        return '('
    elif i == '423':
        return ')'
    elif i == '550':
        return '-'
    elif i == '545':
        return '_'
    elif i == '222':
        return '+'
    elif i == '333':
        return '='
    elif i == '865':
        return '{'
    elif i == '720':
        return '}'
    elif i == '624':
        return '['
    elif i == '244':
        return ']'
    elif i == '346':
        return ';'
    elif i == '421':
        return ':'
    elif i == '040':
        return "'"
    elif i == '881':
        return ','
    elif i == '391':
        return '.'
    elif i == '753':
        return '<'
    elif i == '087':
        return '>'
    elif i == '412':
        return '/'
    elif i == '904':
        return '?'
    elif i == '999':
        return ' '
    else:
        return ''
    

