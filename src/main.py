import os
import re
import csv
import argparse

# Initialize the argument parser
parser = argparse.ArgumentParser()

# Add the parameters we will pass from cli
parser.add_argument('data_dir_path',help='path to the data directory')
parser.add_argument('output_csv_path',help='path to the output CSV file')

# Parse the arguments
args = parser.parse_args() 
#print(args)

# Path to directory containing all text files
data_dir_path= args.data_dir_path
# Path to output csv file
output_csv_path= args.output_csv_path











''' This regex extract dates of the format dd-mm-yyyy, dd-mm-yy, mm-dd-yyyy, mm-dd-yy, d-m-yy, d-m-yyyy etc. '''

def extractDateFormat1_updated(content, fileName, listOfDetections):
                            
                            re1 = re.compile(r'(?i)\d{1,2}-\d{1,2}-\d{2,4}')
                            re1_type = "dd-mm-yyyy"
                            
                            for m in re1.finditer(content):
                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re1_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections
                            




''' This regex will extract dates of the format dd/mm/yyyy, dd/mm/yy, mm/dd/yyyy, mm/dd/yy, d/m/yy, d/m/yyy etc. '''

def extractDateFormat2_updated(content, fileName, listOfDetections):

                        
                            re2 = re.compile(r'(?i)\d{1,2}\/\d{1,2}\/\d{2,4}')
                            re2_type = "dd/mm/yyyy"
                            
                            for m in re2.finditer(content):
                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re2_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections
                            
                            




''' 
This regex will extract dates where the month (in middle) is written in words. E.g. 21 Mar 2020, 7 Dec 2020, 15 Oct 20, 15 October 2020 etc. 
It will also extract date where the month (in words) is at the beginning. E.g. Nov 5, 2020, March 5, 1998 
'''

def extractDateFormat3_updated(content, fileName, listOfDetections):


                           
                            re3 = re.compile(r'(?i)(?:\d{1,2} )?(?:Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{1,2}, )?\d{2,4}')
                            # Reference: https://stackoverflow.com/questions/10804732/difference-between-and

                            re3_type = "day month year/ month day year"
                            
                            for m in re3.finditer(content):
                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re3_type, m.group(), m.start()])
                            
                            #print(listOfDetections)
                            return listOfDetections
                            





''' This regex will extract dates which have a ',' after the name of the month.  E.g. 24 November, 2020 '''

def extractDateFormat4_updated(content, fileName, listOfDetections):

                        
                            re4 = re.compile(r'(?i)\d{1,2} (?:Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*,+ \d{2,4}')
                            re4_type = "day month year"
                            
                            for m in re4.finditer(content):
                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re4_type, m.group(), m.start()])
                            
                            #print(listOfDetections)
                            return listOfDetections
                            
                            



''' This regex will help us extract Deitic Date Expressions like season and year. E.g. Fall 2021, Summer 69, Winter 19, Fall of 2020 '''

def extractDateFormat5_updated(content, fileName, listOfDetections):

                            re5 = re.compile(r'(?i)((?:Fall|Summer|Autumn|Winter|Spring)\s(of)?\s?\d{2,4})')
                            re5_type = "Season year or Season of year"
                            
                            for m in re5.finditer(content):
                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re5_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections
                            
                            



''' It will help us identify Deictic Date Expressions like this monday, next friday, last month, previous season, this fall, next january, this friday evening etc.
    It can also capture phrases like "next monday morning"
'''

def extractDateFormat6_updated(content, fileName, listOfDetections):

                            # It will help us identify deictic date expressions like this monday, next friday, last month, last week, last weekend etc.
                            re6 = re.compile(r'(?i)((?:next|this|last|previous|that)\s(week(end)?|month|year|season|monday|tuesday|wednesday|thursday|friday|saturday|sunday|january|february|march|april|may|june|july|august|september|october|november|december|fall|summer|winter|spring|autumn)\s?(morning|evening|afternoon|night)?)')
                            re6_type ="relative-year/month/week/season"

                            for m in re6.finditer(content):
                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re6_type, m.group(), m.start()])
                            
                            #print(listOfDetections)
                            return listOfDetections

                            



