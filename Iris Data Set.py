# Valerie Walsh
# Topic 5: Input and output 
# Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format.
# The idea to use {:^6} came from reviewing = https://pyformat.info/ - Padding and aligning strings
# The order of the values is as per the wording of the Exercise requirements - Petal length, Petal Width, Sepal Length, Sepal Width
# Made multiple attempts to name the columns but failed, left in the coding to show my attempt - https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas

with open("data/iris.csv") as f:
    f.colums = ['Petal Length', 'Petal Width', 'Sepal Length', 'Sepal Width']
    for line in f:
        print('{:^6} {:^6} {:^6} {:^6}'.format(line.split(',')[2], line.split(',')[3], line.split(',')[0], line.split(',')[1]))

# Made attempts to try add column names / headers but unable to resolve. I have added comments below of the additional code I have tried in order to resolve this.
# import sqlite3
# connection = sqlite3.connect('~/foo.sqlite')
# cursor = connection.execute('select * from bar')
#
# import pandas as pd
# import numpy as np
# 
# df = pd.DataFrame(f,columns=['Petal Length', 'Petal Width', 'Sepal Length', 'Sepal Width'])
#
# PRAGMA table_info(tablename);
#
# df = f.DataFrame(
#   data = [
#   ('Petal Length'),
#   ('Petal Width'),
#   ('Sepal Length')
#   ('Sepal Width')
#   ] 
# )
