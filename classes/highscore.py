import csv
from operator import itemgetter
import sys
import os

class HighScores:
    def __init__(self, fileName, amount, trim = False):
        self.fileName = fileName
        self.allScores = []
        self.amount = amount
        self._parse_file()
        self.trim = trim
        
    def _parse_file(self):
        try:
            if (os.path.isfile(self.fileName)):
                openType = 'rt'
            else:
                openType = 'w+'
            with open(self.fileName, openType) as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')

                self.allScores = []
                for row in reader:
                    self.add_score(row[0], float(row[1]), write = False)
                
            for i, score in enumerate(self.allScores):
                if i <= len(self.allScores) - 1:
                    self.allScores[i] = score
                    
        except FileNotFoundError:
            print("Directory of", self.fileName, "not found.")
            raise
        except IndexError:
            print("No high scores found, or inappropriate file format")
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise        
        
    def _write_scores(self):
        try:
            with open(self.fileName, 'w', newline='\n') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                for i, row in enumerate(self.allScores):
                    if ((not self.trim) or i < self.amount):
                        data = [[row[0], row[1]]]
                        writer.writerows(data)
        except FileNotFoundError:
            print("File not found at", self.fileName)
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise            
        
    def add_score(self, player, score, write = True):
        try:
            player = str(player)
        except:
            print("Player needs to be string:", sys.exc_info()[0])
            raise

        try:
            score = float(score)
        except:
            print("Score could not be converted to a float.")
            raise
        
        self.allScores.append(tuple((player, score)))
        self._sort()
        if (write):
            self._write_scores()

    def _sort(self):
        self.allScores = sorted(self.allScores, key = itemgetter(1, 0), reverse = True)
        
    def __str__(self):
        self._parse_file()
        if (self.amount < len(self.allScores)):
            amount = self.amount
        else:
            amount = len(self.allScores)
        string = "File Name: %s\n\nAmount of High Scores: %s\n" % (self.fileName, amount)
        for i, score in enumerate(self.allScores):
            try:
                if (i < self.amount):
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
