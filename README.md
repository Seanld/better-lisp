# BetterLISP

*A **better**, simpler **LISP**.*

This is a project aimed at developing a compiler for my own dialect of LISP, that generates bytecode for a VM I personally designed (located right [here](https://github.com/Seanld/vm)). 

## Why?

A few reasons, actually:

### Simplicity

Writing LISP code can get daunting very quickly. But BetterLISP has easier-to-remember keywords and names for things like constants, built-in procedures, and many other things.

### Builtins

Not only that, but it will also include many useful built-in modules that assist with everything from networking, to advanced mathematical operations.

### Higher-level Syntax

While LISP is considered a high-level language, it's still very raw. You're essentially writing an abstract syntax tree *for* the compiler, so it doesn't even have to do the dirty work. And, as you may be aware, the easier it is for a computer to understand something, the harder it will likely be for *you* to understand it.

To combat this, BetterLISP makes some minor, yet handy changes, such as:

- No namespaces! C++ can get very annoying when trying to separate namespaces, so we made sure conflictions stay at a minimum by inheriting a Python-like module approach. Importing of modules is done by a pre-processor statement (much like C++), but then *accessing* that module is done by writing `module.function`, where `module` is the name of the imported module, and `function` is the name of the function that the module contains that you want to use.

- Easier basic math operations. Instead of doing `(PLUS 2 3)`, or `(ADD 2 3)`, just write `(+ 2 3)`. This makes it easier on the compiler, and sensical for you.

As well as other features that are in development, and yet to be added.

## Installation

Simply clone or download this repository, and then run the `install.sh` script. This will perform the installation, and you'll be set!

## WARNING!

This compiler is *very* naive. This is my first compiler project. Because it's my first, it's going to be buggy, slow, and there will be quite a few unnecessary pieces of code with unnecessary implementations and algorithms.

The bright side is that the only direction this project can go is up. Just be patient.

Enjoy.