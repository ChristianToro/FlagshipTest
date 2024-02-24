 # WORD SCRAPER 3000

This repository contains Python scripts to complete two separate tasks. The `complaint.py` file collects all unique words from a given text file, sorts them alphabetically, and then prints the sorted list of words. The `remonstration.py` file catalogues words and their frequencies from a text file, displaying each word along with how many times it appears in the document. It's particularly useful for textual analysis, vocabulary collection, or as a foundational tool for more complex text processing tasks.



 ## PROJECT DESCRIPTION


The scripts prompt the user to enter the name of a text file. If no file name is entered, it defaults to shakespeare.txt to showcase the functionality of the .py files. It then reads the file, line by line, splits each line into words, and and either collects a list of unique words or creates a dictionary of each word with its frequency in the file. A dictionary is a datatype within python where data is stored in key:value pairs.


 ## GETTING STARTED


Prerequisites
- Python 3.12.2


Running the Script

- Ensure you have Python installed on your machine
- Place the script in a directory with the text files you want to process. There are free resources to convert files to .txt format, such as [Convert documents to .txt](https://document.online-convert.com/convert-to-txt "@embed")
- Run the script using a command-line interface or source code editor:
-      python complaint.py

-  When prompted, enter the name of the text file you wish to process. If you press Enter without typing a file name, the script will default to processing `shakespeare.txt`

 ## Conclusion

 Both scripts provide valuable insights into the composition of text files by either sorting words alphabetically or by counting their occurrences.









