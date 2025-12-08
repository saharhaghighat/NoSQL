const { MongoClient } = require("mongodb");

const client = new MongoClient("mongodb://localhost:27017");

async function run() {
  await client.connect();
  const db = client.db("newDatabase");
  const orders = db.collection("orders");

  // Query 1
  orders.find({price: {$gt: 1500}}).toArray();

  // Query 2
  orders.find({items: "watch"}).toArray();

  // Query 3
  orders.find({
      city: "Shiraz",
      is_order_warrantied: true
  }).toArray();

  // Query 4
  orders.find({
  "is_order_warrantied": true,
  "$or": [
    {
      "order_priority": 5,
      "stage": { "$ne": "delivered" }
    },
    {
      "price": { "$gte": 1800 }
    }
  ]
    })}

