# tableToPhylip

*tableToPhylip* is a simple Python code written to help systematists to generate species x areas input files for BioGeoBEARS.

# Usage
## A few assumptions
* You have Python 3 installed in your computer.
* The first line of your tab-delimited file contains column labels.
* The first column contains species names (or specimens), which **must not contain spaces** (you can use underscore "_" though).
* The second column contains the species ranges, comprised by one or more areas, that must be **separated using commas (",")**.
* Please, refer to the test.txt file in the example directory

## Running the code
Running the code is as simple as typing the following line in your terminal (assuming both tableToPhylip and file_name.txt are located in the working directory).

`python tableToPhyli.py <file_name.txt>`

The output should look like the test_TABLE.txt (example directory).
