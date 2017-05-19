import sys

from src.tracker import tracker

def main():
	hp = {"z_lr":0.006}
	evaluation = {"video": "vot2014_ball"}
	run = {"visualization":1,"debug":0}
	tracker(hp, evaluation, run)

if __name__ == '__main__':
    sys.exit(main())	