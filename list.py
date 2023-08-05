class MyCustomList:
  def __init__(self, name):
    self.name = name
    self.myList = []

  def myListName(self):
    print("Hello my custom list name is " + self.name)

  def addElementAtLast(self,element):
  	print("Adding element",element, "at the last position")
  	self.myList.append(element)

  def addElementAtPos(self,index,element):
  	print("Adding element",element, "at position ",index)
  	self.myList.insert(index-1,element)
  	
  def displayMyListElement(self):
  	print("My list elements are: ", self.myList)

  def reverseMyList(self):
  	print("Reversing my list")
  	self.myList.reverse()
  	
  def removeElementFromListAtPos(self,pos):
  	print("Remvoing following element " ,self.myList[pos-1])
  	self.myList.pop(pos-1)
  	
  def printLenOfList(self):
  	print("Length of my list is ",len(self.myList))
  	
  def appendNewListAtEnd(self,list):
  	print("Adding following list",list,"at the end of my current list",self.myList)
  	self.myList = self.myList + list

p1 = MyCustomList("List1")
p1.myListName()

p1.addElementAtLast("One")
p1.addElementAtLast("Three")
p1.addElementAtLast("Four")

p1.displayMyListElement()

p1.addElementAtPos(2,"Two")
p1.displayMyListElement()

p1.reverseMyList()
p1.displayMyListElement()

p1.removeElementFromListAtPos(2)
p1.displayMyListElement()

p1.printLenOfList()

p1.appendNewListAtEnd(["Ten","Eleven"])
p1.displayMyListElement()
