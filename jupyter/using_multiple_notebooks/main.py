# This is so we can import functions from other jupyter notebooks.
from ipynb_hook import NotebookLoader
nb = NotebookLoader()
nb.load_module('utils'); from utils import the_answer_to_the_ultimate_question_of_life;

print(the_answer_to_the_ultimate_question_of_life())
