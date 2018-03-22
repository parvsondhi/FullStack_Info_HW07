import pymongo

#gets you the handler on the mongo client
client = pymongo.MongoClient()
#choose the data base
db = client.megalab

# Choose Collection
def chooseCollection(collectionChoice):
	collection = db['collectionChoice']

### Users ###

# Insert value
def insertUser(email, username, password, first, last):
	collection.insert({"Email":email, "Username":username, "Password":password, "First":first, "Last" :last})


# Update field
def updateUser(field, value):
	#???
	pass

# Append to field
def updateUser(field, value):
	#???
	pass

def display():
	return collection

### Trips ###

# Insert value
def insertTrip(collection, title, destination, participants):
	collection.insert({"Title":title, "Destination":destination, "Participants":participants})

# Find instance by username
def findTrips(collection, username):
	trips = collection.find({'username':username})
	return trips
