from Utils import *
import re

def decizie(token):
    # variabilele incep obligatoriu cu litera sau _ si se incheie cu litere, cifre sau _
    regexVar = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]")

    # bibliotecile incep cu orice litera, cifra sau _ si trebuie sa contina .h la final
    regexBiblioteca = re.compile(r"\w[a-zA-Z]+[.]h")
    regexCifra = re.compile(r'\d')

    # float-urile pot sa inceapa cu + sau minus, maxim o aparitie, optional partea intreaga
    # iar daca au punct ( maxim unul ), avem cel putin o cifra
    # daca avem e sau E, obligatoriu avem inca o cifra cu +- care apare maxim o data
    regexFloat = re.compile(r'[-+]?\d*\.?\d+([eE][-+]?\d+)?')

    if token in keywords():
        print(token + " KEYWORD")
    elif token in operators().keys():
        print(token + " ", operators()[token])
    elif token in delimiters().keys():
        eticheta = delimiters()[token]
        if eticheta == 'TAB' or eticheta == 'NEWLINE':
            print(eticheta)
        else:
            print(token + " ", eticheta)
    elif re.search(regexBiblioteca, token):
        print(token + " BIBLIOTECA")
    elif re.match(regexVar, token) or "'" in token or '"' in token:
        print(token + ' VARIABILA')
    elif re.match(regexCifra, token):
        if re.match(regexFloat, token):
            print(token + ' FLOAT')
        else:
            print(token + ' INT')
    return True

def delimiterCorrection(line):
    tokens = line.split(" ")
    for delimiter in delimiters().keys():
        for token in tokens:
            if token == delimiter:
                pass
            elif delimiter in token:
                # despart token-urile compuse
                pos = token.find(delimiter)
                tokens.remove(token)
                token = token.replace(delimiter, " ")
                extra = token[:pos]
                token = token[pos + 1:]
                tokens.append(delimiter)
                tokens.append(extra)
                tokens.append(token)
            else:
                pass
    for token in tokens:
        if token in ['\t', '\n', ' ']:
            tokens.remove(token)
        elif ' ' in token:
            tokens.remove(token)
            token = token.split(' ')
            for d in token:
                tokens.append(d)
    return tokens

