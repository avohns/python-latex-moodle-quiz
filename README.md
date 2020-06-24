# python-latex-moodle-quiz
This is just a bunch of examples/templates for batch generating parameterized moodle quiz questions (includig both cloze and essay type questions) using the `moodle` and `python` packages for LaTeX.

Prerequisites
=============

1. TeX installed and working
1. Python (>=3.6) installed and working
1. LaTeX packages installed and working:
   1. `moodle` see https://ctan.org/pkg/moodle
   1. `python` see https://github.com/brotchie/python-sty
   
Basic Usage
===========

1. Open and edit any of the example files in your favourite LaTeX-Editor.
1. Compile the file with `pdflatex`.
1. You will get both a PDF and a Moodle-XML file as a result.
1. Import the Moodle-XML file to your question bank in moodle. If not chosen otherwise, all questions will be stored inside a category which is named according to the quiz title inside the TeX file.

How does this work?
===================

-- to be continued --


