# python-latex-moodle-quiz
These are some examples/templates for batch generating parameterized moodle quiz questions (includig both cloze and essay type questions) using the `moodle` and `python` packages for LaTeX.

Prerequisites
=============

1. LaTeX installed and working
1. Python (>=3.6) installed and working
1. LaTeX packages installed and working:
   1. `moodle` see https://ctan.org/pkg/moodle
   1. `python` see https://github.com/brotchie/python-sty
   
Basic Usage
===========

1. Familiarize yourself with the documentation of the `moodle` package, which can be found here: http://mirrors.ctan.org/macros/latex/contrib/moodle/moodle.pdf
1. Open and edit any of the example .tex files in your favourite LaTeX-Editor.
1. Compile the file with `pdflatex`.
1. You will get an intermediate .py file, a .pdf file and a -moodle.xml file as a result (and possibly some additional .png files depending on what example you work with). However, for importing your questions into moodle you will only need the -moodle.xml file.
1. Import the -moodle.xml file file to your question bank within moodle. If not specified otherwise, all questions will be stored inside a category which is named according to the quiz title used in the respective .tex file.
1. Create a quiz activity and choose a random question from the respective category.

How this works
==============

The basic structure of any of the examples is constructed like this:

1. You have got your standard LaTeX document (header, body).
1. Inside the body you have a `quiz` environment, which is interpreted according to rules defined by the `moodle` package, which interprets and compiles the code into both the usual .pdf-file and an additional -moodle.xml file once `pdflatex` is invoked.
1. The quiz environment contains a `python` environment that contains at least one main `for` loop. As soon as `pdflatex` is invoked, it in turn invokes Python, which then runs through the `for` loop several times and dynamically adds a piece of LaTeX code in each of these runs, which in turn is again interpreted by `pdflatex` and compiled into moodle-xml-code.
1. The `python` envoirnment contains at least one type of questions envoirnment (multiple-choice, numerical, short answer, essay, matching, cloze, see the `moodle` package documentation for details). 
1. Each question cointains some variables which are dynamically changed with each call to the `for`loop creating a different question with each run.

