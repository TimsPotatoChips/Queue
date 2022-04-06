from hashlib import new


class Queue:
    front = None
    back = None
    strings = []

    def remove(self):
        if(len(self.strings) > 0):
            temp = []

            for x in range(len(self.strings)):
                if(x == 0):
                    continue

                temp.append(self.strings[x])

            self.strings = temp

        else:
            print("There is nothing to remove")

    def display(self):
        print("Queue: " + str(self.strings) + " " +
              "Length: " + str(len(self.strings)))

    def add(self, string):
        self.strings.append(string)


line = Queue()

line.add("Joe")
line.add("Jim")
line.add("Mike")
line.add("Johnny")

line.display()

line.remove()

line.display()

line.add("Joe")

line.display()
