const { MongoClient } = require("mongodb");

const client = new MongoClient("mongodb://localhost:27017");
const db = client.db("quera");

async function run() {
  try {
    await client.connect();
    console.log("Connected to MongoDB");

    // Query 1: Change all orders with stage "processing" in Tehran to "delivered"
    const query1Result = await db.collection("orders").updateMany(
      { stage: "processing", city: "Tehran" },
      { $set: { stage: "delivered" } }
    );
    console.log("Query 1 result:", query1Result);

    // Query 2: Find users with more than 5 purchases, add 50 to balance, set discount_eligibility to true
    const query2Result = await db.collection("users").updateMany(
      { total_purchases: { $gt: 5 } },
      {
        $inc: { balance: 50 },
        $set: { discount_eligibility: true }
      }
    );
    console.log("Query 2 result:", query2Result);

    // Query 3: Find orders where customer_name is "Erfan" and "laptop" is in items, add "wireless mouse" to items
    const query3Result = await db.collection("orders").updateMany(
      { customer_name: "Erfan", items: "laptop" },
      { $addToSet: { items: "wireless mouse" } }
    );
    console.log("Query 3 result:", query3Result);

    // Query 4: Find users with verified email and balance > 300, increase balance by 20%, increase total_purchases by 2, record last_update
    const query4Result = await db.collection("users").updateMany(
      { email_verified: true, balance: { $gt: 300 } },
      {
        $mul: { balance: 1.2 },
        $inc: { total_purchases: 2 },
        $currentDate: { last_update: true }
      }
    );
    console.log("Query 4 result:", query4Result);

    // Query 5: For orders of "Narges" with stage "delivering", remove discount field, rename is_order_warrantied to warranty_status, increase price by 10%, record last_modified
    const query5Result = await db.collection("orders").updateMany(
      { customer_name: "Narges", stage: "delivering" },
      {
        $unset: { discount: "" },
        $mul: { price: 1.1 },
        $rename: { is_order_warrantied: "warranty_status" },
        $currentDate: { last_modified: true }
      }
    );
    console.log("Query 5 result:", query5Result);

  } catch (error) {
    console.error("Error:", error);
  } finally {
    await client.close();
    console.log("Connection closed");
  }
}

run();
