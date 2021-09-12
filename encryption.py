from os import write


switch = {'A' : '9', 'B': '*', 'C': 'f', 'D': '/', 'E':'@', 'F': '6',
'G': 'k', 'H': '^', 'I': 's', 'J': 8, 'K': ';', 'L': '0', 'M': '#',
'N': 'j', 'O': '(', 'P' : ')', 'Q': '%', 'R': ':', 'S' : '$', 'T': '1',
'U': '4', 'V': '-', 'W': '?', 'X':'>', 'Y': '.', 'Z':']',
'a' : '10', 'b': '}', 'c': 'S', 'd': '!', 'e':'d', 'f': '+',
'g': '=', 'h': 'w', 'i': '<', 'j': '[', 'k': 'p', 'l': ',', 'm': '&',
'n': 'R', 'o': '{', 'p' : '|', 'q': 'E', 'r': '25', 's' : '$-', 't': '?',
'u': '4', 'v': '@', 'w': 'Q', 'x':'<', 'y': ':', 'z':'*',' ':'9', '.':'<', ':': 'P'}

infile = open("info_security.txt", 'r')
file_contents = infile.read()
file_contents = file_contents.rstrip('\n')

outfile = open("encryption.txt", 'w')

for x in file_contents:
    outfile.write(switch[x])

infile.close()
outfile.close()
