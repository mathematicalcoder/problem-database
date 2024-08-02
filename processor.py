'''
TO DEVELOP
- separate short answer from proof
'''

import math
import random
from problems import *

# edit problem database in problems.py

filteredProblems = []
d0S = []
d1S = []
d2S = []
d3S = []
d4S = []
d5S = []
d3P = []
d4P = []
d5P = []
d0SelecS = []
d1SelecS = []
d2SelecS = []
d3SelecS = []
d4SelecS = []
d5SelecS = []
d3SelecP = []
d4SelecP = []
d5SelecP = []

title = input("Title of problem set: ")
d0NumS = int(input("Number of short answer problems with difficulty 0: "))
d1NumS = int(input("Number of short answer problems with difficulty 1: "))
d2NumS = int(input("Number of short answer problems with difficulty 2: "))
d3NumS = int(input("Number of short answer problems with difficulty 3: "))
d4NumS = int(input("Number of short answer problems with difficulty 4: "))
d5NumS = int(input("Number of short answer problems with difficulty 5: "))
d3NumP = int(input("Number of proof problems with difficulty 3: "))
d4NumP = int(input("Number of proof problems with difficulty 4: "))
d5NumP = int(input("Number of proof problems with difficulty 5: "))
numS = d0NumS+d1NumS+d2NumS+d3NumS+d4NumS+d5NumS
numP = d3NumP+d4NumP+d5NumP

print(f"Your problem set will then have {str(numS)} short answer problems and {str(numP)} proof problems")
area = input("Area to focus on (A, C, G, N, or M; if none don't type anything): ")
showSource = input("Show source along with problems (y/n)? ")

if area in ['A', 'C', 'G', 'N', 'M']:
    for i in problems:
        if i[1] == area:
            filteredProblems.append(i)
else:
    filteredProblems = problems
    
for i in filteredProblems:
    if i[0] == 0 and i[2] == 'S':
        d0S.append(i)
    if i[0] == 1 and i[2] == 'S':
        d1S.append(i)
    if i[0] == 2 and i[2] == 'S':
        d2S.append(i)
    if i[0] == 3 and i[2] == 'S':
        d3S.append(i)
    if i[0] == 4 and i[2] == 'S':
        d4S.append(i)
    if i[0] == 5 and i[2] == 'S':
        d5S.append(i)
    if i[0] == 3 and i[2] == 'P':
        d3P.append(i)
    if i[0] == 4 and i[2] == 'P':
        d4P.append(i)
    if i[0] == 5 and i[2] == 'P':
        d5P.append(i)

for i in range (0, d0NumS):
    x = random.choice(d0S)
    d0SelecS.append(x)
    d0S.remove(x)
for i in range (0, d1NumS):
    x = random.choice(d1S)
    d1SelecS.append(x)
    d1S.remove(x)
for i in range (0, d2NumS):
    x = random.choice(d2S)
    d2SelecS.append(x)
    d2S.remove(x)
for i in range (0, d3NumS):
    x = random.choice(d3S)
    d3SelecS.append(x)
    d3S.remove(x)
for i in range (0, d4NumS):
    x = random.choice(d4S)
    d4SelecS.append(x)
    d4S.remove(x)
for i in range (0, d5NumS):
    x = random.choice(d5S)
    d5SelecS.append(x)
    d5S.remove(x)
for i in range (0, d3NumP):
    x = random.choice(d3P)
    d3SelecP.append(x)
    d3P.remove(x)
for i in range (0, d4NumP):
    x = random.choice(d4P)
    d4SelecP.append(x)
    d4P.remove(x)
for i in range (0, d5NumP):
    x = random.choice(d5P)
    d5SelecP.append(x)
    d5P.remove(x)
    
