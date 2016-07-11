from classes.highscore import HighScores
import os

def main():
	try:
	    directory = 'data' # path to directory containing data file
	    file = 'highscore.csv' # name of the file located in above directory
	    fileName = os.path.abspath('%s/%s' % (directory, file))
	    hs = HighScores(fileName, 10)
	    print(hs)
	    hs.add_score("testaddition2", 340)
	    print(hs)
	except FileNotFoundError:
		print("File not found at %s" % (fileName))
		raise
	except:
		print("Unexpected error")
		raise

if __name__ == '__main__':
    main()
