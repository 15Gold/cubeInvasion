import random as rnd

currentDrones = []
itemsByID = ["copperHelmet","copperChestpiece",]

def genRandom3DPoint():
 tempX = rnd.randint(-100,100)
 tempY = rnd.randint(-100,100)
 tempZ = rnd.randint(-100,100)
 return Point3D(tempX,tempY,tempZ)

def findDistPoints(Point1,Point2):
  diffX = Point1.x - Point2.x
  diffY = Point1.y - Point2.y
  diffZ = Point1.z - Point2.z
  return (diffX**2 + diffY**2 + diffZ**2)**0.5)

def incomingFile(droneCount):
  incoming = open("inComing.txt" ,"w")

  for i in range(droneCount):
    temp = genRandom3DPoint()
    incoming.write(str(temp.x) + "," + str(temp.y) + "," + str(temp.z) + "\n")

  incoming.close()

def separateCoords(xyz):
  x = ""
  y = ""
  z = ""
  i = 0
  coordFinished = False
  while not coordFinished:
    if xyz[i] != ",":
      x = x + xyz[i]
      i = i + 1
    else:
      coordFinished = True
      i = i + 1
  coordFinished = False

  while not coordFinished:
    if xyz[i] != ",":
      y = y + xyz[i]
      i = i + 1
    else:
      coordFinished = True
      i = i + 1
  z = xyz[i:len(xyz)]

  x = int(x)
  y = int(y)
  z = int(z)

  return [x,y,z]

def identifyDrones():
  global currentDrones

  index = 0
  incFile = open("inComing.txt","r")

  while True:
    rawXYZ = incFile.readline()
    if rawXYZ != "" :
      coordList = separateCoords(rawXYZ)
      XYZ = Point3D(coordList[0],coordList[1],coordList[2])

      ##Determining the enemy level by distance to 0,0,0 when spawned.##
      spawnDist = XYZ.distanceFromSpawn()
      if spawnDist <= 173.20508075688772 and spawnDist >= 138.5640646055102:
        droneLevel = 4
      elif spawnDist < 138.5640646055102 and spawnDist >= 69.2820323027551:
        droneLevel = 3
      elif spawnDist < 69.2820323027551 and spawnDist >= 17.320508075688775:
        droneLevel = 2
      elif spawnDist < 17.320508075688775:
        droneLevel = 1

      currentDrones.append(Drone(XYZ,droneLevel,5,index))
      index = index + 1
    else:
      print("Drones have been identified.")
      return

class Point3D:
  def __init__(self,x,y,z):
    self.x = int(x)
    self.y = int(y)
    self.z = int(z)

  def __str__(self):
    return f"({self.x},{self.y},{self.z})"

  def distanceFromSpawn(self):
    return ((self.x*self.x + self.y*self.y + self.z*self.z)**0.5)

class Drone:
  def __init__(self,coords,level,attackRange,EntityID) :
    self.coords = coords
    self.level = level
    self.attackRange = attackRange
    self.EntityID = EntityID
    match self.level:
      case 4:
        self.dmg = 20.0
        self.hp = 200.0
      case 3:
        self.dmg = 10.0
        self.hp = 100.0
      case 2:
        self.dmg = 5.0
        self.hp = 50.0
      case 1:
        self.dmg = 1.0
        self.hp = 20.0
  def __str__(self):
    return f"My coordinates are {self.coords}. I deal {self.dmg} hitpoints of damage and I have {self.hp} hitpoints. ({self.EntityID})\n"
  def __repr__(self):
    return f"My coordinates are {self.coords}. I deal {self.dmg} hitpoints of damage and I have {self.hp} hitpoints. ({self.EntityID})\n"
  def attackPlayer():
    pass
  def moveTowardsPlayer():
    pass
  def beAttacked():
    pass

class Player:
  def __init__(self,baseHealth,baseArmour,baseAttack,meleeBoost,rangedBoost,mageBoost,equipped,inventory):
    pass

class Item:
   def __init__(self,type,ItemID):
     pass

class Consumable:
  def __init__(self,lore,effect):
    self.lore = lore

class Ingredient:
  def __init__(self,lore):
    self.lore = lore

class Armour:
  def __init__(self,role,lore,setName,setBonus,pieceBonus):
    self.role = role

class Weapon:
  def __init__(self,role,lore,enchants,baseDamage):
    pass

#point1 = Point3D(80,-78,-50)
#point2 = Point3D(79,19,26)
#print(findDistPoints(point1,point2))

incomingFile(60)
identifyDrones()
#print(currentDrones[0])

#point1 = Point3D(10,10,10)
#print(point1.distanceFromSpawn())