with open('test.tex', 'w') as file:
    file.write("\\documentclass[a4paper]{article}\n\\usepackage{multicol}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{asymptote}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{lemma}[theorem]{Lemma}\n\\newtheorem{claim}[theorem]{Claim}\n\\everymath{\\displaystyle}\n\\begin{document}\n\\begin{center}{\\huge\\textbf{"+title+"\\large\\\\"+str(numS+numP)+" problems}}\\end{center}\n\\section{Problems}\n\n")
    if len(d0SelecS)+len(d1SelecS)+len(d2SelecS)+len(d3SelecS)+len(d4SelecS)+len(d5SelecS) != 0:
        file.write("\\noindent\\textbf{SHORT ANSWER: Give the numerical answer for each problem.}")
        file.write("\\begin{enumerate}")
    if showSource == "y":
        for i in d0SelecS:
            file.write("\n\\item ("+i[3]+") "+i[4])
        for i in d1SelecS:
            file.write("\n\\item ("+i[3]+") "+i[4])
        for i in d2SelecS:
            file.write("\n\\item ("+i[3]+") "+i[4])
        for i in d3SelecS:
            file.write("\n\\item ("+i[3]+") "+i[4])
        for i in d4SelecS:
            file.write("\n\\item ("+i[3]+") "+i[4])
        for i in d5SelecS:
            file.write("\n\\item ("+i[3]+") "+i[4])
    else:
        for i in d0SelecS:
            file.write("\n\\item "+i[4])
        for i in d1SelecS:
            file.write("\n\\item "+i[4])
        for i in d2SelecS:
            file.write("\n\\item "+i[4])
        for i in d3SelecS:
            file.write("\n\\item "+i[4])
        for i in d4SelecS:
            file.write("\n\\item "+i[4])
        for i in d5SelecS:
            file.write("\n\\item "+i[4])
    if len(d0SelecS)+len(d1SelecS)+len(d2SelecS)+len(d3SelecS)+len(d4SelecS)+len(d5SelecS) != 0:
        file.write("\\end{enumerate}")
    if len(d3SelecP)+len(d4SelecP)+len(d5SelecP) != 0:
        file.write("\\noindent\\textbf{PROBLEM SOLVING: Write your complete solution for each problem.}")
        file.write("\\begin{enumerate}")
    if showSource == "y":
        for i in d3SelecP:
            file.write("\n\\item ("+i[3]+") "+i[4])
        for i in d4SelecP:
            file.write("\n\\item ("+i[3]+") "+i[4])
        for i in d5SelecP:
            file.write("\n\\item ("+i[3]+") "+i[4])
    else:
        for i in d3SelecP:
            file.write("\n\\item "+i[4])
        for i in d4SelecP:
            file.write("\n\\item "+i[4])
        for i in d5SelecP:
            file.write("\n\\item "+i[4])
    if len(d3SelecP)+len(d4SelecP)+len(d5SelecP) != 0:
        file.write("\\end{enumerate}")

    file.write("\\begin{center}\\textbf{--- THE ANSWERS ARE ON THE FOLLOWING PAGE ---}\\end{center}\\newpage\n\\section{Answers and Solutions}\n")
    
    if len(d0SelecS)+len(d1SelecS)+len(d2SelecS)+len(d3SelecS)+len(d4SelecS)+len(d5SelecS) != 0:
        file.write("\\noindent\\textbf{SHORT ANSWER:}")
        file.write("\\begin{multicols}{2}\\begin{enumerate}")
    for i in d0SelecS:
        file.write("\n\\item "+i[5])
    for i in d1SelecS:
        file.write("\n\\item "+i[5])
    for i in d2SelecS:
        file.write("\n\\item "+i[5])
    for i in d3SelecS:
        file.write("\n\\item "+i[5])
    for i in d4SelecS:
        file.write("\n\\item "+i[5])
    for i in d5SelecS:
        file.write("\n\\item "+i[5])
    if len(d0SelecS)+len(d1SelecS)+len(d2SelecS)+len(d3SelecS)+len(d4SelecS)+len(d5SelecS) != 0:
        file.write("\\end{enumerate}\\end{multicols}")
    if len(d3SelecP)+len(d4SelecP)+len(d5SelecP) != 0:
        file.write("\\noindent\\textbf{PROBLEM SOLVING:}")
        file.write("\\begin{enumerate}")
    for i in d3SelecP:
        file.write("\n\\item "+i[5])
    for i in d4SelecP:
        file.write("\n\\item "+i[5])
    for i in d5SelecP:
        file.write("\n\\item "+i[5])
    if len(d3SelecP)+len(d4SelecP)+len(d5SelecP) != 0:
        file.write("\\end{enumerate}")
    
    file.write("\n\\end{document}")
    file.close()

print("Done! Check test.tex to see your problem set")