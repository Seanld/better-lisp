# BetterLISP

A new dialect of LISP to make writing LISP code easier, and less annoying. It has more intuitive syntax and keywords that are easier to remember.

This dialect of LISP does *not* compile to machine-dependent executable binaries, but rather code for my [VM](https://github.com/Seanld/vm).

You can run this compiled VM code if you've installed the runtime for it (grab it over at the afore-linked repository).

## Running

BetterLISP is currently still in early alpha development. _Very_ early alpha. But if you want to try running one of the test source code programs, just type:

```sh
$ python bl.py tests/helloworld.lisp
```

And depending on the state of the project, it should operate on that file's source code. The goal is to get it to eventually generate bytecode in a separate file that can be executed using https://github.com/Seanld/vm, but that's going to take a while.

Side note: The aforementioned VM project is _also_ in very early alpha, so please don't laugh at me. It will only get better - I promise. I'm planning on re-writing it in C++ (because we all know running a VM in Python is Satan), but only once I figure out the overall structure of it in Python.

## Project Structure

- **bl.py**: The main compiler tool for BetterLISP. Used in the command-line as `python bl.py <betterlisp-program>`; can also be used when put into PATH, and then running `bl <betterlisp-program>`.
- **tokenizer.py**: Handles the generating of tokens from the source code. This is the first step in compilation.
- **syntaxtree.py**: Handles the generating of abstract syntax trees for the source code via tokens generated in `tokenizer.py`. This is one of the final stages of compilation.
- **ast.json**: Contains a Python-compatible grammar format for assisting `syntaxtree.py` with building ASTs.