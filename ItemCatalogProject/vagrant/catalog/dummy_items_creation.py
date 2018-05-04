#from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog_database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user1 = User(name="Stacy Achenbach", email="achenbach333@gmail.com", picture="https://plus.google.com/u/0/photos/103350261740473697026/albums/profile/5697635113032929042?iso=false")
session.add(user1)
session.commit()

# Create category #1 and add items to the category
category1 = Category(name="Glass Bottles", user_id=1)
session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Antique Mason Jar",
                     description ="Material: Glass, Size:large",   
                     image = "/static/images/antique_mason_jar.jpg",
                     category=category1)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Blue French Water Bottle",
                    description="Material: Glass, Size: Large",
                    image = "/static/images/BlueBottle.jpg",
                    category = category1)
session.add(item2)
session.commit()


# Create category #2 and add items to the category
category2 = Category(name="Perfume Bottles", user_id=1)
session.add(category2)
session.commit()

item3 = Item(user_id=1, name = "Crystal Sail",
                     description ="Material: Crystal Size: 'Large'",
                     image = "/static/images/CrystalSail.jpg",
                     category=category2)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Sunburst",
                     description ="Material: Glass Size: Medium",
                     image = '/static/images/Sunburst.jpg',
                     category=category2)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Avon Swirl",
                    description ="Material: Plastic Size: Small", 
                    image = "/static/images/AvonSwirl.jpg",
                    category=category2)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Royal Crown",
                    description ="Material: Glass, Silver Size: Miniature",
                    image = "/static/images/RoyalCrown.jpg",
                     category=category2)
session.add(item6)
session.commit()

