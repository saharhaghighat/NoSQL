db.users.deleteOne({username:"user7945"})

db.users.deleteMany({ email: { $regex: /^.+@benyamin\.il$/ } })


db.users.findOneAndDelete(
    {total_purchases :0},
    {
        sort:{created_at:-1},
        projection: {_id:0 , name:1, username:1}

    }
    )