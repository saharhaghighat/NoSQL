from pymongo import MongoClient, ASCENDING, DESCENDING

client = MongoClient("mongodb://localhost:27017/")

db = client["newDatabase"]
collection = db["users"]

#  Queries


# Find all documents
find_all_documents = collection.find()
print("The list of all documents is:", list(find_all_documents))

# Find documents where age == 19
filtered_result = collection.find({"age": 19})
print("Filtered documents with age of 19:", list(filtered_result))


# Projection
projection_query = collection.find({"age": 19}, {"name": 1, "_id": 0})
print("Result of projection query:", list(projection_query))

# Find one document where age == 19
find_one_document = collection.find_one({"age": 19})
print("The first result is:", find_one_document)


# Limiting
limit_query = collection.find().limit(2)
print("The limited query result is:", list(limit_query))

# Pagination
pagination_query = collection.find().skip(1).limit(2)
print("The pagination query result is:", list(pagination_query))



# Ascending sort
ascending_sort = collection.find().sort("age", ASCENDING)
print('Ascending sort:', list(ascending_sort), end='\n\n')

# Descending sort
descending_sort = collection.find().sort("age", DESCENDING)
print('Descending sort:', list(descending_sort), end='\n\n')

# Sort by multiple fields
cursor_multiple = collection.find().sort([
    ("age", ASCENDING),
    ("name", DESCENDING)
])
print("Sort by 'age' and 'name':", list(cursor_multiple))



client.close()





