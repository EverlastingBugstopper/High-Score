import csv
from operator import itemgetter
import sys

class HighScores:
    def __init__(self, fileName, amount):
        self.fileName = fileName
        self.highScores = [None] * amount
        self._parse_file()
        
    def _parse_file(self):
        try:
            with open(self.fileName, 'rt') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            
                highScores = []
                for row in reader:
                    row[1] = int(row[1])
                    highScores.append(tuple(row))
                    highScores = sorted(highScores, key=itemgetter(1, 0), reverse=True)
                
            for i, score in enumerate(highScores):
                if i <= len(self.highScores) - 1:
                    self.highScores[i] = score
        except FileNotFoundError:
            print("File not found at", self.fileName)
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        
    def __str__(self):
        string = "File Name: %s\n\nAmount of High Scores: %s\n" % (self.fileName, len(self.highScores))
        for score in self.highScores:
            try:
                string += "\n" + str(score[0]) + ": " + str(score[1])
            except TypeError:
                if score is not None:
                    print("Unexpected type error:", sys.exc_info()[0])
                    raise
                else:
                    pass
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise
        return string
