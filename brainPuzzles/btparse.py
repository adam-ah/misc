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
            self.question = self.question + line + ' '

    def addAnswer(self, answer):
        if self.answer == '':
            self.answer = self.fixline(answer) 

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
        line = line.strip()
        return line

    def __init__(self, number):
        self.question = '' 
        self.answer = ''
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
    inanswers = False
    lines = content.split('\r\n')
    for line in lines:
        if re.match("^\d+\.\s$", line):
            number = int(line.replace('. ', ''))
            if number == prev + 1:
                print number
                if inanswers:
                    puzzle = puzzles[number - 1]
                else:
                    puzzle = Puzzle(number)
                    puzzles.append(puzzle)

                prev = number
        else:
            if line.startswith("aNSWerS aNSWerS "):
                inanswers = True
                prev = 0
                continue
            if inanswers:
                puzzle.addAnswer(line)
            else:
                puzzle.addLine(line)
        # print line.replace("’","'")
    # print(str.format('Length: {0}', len(puzzles)))
    # print json.dumps(puzzles[2].__dict__)
    for puzzle in puzzles:
        print json.dumps(puzzle.__dict__)

if __name__ == "__main__":
        main()
