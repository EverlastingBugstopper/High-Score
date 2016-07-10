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
                    row[1] = float(row[1])
                    highScores.append(tuple(row))
                    highScores = sorted(highScores, key=itemgetter(1, 0), reverse=True)
                
            for i, score in enumerate(highScores):
                if i <= len(self.highScores) - 1:
                    self.highScores[i] = score
        except FileNotFoundError:
            print("File not found at", self.fileName)
            raise
        except IndexError:
            print("No high scores found, or inappropriate file format")
            pass
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        
    def _write_score(self, score):
        try:
            with open(self.fileName, 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(score)
        except FileNotFoundError:
            print("File not found at", self.fileName)
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise            
        
    def add_score(self, player, score):
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
        scoreInfo = (player, score)
        print(scoreInfo)

        self._write_score(scoreInfo)
        
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
