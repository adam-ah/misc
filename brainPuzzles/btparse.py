# -*- coding: UTF-8 -*-
import re
import json

class Puzzle:
    def addLine(self, line):
        if len(line.strip()) <= 1:
            return
        line = self.fixline(line)

        if re.match("^\([a-z]\) ", line):
            self.choices.append(line)
        else:
            self.question = self.question + line.strip() + ' '

    def fixline(self, line):
        line = line.replace('\x92',"'")
        line = line.replace('\x93','"')
        line = line.replace('\x94','"')
        line = line.replace('\xd7','*')
        line = line.replace('\x85',':')
        line = line.replace('\x96','-')
        line = line.replace('\xb0','deg')
        line = line.replace('\xba','deg')
        line = line.replace('\xb4',"'")
        line = line.replace('\x97',"-")
        return line

    def __init__(self, number):
        self.question = '' 
        self.choices = []
        self.number = number
        pass

    def __str__(self):
        return str.format('{0} {1} {2}', self.number, self.question, self.choices)

def main():
    prev = 0
    puzzles = []
    puzzle = Puzzle(0)
    f = open('bt.txt')
    content = f.read()
    lines = content.split('\r\n')
    for line in lines:
        if re.match("^\d+\.\s$", line):
            number = int(line.replace('. ', ''))
            if number == prev + 1:
                puzzle = Puzzle(number)
                puzzles.append(puzzle)
                print number
                prev = number
        else:
            if line.startswith("aNSWerS aNSWerS "):
                break
            puzzle.addLine(line)
        # print line.replace("’","'")
    # print(str.format('Length: {0}', len(puzzles)))
    for puzzle in puzzles:
        print json.dumps(puzzle.__dict__)

if __name__ == "__main__":
        main()
