a=[[[1,4,2,5,3],[1,2,3,4,5],[1,4,2,3,5],[1,2,4,3,5]],
  [[2,4,1,5,3],[2,1,3,4,5],[2,4,1,3,5],[2,3,4,1,5]],
  [[3,4,1,5,2],[3,1,2,4,5],[3,4,1,2,5],[3,2,4,1,5]],
  [[4,3,1,5,2],[4,1,2,3,5],[4,3,1,2,5],[4,2,3,1,5]],
  [[5,3,1,4,2],[5,1,2,3,4],[5,3,1,2,4],[5,2,3,1,4]],
  [[1,4,2,3,5],[1,4,2,5,3],[1,2,3,4,5],[1,2,4,3,5]],
  [[2,4,1,3,5],[2,4,1,5,3],[2,1,3,4,5],[2,3,4,1,5]],
  [[3,4,1,2,5],[3,4,1,5,2],[3,1,2,4,5],[3,2,4,1,5]],
  [[4,3,1,2,5],[4,3,1,5,2],[4,1,2,3,5],[4,2,3,1,5]],
  [[5,3,1,4,2],[5,1,2,3,4],[5,3,1,2,4],[5,2,3,1,4]]
   ]
c=0
for x in a:
  c+=1
  d=-1
  pngfile=[]
  for y in x:
    d+=1
    yimg=y.copy()
    yimg=[z-1 for z in yimg]
    pngfile.append('kolam/kolam-'+''.join(map(str, yimg))+'.png')
  print(rf"""\begin{{cloze}}[points=4]{{Ethnomathematik: Kolam (Version {c})}}
  \textbf{{Ethnomathematik: Kolam}}\\ Ein Kolam ist eine in einem einzigen Linienzug durchf\"uhrbare, regelgeleitet erstellte Kreidezeichnung, wie sie sich noch heute bei den s\"udindischen Tamilen als ethnomathematische Praxis auffinden l\"asst. \\ Unten sind mehrere solche Kolam mit 8 Armen zu je 5 Punkten in vereinfachter Form abgebildet.\\ \\ <ol type=a><li>Wenn man mit dem Z\"ahlen der Punkte beim innersten Punkt des nach oben zeigenden Arms beginnt, welches Bild steht dann f\"ur die links herum abgelaufene Punktfolge $<{str(x[0]).strip('[]')}>$?  \\
  \begin{{multi}}[single,horizontal,points=2]
   \item \includegraphics[width=3.5cm]{{{pngfile[1]}}}
   \item* \includegraphics[width=3.5cm]{{{pngfile[0]}}}
   \item \includegraphics[width=3.5cm]{{{pngfile[3]}}}
   \item \includegraphics[width=3.5cm]{{{pngfile[2]}}}
  \end{{multi}}</li>
  \begin{{multi}}[single,points=2]
  \\ <li> Ein Kolam kann genau dann in einem Zug gezeichnet werden, wenn f\"ur die Anzahl der Arme und die Anzahl der Punkte auf einem Arm gilt: \item* Die beiden Anzahlen sind teilerfremd.
   \item Es gibt mehr Arme als Punkte je Arm.
   \item Die Differenz der Armanzahl und der Punktanzahl ist ungerade.
   \item Die Armanzahl ist gerade, die Punktanzahl ungerade.
  \end{{multi}} </li></ol>
  \end{{cloze}}\newpage """)

