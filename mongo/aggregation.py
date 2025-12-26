from datetime import datetime

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["test"]
collection = db["orders"]
#
# # Aggregation pipeline
# pipeline = [
#     {
#         "$match": {
#             "orderDate": {
#                 "$gte": datetime(2025, 4, 5),
#                 "$lt":  datetime(2025, 5, 1)
#             }
#         }
#     },
#     { "$project": { "status": 1 } },
#     {
#         "$group": {
#             "_id":   "$status",
#             "count": { "$sum": 1 }
#         }
#     }
# ]
#
# cursor = collection.aggregate(pipeline)
# for doc in cursor:
#     print(doc)
#
#
#
# # Aggregation pipeline: add itemCount, then group by status
# pipeline = [
#     { "$addFields": { "itemCount": { "$size": "$items" } } },
#     { "$group": {
#         "_id": "$status",
#         "totalLineItems": { "$sum": "$itemCount" }
#     }}
# ]
#
# cursor = collection.aggregate(pipeline)
# for doc in cursor:
#     print(doc)
#
#
# # Aggregate: unwind items, sum qty per SKU, sort by units desc
# pipeline = [
#     { "$unwind": "$items" },
#     { "$group": {
#         "_id":   "$items.sku",
#         "units": { "$sum": "$items.qty" }
#     }},
#     { "$sort": { "units": -1 } }
# ]
#
# cursor = collection.aggregate(pipeline)
# for doc in cursor:
#     print(doc)
#
#
# print("-----------------------------------------------------------------")
# # Aggregate: compute revenue per SKU and sort by revenue desc
# pipeline = [
#     { "$unwind": "$items" },
#     { "$addFields": {
#         "lineTotal": { "$multiply": [ "$items.qty", "$items.price" ] }
#     }},
#     { "$group": {
#         "_id":    "$items.sku",
#         "revenue": { "$sum": "$lineTotal" }
#     }},
#     { "$sort": { "revenue": -1 } }
# ]
#
# cursor = collection.aggregate(pipeline)
# for doc in cursor:
#     print(doc)
#
# pipeline = [
#     {"$unwind": "$items"},
#     {"$group": {"_id":"$items.product",
#                 "totalSold":{"$sum":"$items.quantity"}}},
#     {"$sort":{"totalSold":-1},},
#     {"$limit":3}
#
#
# ]
#
#
# cursor = collection.aggregate(pipeline)
# for doc in cursor:
#     print(doc)

#
# pipeline =[
#     {"$unwind": "$items"},
#     {"$group":{"_id": "$items.category", "avgPrice":{"$avg":"$items.price"} }},
#     {"$sort": {"avgPrice":-1}},
# ]
# cursor = collection.aggregate(pipeline)
# for doc in cursor:
#     print(doc)

# pipeline = [
#     {"$unwind": "$items"},
#     {"$addFields":{"price": {"$multiply": ["$items.price","$items.quantity"]}}},
#     {"$group": {"_id":"$customer.region", "totalRevenue": {"$sum":"$price"}}},
#     {"$sort": {"totalRevenue":-1}}
#
# ]
# cursor = collection.aggregate(pipeline)
# for doc in cursor:
#     print(doc)

# validator

# db.createCollection("VIPCustomers", {
#   validator: {
#     $jsonSchema: {
#       bsonType: "object",
#       required: [
#         "name",
#         "email",
#         "phone_number",
#         "membership_level",
#         "points",
#         "balance",
#         "join_date",
#         "is_active"
#       ],
#       properties: {
#         name: {
#           bsonType: "string",
#           description: "Name must be a string"
#         },
#         email: {
#           bsonType: "string",
#           pattern: "^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$",
#           description: "Email must be a valid email address"
#         },
#         phone_number: {
#           bsonType: "string",
#           pattern: "^09\\d{9}$",
#           description: "Phone number must start with 09 and have 11 digits"
#         },
#         membership_level: {
#           enum: ["Gold", "Silver", "Bronze"],
#           description: "Membership level must be Gold, Silver, or Bronze"
#         },
#         points: {
#           bsonType: "int",
#           minimum: 0,
#           description: "Points must be an integer >= 0"
#         },
#         balance: {
#           bsonType: "double",
#           minimum: 0,
#           description: "Balance must be a non-negative number"
#         },
#         join_date: {
#           bsonType: "date",
#           description: "Join date must be a date"
#         },
#         is_active: {
#           bsonType: "bool",
#           description: "Is active must be boolean"
#         }
#       }
#     }
#   },
#   validationLevel: "strict",
#   validationAction: "error"
# })
