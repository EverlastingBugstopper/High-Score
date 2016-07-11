from classes.highscore import HighScores
import os

def _debug(val):
	DEBUGGING = True # change to false to turn off debug output
	if (DEBUGGING):
		print(val)

def main():
	try:
		directory = 'data2' # path to directory containing data file
		file = 'highscore2.csv' # name of the file located in above directory
		fileName = os.path.abspath('%s/%s' % (directory, file))
		hs = HighScores(fileName, 10)
		_debug(hs)
		
		for i in range(5):
			tup = addInput()
			hs.add_score(tup[0], tup[1])
			_debug(hs)
			
	except:
		print("Unexpected error")
		raise

def addInput():
	player = input("Player name: ")
	score = input("Score: ")
	return player, score

if __name__ == '__main__':
	main()
