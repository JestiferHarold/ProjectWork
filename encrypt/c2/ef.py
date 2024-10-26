def bets1(i):
    if i in ('A','123'):
        return '123', 'A'
    elif i  in ('B','141'):
        return '141', 'B'
    elif i in ('C','124'):
        return '124', 'C'
    elif i in ('D', '139'):
        return '139', 'D'
    elif i in ('E','156'):
        return '156', 'E'
    elif i in ('F','166'):
        return '166', 'F'
    elif i in ('G','002'):
        return '002', 'G'
    elif i in ('H','111'):
        return '111', 'H'
    elif i in ('I','174'):
        return '174', 'I'
    elif i in ('J','768'):
        return '768', 'J'
    elif i in ('K','679'):
        return '679', 'K'
    elif i in ('L','660'):
        return '660', 'L'
    elif i in ('M','049'):
        return '049', 'M'
    elif i in ('N','598'):
        return '598', 'N'
    elif i in ('O','069'):
        return '069', 'O'
    elif i in ('P','128'):
        return '128', 'P'
    elif i in ('Q','024'):
        return '024', 'Q'
    elif i in ('R','379'):
        return '379', 'R'
    elif i in ('S','380'):
        return '380', 'S'
    elif i in ('T','666'):
        return '666', 'T'
    elif i in ('U','989'):
        return '989', 'U'
    elif i in ('V','116'):
        return '116', 'V'
    elif i in ('X','247'):
        return '247', 'X'
    elif i in ('Y','050'):
        return '050', 'Y'
    else:
        return '701', 'Z'

def bets2(i):
    if i in ('a','167'):
        return '167', 'a'
    elif i in ('b','112'):
        return '112', 'b'
    elif i in ('c','121'):
        return '121', 'c'
    elif i in ('d','192'):
        return '192', 'd'
    elif i in ('e','124'):
        return '123', 'e'
    elif i in ('f','167'):
        return '167', 'f'
    elif i in ('g','010'):
        return '010', 'g'
    elif i in ('h','230'):
        return '230', 'h'
    elif i in ('i','229'):
        return '229', 'i'
    elif i in ('j','779'):
        return '779', 'j'
    elif i in ('k','230'):
        return '230', 'k'
    elif i in ('l','023'):
        return '023', 'l'
    elif i in ('m','199'):
        return '199', 'm'
    elif i in ('n','197'):
        return '197', 'n'
    elif i in ('o','012'):
        return '012', 'o'
    elif i in ('p','128'):
        return '128', 'p'
    elif i in ('q','067'):
        return '067', 'q'
    elif i in ('r','240'):
        return '240', 'r'
    elif i in ('s','241'):
        return '241', 's'
    elif i in ('t','676'):
        return '676', 't'
    elif i in ('u','239'):
        return '239', 'u'
    elif i in ('v','611'):
        return '611', 'v'
    elif i in ('x','742'):
        return '742', 'x'
    elif i in ('y','049'):
        return '049', 'y'
    else:
        return '103', 'z'

def git(d):
    if d in ('0','047'):
        return '047', '0'
    elif d in ('1','031'):
        return '031', '1'
    elif d in ('2','303'):
        return '303', '2'
    elif d in ('3','269'):
        return '269', '3'
    elif d in ('4','449'):
        return '449', '4'
    elif d in ('5','056'):
        return '056','5'
    elif d in ('6','043'):
        return '043', '6'
    elif d in ('7','078'):
        return '078', '7'
    elif d in ('8','761'):
        return '761', '8'
    elif d in ('9','191'):
        return '191', '9'
def space(s):
    return '723', ' '

def special(s):
    if s in ('~','007'):
        return '007', '~'
    elif s in ('`','271'):
        return '271', '`'
    elif s in ('!'.'986'):
        return '986', '!'
    elif s in ('@','097'):
        return '097', '@'
    elif s in ('#','008'):
        return '008', '#'
    elif s in ('$','447'):
        return '447', '$'
    elif s in ('%','230'):
        return '230', '%'
    elif s in ('*','117'):
        return '117', '*'
    elif s in ('&','118'):
        return '118', '&'
    elif s in ('^','421'):
        return '421', '^'
    elif s in ('(','496'):
        return '496', '('
    elif s in (')','423'):
        return '423', ')'
    elif s in ('-','550'):
        return '550', '-'
    elif s in ('_'.'545'):
        return '545', '_'
    elif s in ('+','222'):
        return '222', '+'
    elif s in ('=','333'):
        return '333', '='
    elif s in ('{','865'):
        return '865', '{'
    elif s in ('}','720'):
        return '720', '}'
    elif s in ('[','624'):
        return '624', '['
    elif s in (']','244'):
        return '244', ']'
    elif s in (';','346'):
        return '346', ';'
    elif s in (':','421'):
        return '421', ':'
    elif s in ("'",'040'):
        return '040', "'"
    elif s in (',','881'):
        return '881', ','
    elif s in ('.','391'):
        return '391', '.'
    elif s in ('<','753'):
        return '753', '<'
    elif s in ('>','087'):
        return '087', '>'
    elif s in ('/','412'):
        return '412', '/'
    elif s in ('?','904'):
        return '904', '?'
    else:
        return '785','\ '.rstrip()

def text(ptct):
    global ft
    ft = ''
    for i in ptct:
        if i.isalpha():
            if i.isupper():
                bets1()
            else:
                bets2()
        elif i.isdigit():
            git()
        elif i.isspace():
            space()
        else:
            special()
    