''' This regex will help us identify Deictic Date Expressions like 34 years ago,   before 20 days,    666 days etc.
    It can also match expressions like two years ago, nine months prior, before sixty years etc. 
'''

def extractDateFormat7_updated(content, fileName, listOfDetections):


                            re7 = re.compile(r'(?i)(((?:before|after)(\s))?(\w*)\s(days|months|years)\s?(ago|before|after|prior)?)')
                            re7_type ="before/after years/months/days ago/before/after"

                            for m in re7.finditer(content):

                                #print("***********")
                                #print(m.group(0))
                                #print(m.start(), m.group())
                                #print("***********")
                                
                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re7_type, m.group(), m.start()])
                            
                            #print(listOfDetections)
                            return listOfDetections





''' This regex will help us identify Deictic Date Expressions like yesterday, before tomorrow night, after today, after today evening etc. '''

def extractDateFormat8_updated(content, fileName, listOfDetections):

                            re8 = re.compile(r'(?i)(((?:after|before)(\s))?(today|tomorrow|yesterday)\s?(morning|evening|afternoon|night)?)')
                            re8_type ="relative-tomorrow/yesterday/today- timeOfDay"

                            for m in re8.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re8_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections




''' This regex will help us identify Deictic Date Expressions like 'the last 4 months', 'the last eight years'  etc. '''

                            
def extractDateFormat9_updated(content, fileName, listOfDetections):

                            re9 = re.compile(r'(?i)(the\slast\s(\w*)\s(months|years|days))')
                            re9_type ="the last xx years/months/days"

                            for m in re9.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re9_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections




''' This regex will help us identify Deictic Date Expressions like 'the day before yesterday', 'the day after tomorrow', etc. '''


def extractDateFormat10_updated(content, fileName, listOfDetections):

                            re10 = re.compile(r'(?i)((the)?\s?day\s(after|before)\s(tomorrow|yesterday))')
                            re10_type ="relative-day"

                            for m in re10.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re10_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections




''' This regex will help us identify Deictic Date Expressions like 'later this year', 'later this month', 'earlier this week', 'earlier this day' etc. '''

def extractDateFormat11_updated(content, fileName, listOfDetections):

                            re11 = re.compile(r'(?i)((earlier|later)\sthis\s(month|year|week|day))')
                            re11_type ="relative year/month/week/day"

                            for m in re11.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re11_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections





''' This regex will help us identify Deictic Date expressions like 'the 1990s', 'the 80s'  etc. '''

def extractDateFormat12_updated(content, fileName, listOfDetections):

                            re12 = re.compile(r'(?i)(the\s(\d{2,4}s))')
                            re12_type ="decade"

                            for m in re12.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re12_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections





'''This regex will help us identify Deictic Date Expressions like 'first quarter of 2004', 'second half of 2020'  etc. '''

def extractDateFormat13_updated(content, fileName, listOfDetections):

                            re13 = re.compile(r'(?i)((first|second|third|fourth|last)\s(quarter|half)\s(of)\s(\d{4}))')
                            re13_type ="quarter/half of year"

                            for m in re13.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re13_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections





'''
Match single Month name only if it is not preceded by a digit or a - AND if it is not followed by a - or space followed by digit.
This will help us extract name of months when they are used INDEPENDENTLY and not part of a date
'''
def extractDateFormat14_updated(content, fileName, listOfDetections):

    
    
                            re14 = re.compile(r'(?<!(\d|-))((January|February|March|April|May\s|June|July|August|September|October|November|December))(?!(-|\s\d))')
                            re14_type ="month"

                            for m in re14.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re14_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections


'''Match days of week like Monday, Wednesday, Friday)'''

def extractDateFormat15_updated(content, fileName, listOfDetections):

                            re15 = re.compile(r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)')
                            re15_type ="dayofweek"

                            for m in re15.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re15_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections


