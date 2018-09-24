# BetterLISP

A new dialect of LISP to make writing LISP code easier, and less annoying. It has more intuitive syntax and keywords that are easier to remember.

This dialect of LISP does *not* compile to machine-dependent executable binaries, but rather code for my [VM](https://github.com/Seanld/vm).

You can run this compiled VM code if you've installed the runtime for it (grab it over at the afore-linked repository).

## Project Structure

- **bl.py**: The main compiler tool for BetterLISP. Used in the command-line as `python bl.py <betterlisp-program>`; can also be used when put into PATH, and then running `bl <betterlisp-program>`.
- **tokenizer.py**: Handles the generating of tokens from the source code. This is the first step in compilation.
- **syntaxtree.py**: Handles the generating of abstract syntax trees for the source code via tokens generated in `tokenizer.py`. This is one of the final stages of compilation.
- **ast.json**: Contains a Python-compatible grammar format for assisting `syntaxtree.py` with building ASTs.