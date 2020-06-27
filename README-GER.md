# python-latex-moodle-quiz

Hier finden Sie einige Beispiele/Vorlagen zur Batch-Erzeugung parametrisierter Fragen (inklusive Lückentext- und Freitext-Fragen) für die Test-Aktivität in Moodle, die die Paketen`moodle` und `python` für LaTeX nutzen.

[Switch to the English version of this README](https://github.com/avohns/python-latex-moodle-quiz)

Voraussetzungen
===============

1. Eine lauffähige LaTeX-Installation
1. Eine lauffähige Installation von Python (>=3.6)
1. Die folgenden Pakete müssen für LaTeX installiert sein:
   1. `moodle` see https://ctan.org/pkg/moodle
   1. `python` see https://github.com/brotchie/python-sty
1. Wenn Sie in irgendeiner Art Bilder (statisch, dynamisch) einbinden wollen, dann benötigen Sie eine lauffähige Installation von [ImageMagick](https://imagemagick.org/index.php).
   
Benutzung/Workflow
==================

Die Ordner `simple-examples-ger` und `simple-examples-eng` enthalten einfache Demonstrationen/Minimalbeispiele (in englischer bzw. deutscher Sprache), die `àdvanced-examples-`-Ordner enthalten einige praktisch in meiner Tätgkeit in der Mathematiklehrerbildung eingesetzte Fallbeispiele.

1. Machen Sie sich mit der Dokumentation des Paketes `moodle` vertraut, die Sie [hier](http://mirrors.ctan.org/macros/latex/contrib/moodle/moodle.pdf) finden können.
1. Öffnen und bearbeiten Sie eines der TeX-Beispieldokumente in ihrem bevorzugten LaTeX-Editor.
1. Kompilieren Sie die Datei mit `pdflatex`.
1. Sie erhalten als Ergebnis eine intermediäre .py-Datei, eine .pdf-Datei und eine -moodle.xml Datei (und je nach Beispiel u.U. auch noch einige .png-Dateien). Für den Import nach Moodle benötigen Sie allerdings nur die -moodle.xml Datei.
1. Importieren Sie die -moodle.xml Datei in Ihre Fragensammlung in Moodle. Falls nicht anders angegeben, werden alle Fragen automatisch in eine neue Kategorie importiert, deren Name mit dem Titel des Quizzes in der .tex-Datei übereinstimmt.
1. Create a quiz activity and choose a random question from the respective category.

Wie das Ganze funktioniert
==========================

Die grundlegende Struktur aller Beispiele schaut in etwas so aus:

1. Wir haben eine gewöhnliche LaTeX Datei mit Header und Body.
1. Im Header sollten die beiden genannten Pakete aufgerufen werden, zusätzlich noch das T1 Font-Encoding, falls Sie rohes HTML in die Datei schreiben wollen, und `graphicx`, wenn Sie Bilder verwenden möchten (s. unten):
    ```latex 
    \usepackage[T1]{fontenc}
	\usepackage{graphicx}
    \usepackage{moodle}
    \usepackage{python}
    ```
1. Innerhalb des Bodys haben wir eine `quiz`-Umgebung (s. Beispiel unten), welche beim Kompilieren mit `pdflatex` durch das `moodle`-Paket interpretiert wird und neben der gewohnten .pdf-Datei zusätzlich eine -moodle.xml-Datei erzeugt.
    ```latex
    \begin{quiz}{quiz title}
      ...
    \end{quiz}
    ```
1. Die `quiz`-Umgebung enthät ihrerseits eine `python`-Umgebung, die wenigstens eine zentrale `for`-Schleife enthält (s. Beispiel unten). Sobald `pdflatex` aufgerufen wird, ruft dieses nun seinerseits Python auf, welches mehrfach durch die `for`-Schleife iteriert und dabei in jeder Iteration dynamisch ein Stück LaTeX-Code ergänzt, das dann wieder durch `pdflatex`interpretiert und in die .pdf- und -moodle.xml-Datei integriert wird.
    ```latex
    \begin{python}
    for x in range(2,10):
      ...
    \end{python}
    ```
1. Die `for`-Schleife enthält wenigstens einen `print`-Befehl mit einem Multiline-f-String, der wenigstens eine Fragenumgebung enthält (Multiple-Choice, Numerisch (s. Beispiel unten), Kurzantwort, Freitext, Zuordnung, Lückentext (Cloze), vgl. Abschnitt 3 der Dokumentation des `moodle`-Paketes für weitere Details). 
    ```python
    print(rf"""\begin{{numerical}}
      ${x} + {y} =$
      \item {x+y} 
    \end{{numerical}}""")
    ```
1. Jede der Fragen enthält einige Variablen (z.B. `x`und `y`im Beispiel oben), für welche mit jedem Durchlauf der `for`-Schleife verschiedene Werte eingesetzt werden, was mit jedem Durchlauf eine neue Frage erzeugt.

Bekannte Einschränkungen
========================

Einschränkungen der übersetzen LaTeX Befehle
--------------------------------------------

Die Anzahl der LaTeX-Befehle, welche bei Erzeugung der -moodle.xml-Datei in entsprechende HTML Tags umgewandelt werden ist beschränkt (Details können der Abschnitt 4 der Dokumentation des Paketes `moodle` entnommen werden). 

Wenn Sie weitere HTML Tags etwa für Layout-Zwecke (etwas: Listen, Tabellen) nutzen wollen, können Sie diese direkt als HTML-Code eingeben. Leider erscheint dieser rohe HTML-Code dann auch uninterpretiert in der erzeugten PDF-Datei.

Grafiken
--------

Es ist sowohl möglich statiosche, vorab erstellte Bilder wie auch dynamische, zur Laufzeit etwa via `python` erstellte Bilder einzubinden (es kann auch tikZ aufgerufen werden). Alle einzubindenden Bilder werden in .png-Dateien umgewandelt, die dann ihrerseits während der Kompilierung base64-codiert und direkt in die -moodle.xml-Datei eingebettet werden.

Sie sollten die Abmessungen der Grafik (Breite, Höhe in cm oder inch) angeben und die Konvertierung basiert auf einer DPI-Einstellung (falls nicht ausdrücklich anders angegeben, wird 103 DPI als Standardwert verwendet). Details entnehmen Sie bitte Abschnitt 5 der Dokumentation des Paketes `moodle`.

Meiner Erfahrung nach empfiehlt es sich, sich von vorneherein auf .png-Dateien zu beschränken, da die Umwandlung mit ImageMagick, wie sie durch das Paket `moodle` realisiert ist, für andere Formate etwas fehleranfällig ist.


Encoding/Umlaute
----------------

Das `moodle`-Paket veträgt sich leider nicht mit UTF8-Text-Encoding. Wollen Sie Beispiele in deutscher Sprache verfassen, so muss man daher alle Umlaute (Ä, Ö, Ü, ä, ö, ü, ß) als TeX-Code eingeben (`\"A, \"O, \"U, \"a, \"o, \"u und \ss{}`).


Shuffling answers in embedded questions
---------------------------------------

Das Paket `moodle`wurde erstellt, bevor das zufällige Mischen von Antworten für Teilfragen einer Lückentext-(Cloze)-Frage in Moodle (>= 3.0) eingeführt wurde 

Wenn Sie zufällig gemischte Antworten für Teilfragen einer Lückentext-(Cloze)-Frage verwenden möchte, müssen Sie irgendwo unterhalb der `quiz`-Umgebung eine weitere `python`-Umgebung in das LaTeX-Dokument aufnehmen, die dann direkt den Fragetyp innerhalb der XML-Datei verändert (Details können Sie der Seite https://bit.ly/2ZdpIpw entnehmen).

Nehmen wir einmal an, ihre XML-Datei ist z.B. `example-moodle.xml`und wir haben eine Frage vom Typus `MULICHOICE`. Wir müssen dann jedes Auftreten von `MULICHOICE` durch `MULTICHOICE_S` ersetzen, was z.B. mit dem folgenden Code-Schnippsel möglich ist:
```python
with open("example-moodle.xml", "rt") as fin:
  with open("example-shuffled-moodle.xml", "wt") as fout:
    for line in fin:
      fout.write(line.replace('MULTICHOICE:', 'MULTICHOICE_S:'))
```

Limitations inherited from the usable question types
----------------------------------------------------

As the `moodle` package only uses standard moodle question types, the generated questions should be useable on any moodle installation, there are no additional plugins required whatsoever (the MathML filter should be set to active in your moodle installation if you want to display formulas written in TeX code).

These question types come with their own set of limitations. For STEM subjects you might want to check answers for algebraic equivalence, which is simply not possible with these question types. You might want to check out the [STACK](https://moodle.org/plugins/qtype_stack) or [WIRIS](https://moodle.org/plugins/view.php?id=26) plugins for such purposes.


