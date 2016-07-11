import csv
from operator import itemgetter
import sys

class HighScores:
    def __init__(self, fileName, amount, trim = False, sort = True):
        self.fileName = fileName
        self.allScores = []
        self.highScores = [None] * amount
        self._parse_file()
        self.trim = trim
        self.sort = sort
        
    def _parse_file(self):
        try:
            with open(self.fileName, 'rt') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')

                self.allScores = []
                for row in reader:
                    self.add_score(row[0], float(row[1]), write = False)
                
            for i, score in enumerate(self.allScores):
                if i <= len(self.highScores) - 1:
                    self.highScores[i] = score
        except FileNotFoundError:
            print("File not found at", self.fileName)
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
                for row in self.allScores:
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
        temp = sorted(self.allScores, key=itemgetter(1, 0), reverse=True)
        if (write):
            self._write_scores()
        
    def __str__(self):
        self._parse_file()
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
