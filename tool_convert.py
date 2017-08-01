# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:39:38 2017
@author: Tim

"""

import csv

# zu konvertierende Datei öffnen
file=open("C:/Users/Tim/Desktop/TOOL.txt")

data=file.readlines()

# Länge der einzelnen Spalten herausfinden
head=data[0].split() # Header aufteilen

# Rechtes Ende der einzelnen Spalten bestimmen
rechts=[]

for spalte in head:
    rechts.append(data[0].find(spalte))

rechts.append(len(data[0]))

output=[head] # Ausgabematrix initialisieren

for zeile in data[1:-1]:
    row=[]
    for i in range(len(rechts)-1):
        row.append((zeile[rechts[i]:rechts[i+1]]).strip())
    output.append(row) 
    
# .csv-Datei schreiben
with open('werkzeuge.csv', 'w',newline='') as myfile:
    wr = csv.writer(myfile, delimiter='\t')
    wr.writerows(output)