
class Greeting:
    def __init__(self):
        self.msg = []
        self.lLine = 1

    def addToMsg(self, nextMsg, post):
        self.compareLineMax()
        self.msg.append(f"{self.msg}{nextMsg}{post}")

    def phraseStatementAdd(self, phrase, statement, connector):
        fullMsg = f"{phrase}{connector} {statement}"

        self.addToMsg(fullMsg, "\n")

    def getGreeting(self):
        return "".self.msg.join()

    def resetGreeting(self):
        self.msg = []
        self.lLine = 0

    def addNewLine(self):
        self.msg.append("\n")

    def addAnotherTab(self):
        self.msg.append("\t")

    def addStatus(self, phrase, statement, connector):
        self.addAnotherTab()
        self.phraseStatementAdd(phrase, statement, connector)

    def compareLineMax(self, newMsg):
        if self.lLine < len(newMsg):
            self.lLine = len(newMsg)

    def addSeperator(self, symbol, post):
        seperator = []
        for i in range(0, self.lLine):
            seperator.append(symbol)

        self.addToMsg("".seperator.join(), post)
