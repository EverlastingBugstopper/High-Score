from classes.highscore import HighScores
import os

def main():
    directory = 'data' #path to directory containing data file
    file = 'highscore.csv' #name of the file located in above directory
    fileName = os.path.dirname(__file__) + os.path.normpath('/%s/%s' % (directory, file))
    hs = HighScores(fileName, 10)
    print(hs)

if __name__ == '__main__':
    main()
