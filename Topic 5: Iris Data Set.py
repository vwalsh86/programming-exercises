# Valerie Walsh
# Topic 5 Input and Output 07/03/2018
# Exercise Irish Flower Data Set
# The idea to use {:^6} came from reviewing = https://pyformat.info/ - Padding and aligning strings
# The order of the values is as per the wording of the Exercise requirements - Petal length, Petal Width, Sepal Length, Sepal Width
# Made multiple attempts to name the columns but failed, left in the coding to show my attempt - https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas

with open("data/iris.csv") as f:
    f.colums = ['Petal Length', 'Petal Width', 'Sepal Length', 'Sepal Width']
    for line in f:
        print('{:^6} {:^6} {:^6} {:^6}'.format(line.split(',')[2], line.split(',')[3], line.split(',')[0], line.split(',')[1]))
