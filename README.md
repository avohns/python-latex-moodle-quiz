# python-latex-moodle-quiz
These are some examples/templates for batch generating parameterized moodle quiz questions (includig both cloze and essay type questions) using the `moodle` and `python` packages for LaTeX.

Prerequisites
=============

1. LaTeX installed and working
1. Python (>=3.6) installed and working
1. LaTeX packages installed and working:
   1. `moodle` see https://ctan.org/pkg/moodle
   1. `python` see https://github.com/brotchie/python-sty
1. If you want to include any kind of images (static, dynamic), ImageMagick has to be installed and working.
   
Basic Usage
===========

1. Familiarize yourself with the documentation of the `moodle` package, which can be found here: http://mirrors.ctan.org/macros/latex/contrib/moodle/moodle.pdf
1. Open and edit any of the example .tex files in your favourite LaTeX-Editor.
1. Compile the file with `pdflatex`.
1. You will get an intermediate .py file, a .pdf file and a -moodle.xml file as a result (and possibly some additional .png files depending on what example you work with). However, for importing your questions into moodle you will only need the -moodle.xml file.
1. Import the -moodle.xml file into your question bank within moodle. If not specified otherwise, all questions will be stored inside a category which is named according to the quiz title used in the respective .tex file.
1. Create a quiz activity and choose a random question from the respective category.

How this works
==============

The basic structure of any of the examples looks like this:

1. You have got your standard LaTeX document (header, body).
1. The header should call both packages and T1 font encoding if you want to use additional raw HTML (see below):
    ```latex 
    \usepackage[T1]{fontenc}
    \usepackage{moodle}
    \usepackage{python}
    ```
1. Inside the body you have a `quiz` environment (see example below), which is interpreted according to rules defined by the `moodle` package, which interprets and compiles the code into both the usual .pdf-file and an additional -moodle.xml file once `pdflatex` is invoked.
    ```latex
    \begin{quiz}{quiz title}
      ...
    \end{quiz}
    ```
1. The quiz environment contains a `python` environment that contains at least one main `for` loop (see example below). As soon as `pdflatex` is invoked, it in turn invokes Python, which then iterates through the `for` loop several times and dynamically adds a piece of LaTeX code in each of these iterations, which in turn is again interpreted by `pdflatex` and compiled into moodle-xml-code.
    ```latex
    \begin{python}
    for x in range(2,10):
      ...
    \end{python}
    ```
1. The `python` envoirnment contains at least one type of questions envoirnment (multiple-choice, numerical (see example below), short answer, essay, matching, embedded answers (cloze), see section 3 of the `moodle` package documentation for details). 
    ```python
    print(rf"""\begin{{numerical}}
      ${x} + {y} =$
      \item {x+y} 
    \end{{numerical}}""")
    ```
1. Each question cointains some variables (e.g. `x`and `y`in the example above) which are dynamically changed with each iteration of the `for` loop creating a different question with each iteration.

Limitations
===========

Restrictions on interpreted LaTeX commands
------------------------------------------

The set of LaTeX commands getting converted to HTML and included in the resulting -moodle.xml file is limited (please refer to section 4 of the `moodle` package documentation for details). 

If you want to use additional HTML for layout purposes (e.g. lists or tables), you can include raw HTML inside your LaTeX document. Unfortunately, the raw HTML code will also be visible in the resulting PDF document.

Graphics
--------

It is both possible to include static images and to create images dynamically using `python` (even tikZ may be invoked). Any images included will be converted into .png files, which in turn are base64 encoded and directly included into the -moodle.xml file during compilation. 

You should specify the image dimensions (width, height in either cm or inch) and the conversion depends on a dpi setting (if not defined specifically, 103 dpi will be used as a default). Please refer to section 5 of the `moodle` package documentation for more details. 

In my experience, it is advisable to strictly stick to png files, as the conversion via ImageMagick implemented by the `moodle` package is a bit prone to errors.

Shuffling answers in embedded question
--------------------------------------

The `moodle` package was written before shuffling answers was introduced for embedded questions in moodle (>= 3.0). If you want to use shuffled answers in embedded questions, you have to include another `python` environment (below the `quiz` environment inside the TeX document's body) to change the questions type directly within the -moodle.xml file (see https://docs.moodle.org/39/en/Embedded_Answers_(Cloze)_question_type#Shuffle_sub_questions for more details). Suppose our xml file is `example-moodle.xml`and we have a `MULICHOICE` question we need to change each occurence to `MULTICHOICE_S` which can be done with the following bit of code:

    ```python
    with open("example-moodle.xml", "rt") as fin:
      with open("example-shuffled-moodle.xml", "wt") as fout:
        for line in fin:
          fout.write(line.replace('MULTICHOICE:', 'MULTICHOICE_S:'))
    ```

Encoding/Umlauts
----------------

The `moodle` package does not play nicely with utf8 text encoding, when e.g. writing examples in German, you will need to write Umlauts (Ä, Ö, Ü, ä, ö, ü, ß) in code (`\"A, \"O, \"U, \"a, \"o, \"u und \ss{}`).

