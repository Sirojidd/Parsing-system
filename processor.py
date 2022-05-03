import os

import nltk
import numpy as np
from nltk.parse.corenlp import CoreNLPParser
from nltk.parse.corenlp import CoreNLPServer
from nltk.tree.prettyprinter import TreePrettyPrinter

os.environ['JAVAHOME'] = "C:/Program Files/Java/jre1.8.0_321/bin/java.exe"

server = CoreNLPServer(
    os.path.join("stanford", "stanford-corenlp-4.4.0.jar"),
    os.path.join("stanford", "stanford-corenlp-4.4.0-models.jar"),
)


class Tree:
    def __init__(self, pdf):
        self.lines = np.array([], dtype=str)
        self.__make_lines(str(pdf))

    def __make_lines(self, pdf):
        tokenizer = nltk.tokenize.PunktSentenceTokenizer()
        tokenized = tokenizer.tokenize(str(pdf))
        for line in tokenized:
            line = line.replace("\n", "")
            self.lines = np.append(self.lines, np.array([line], dtype=str))

    @staticmethod
    def __make_trees(string):
        parser = CoreNLPParser()
        parse = next(parser.raw_parse(string))
        result = TreePrettyPrinter(parse)

        # parser = CoreNLPDependencyParser()
        # parse = next(parser.raw_parse(string))
        # result = str(result) + "\n" + str(parse) + "\n"

        return result

    def get_lines(self):
        string = ""
        for counter, line in enumerate(self.lines):
            string = string + str(counter + 1) + ". " + line + "\n"
        return str(string) + "\n"

    def get_tree(self, number):
        if number != 0:
            return self.__make_trees(self.lines[number - 1])
        elif number == 0:
            return self.get_lines()
        else:
            pass
