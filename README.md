# Word Wrap (Print Pretty)

The following program prints a paragraph neatly on a page. The paragraph consists of words of length l<sub>1</sub>, l<sub>2</sub>, ..., l<sub>n</sub>. The maximum line length is M (assume l<sub>i</sub> <= M always). We define a measure of neatness as follows. The extra space on a line (using one space between words) containing words l<sub>i</sub> through l<sub>j</sub> is M - j + i - S, such that S = the sum from k=i to j, l<sub>k</sub>. The penalty is the sum over all lines except the last of the cube of the extra space at the end of the line. This has proven to be an effective heuristic for neatness in practice.

`print-neatly.py` contains a dynamic programming solution to determine the neatest way to print a paragraph.

The `print_neatly` class method implements an O(nM) time and O(n) space solution.

The `print_neatly_non_optimized` class method implements a O(n<sup>2</sup>) time and space solution.
