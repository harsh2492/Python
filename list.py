class MyCustomList:
  def __init__(self, name):
    self.name = name
    self.myList = []

  def myListName(self):
    print("Hello my custom list name is " + self.name)

  def addElementAtLast(self,element):
  	#print("Adding following list element at the last : " + element)
  	self.myList.append(element)
  	#print(self.myList)
  
  def addElementAtPos(self,index,element):
  	self.myList.insert(index-1,element)
  	
  def displayMyListElement(self):
  	print("My list elements are: ")
  	print(self.myList)
  	
  def reverseMyList(self):
  	print("Reversing my list")
  	self.myList.reverse()
  	
  def removeElementFromListAtPos(self,pos):
  	print("Remvoing following element " + self.myList[pos-1])
  	self.myList.pop(pos-1)
  	
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
