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

1. Open and edit any of the example .tex files in your favourite LaTeX-Editor.
1. Compile the file with `pdflatex`.
1. You will get an intermediate .py file, a .pdf file and a -moodle.xml file as a result.
1. Import the -moodle.xml file file to your question bank within moodle. If not specified otherwise, all questions will be stored inside a category which is named according to the quiz title used in the respective .tex file.
1. Create a quiz activity and choose a random question from the respective category.

How does this work?
===================

-- to be continued --


