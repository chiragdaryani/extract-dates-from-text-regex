# Extract Dates from News Articles

In this project, our aim is using regular expressions to locate dates from written text. We try to extract various formats of dates from news texts. The dates are categorized into two types. The first one is simple date expressions, strings like “14 June 2019” and “Fall 2020” which represent absolute points in time and are independent of when you are reading them. The second type is deictic date expressions, dates that are relative to the current time, for example, “the day before yesterday”, “next Friday”, and “two weeks prior”.


## How to Execute?

To run this project,

1. Download the repository as a zip file.
2. Extract the zip to get the project folder.
3. Open Terminal in the directory you extracted the project folder to. 
4. Change directory to the project folder using:

    `cd extract-dates-from-text-regex-main`
 
5. Now to execute the code, use the following command (in the current directory):

    `python3 src/main.py data/dev/ output/dev.csv`

## Description of the execution command

Our program **src/main.py** that takes two positional command-line arguments in this order: the first is a path to the data directory, and the second is the path to the output CSV file. 

For our project, the input dataset which is a collection of news articles is stored in the directory [data/dev](data/dev).
The final output is written in a file 'dev.csv' inside the output folder [output/dev.csv](output/dev.csv)

So we'll specify these two paths and our final execution command becomes:

**python3 src/main.py data/dev/ output/dev.csv**

## References

https://regex101.com/

https://www.w3schools.com/python/python_regex.asp

https://www.programiz.com/python-programming/writing-csv-files

https://www.dataquest.io/blog/regular-expressions-data-scientists/

https://stackoverflow.com/questions/10804732/difference-between-and

https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285

https://machinelearningabc.medium.com/how-to-extract-date-information-from-a-string-with-python-basic-nlp-in-3-minutes-8bd90381159e
