class Classy(object):
    def __init__(self):
        self.items = []

    def getClassiness(self):

        total = 0
        for item in self.items:
            if item == 'tophat':
                total += 2
            elif item == 'bowtie':
                total += 4
            elif item == 'monocle':
                total += 5
        
        return total

    def addItem(self, item):
        self.items.append(item)

# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()