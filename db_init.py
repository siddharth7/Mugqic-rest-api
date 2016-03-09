from app import db, models
u = models.User(name="siddharth", phonenumber="9810180107")
db.session.add(u)
db.session.commit()
u = models.User(name="rohan", phonenumber="9811223342")
db.session.add(u)
db.session.commit()