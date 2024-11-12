def doit(i : str, le : list,l : list,  m : str) -> None:
    r = le.index(i)
    m += le[l[i] + r]
    l[i] += r

def addem(m : str) -> None:
    m += ' '