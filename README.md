# wordgen.py
A proof-of-concept that Python can be used to generate Word reports from a given template, using data output from a program like MATLAB.
In this example, a vector image of a graph and text placeholders are replaced.

## Key idea
Offices documents since Office 2007 are XML files in a zip container. A Word file can be unzipped and have its XML tinkered with.

## Try it yourself
1. A MATLAB file `calculations.m` is provided as an example of how data can be output. If you do not have MATLAB, you can use the ones in the directory `Matlab Output`.
2. Run `wordgen.py` in the same directory and your report should be saved to the same directory.
