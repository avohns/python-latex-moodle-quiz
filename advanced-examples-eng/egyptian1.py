def egyptian(c,d):
  i=1
  j=2
  L=[]
  K=[]
  print(r"$$\begin{array}{rrr}")
  a=c
  b=d
  rest1=a
  zeile=0
  while i<=a:
    L.append([i,i*b,zeile])
    rest1-=i
    i=10*i
    zeile+=1
  while j-1<=rest1:
    L.append([j,j*b,zeile])
    j=2*j
    rest=rest1
    zeile+=1
  rest=a
  L.sort(key=lambda x: int(x[0]))
  for i in range(0,len(L)):
    if rest>=L[len(L)-1-i][0]:
      z=L[len(L)-1-i][0]
      L[len(L)-1-i][0]='/ &'+str(L[len(L)-1-i][0])
      rest=rest-z
    else:
      L[len(L)-1-i][0]=' & '+str(L[len(L)-1-i][0])
  L.sort(key=lambda x: int(x[2]))
  for i in range(0,len(L)):
    print(L[i][0],' & ',L[i][1],r"\\")
    if (L[i][0]).find('/')!=-1:
      K.append(L[i][1])

  print("\hline")

  print(" &",a," & ",sum(K))
  print(r"\end{array}$$ ")
  return('')
auswahl1=[[659,15],[479,18]]
auswahl2=[
  [1219,23],[1007,19],[1127,23],[1073,37]]
c=0
for y in auswahl1:
  for x in auswahl2:
    c+=1
    print(r"\begin{essay}[points=6, response format=html, response field lines=20, template={<h2>Part a.):</h2><p>","<span style=\"font-size: medium;\">",r"(Write down your solution here)<br><br></span></p><h2>Part b.):</h2>","<p><span style=\"font-family: \'courier new\', courier, monospace; font-size: medium;\">/1&nbsp;&nbsp;&nbsp;&nbsp;",x[1],"<br>(Write down the intermediate steps here)<br>--------<br>&nbsp;",x[0]//x[1],"&nbsp;",x[0],r"</span></p><h2>Part c.):</h2><p>","<span style=\"font-size: medium;\">",r"(Write down your solution here)<br><br></span></p>}]{Egytian Calculations (",c,r")}",sep='')
    print(rf"""
    \textbf{{Ancient Egytian Calculations}}\\<ol type=a><li>
    Use the following example to explain how the ancient Egyptian method of multiplying two numbers (in this case: ${y[1]}\cdot{y[0]}$) works.
    {egyptian(y[1],y[0])}
    </li>\\
    <li>
    Using the ancient Egyptian method, solve the division task ${x[0]}:{x[1]}$.
    The first and last line of the solution is already given below.
    </li>\\
    <li>
    Using $180:27$ as an example, explain why not all division tasks can be solved in this way, even if you allow unit fractions in the form $\frac{{1}}{{2^n}}$.
    </li></ol>\\
    \item This task has to be corrected manually, sorry!
    \end{{essay}}""")
    if c%2==0 and c<8:
      print(r"\newpage")
    else:
      print(r" \bigskip \,\\ \medskip ")