'''Match years like 1990, 1890 only when THEY ARE NOT FOLLOWED by s e.g. 1990s must not be matched. (we have seperate functions for matching it)'''

def extractDateFormat16_updated(content, fileName, listOfDetections):

                            re16 = re.compile(r'(\d{4})(?!s)')
                            re16_type ="year"

                            for m in re16.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re16_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections






'''Match month and year only. Like June 2001, May 1998 etc'''

def extractDateFormat17_updated(content, fileName, listOfDetections):

                            re17 = re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}')
                            re17_type ="month year"

                            for m in re17.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re17_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections


'''
Match day of month and Month name only if it is not followed by a - or space followed by digit. E.g. 11 March is to be accepted but 11 March 2001 shouldn't as we
have another function for it.
This will help us extract day of month+ name of month when they are used INDEPENDENTLY and not part of a date
'''
def extractDateFormat18_updated(content, fileName, listOfDetections):

    
    
                            re18 = re.compile(r'(\d{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December))(?!(-|\s\d))')
                            re18_type ="day month"

                            for m in re18.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re18_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections





''' This regex will help us identify Deictic Date Expressions like 'May last year', 'february this year'  etc. '''

                            
def extractDateFormat19_updated(content, fileName, listOfDetections):

                            re19 = re.compile(r'(?i)(January|February|March|April|May|June|July|August|September|October|November|December)\s(last|this)\syear')
                            re19_type ="month relative-year"

                            for m in re19.finditer(content):

                                print(m.start(), m.group())
                                listOfDetections.append([fileName, re19_type, m.group(), m.start()])

                            #print(listOfDetections)
                            return listOfDetections




'''

Main function will do the following:

1. open the output file in write mode
2. go through each input file one by one, read content of each file 
3. Apply all regular expression functions recursively on the content of each input file
4. Finally write the output in the desired format to the output file

'''

def main():

        try:

            # create the output csv file
            with open(output_csv_path, 'w', newline='') as outputFile:
                writer = csv.writer(outputFile)
                # create format for output file
                writer.writerow(["article_id", "expr_type", "value", "offset"])


                # All files in the directory sorted according to file
                files = sorted(os.listdir(data_dir_path))

                # Going through each file in the directory
                for file in files:
                    if os.path.isfile(os.path.join(data_dir_path, file)):


                        try:    


                            #opening file in read mode
                            f = open(os.path.join(data_dir_path, file),'r')

                            #print(f.name) #full file path
                            
                            #only file name with its extension
                            fileName= os.path.basename(f.name)
                            print(fileName) 

                            listOfDetections = []
                            
                            for content in f:
                                print(content)

                                # We have the content of the file. Let's apply regex on the content

                                
                                listOfDetections = extractDateFormat1_updated(content, fileName, listOfDetections)
                                

                                listOfDetections = extractDateFormat2_updated(content, fileName, listOfDetections)

                                
                                #listOfDetections = extractDateFormat3_updated(content, fileName, listOfDetections)

                                
                                listOfDetections = extractDateFormat4_updated(content, fileName, listOfDetections)


                                listOfDetections = extractDateFormat5_updated(content, fileName, listOfDetections)


                                listOfDetections = extractDateFormat6_updated(content, fileName, listOfDetections)



                                listOfDetections = extractDateFormat7_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat8_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat9_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat10_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat11_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat12_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat13_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat14_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat15_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat16_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat17_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat18_updated(content, fileName, listOfDetections)

                                listOfDetections = extractDateFormat19_updated(content, fileName, listOfDetections)








                            print(listOfDetections)

                            #write to output csv file
                            writer.writerows(listOfDetections)            
                            
                            print("======================================================================")

                            #f.close()
                        

                        except:
                            print("Something went wrong when reading the input file. We are moving to the next file!")
                            continue
                        
                        finally:
                            f.close()
        except:
                print("Something went wrong when opening the output file")



    
if __name__ == "__main__":
    main()