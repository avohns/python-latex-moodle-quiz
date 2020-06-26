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
  print(rf"""\begin{{cloze}}[points=4]{{Ethnomathematics: Kolam (Version {c})}}
  \textbf{{Ethnomathematitcs: Kolam}}\\ Kolams are an ethnomathematical practice that is still common in southern India. A kolam is a chalk drawing that can be executed in a single line and is created according to a set of rules.\\ Below several such kolams with 8 arms of 5 points each are shown in a simplified form.\\ \\ <ol type=a><li>If you start counting the points at the innermost point of the upward pointing arm, which picture stands for the counterclockwise sequence of points $<{str(x[0]).strip('[]')}>$?  \\
  \begin{{multi}}[single,horizontal,points=2]
   \item \includegraphics[width=3.5cm]{{{pngfile[1]}}}
   \item* \includegraphics[width=3.5cm]{{{pngfile[0]}}}
   \item \includegraphics[width=3.5cm]{{{pngfile[3]}}}
   \item \includegraphics[width=3.5cm]{{{pngfile[2]}}}
  \end{{multi}}</li>
  \begin{{multi}}[single,points=2]
  \\ <li> A kolam can be drawn in a single line if the following holds true for the number of arms and the number of points on an arm: \item* The two numbers are coprime.
   \item There are more arms than points per arm.
   \item The difference between the number of arms and the number of points is odd.
   \item The number of arms is even, the number of points odd.
  \end{{multi}} </li></ol>
  \end{{cloze}}\newpage """)

