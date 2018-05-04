Udacity’s Item Catalog Project for FSND
This project required the development of a RESTful web application that provides a list of items within a variety of categories as well as provides a user authentication system by implementing third-party OAuth authentication. . Registered users will have the ability to post, edit and delete their own items. The project also requires implementing CRUD (create, read, update and delete) operations so registered users will have the ability to post, edit and delete their own items. 
Getting Started
1. Clone the fullstack-nanodegree-vm repository.
2. Look for the catalog folder and replace it with the contents of this repository.
3. Launch the Vagrant VM from inside the vagrant folder with: vagrant up
4. Then access the shell with: vagrant ssh
5. Then move inside the catalog folder: cd /vagrant/catalog
6. Then run the application: python application.py
7. After the last command you are able to browse the application at this URL: http://localhost:8000/
Prerequisites
* Python ~2.7
* Vagrant
* VirtualBox
JSON Endpoints
API endpoints for all users:


@app.route('/users.json')
def userJSON():
    users = session.query(User).all()
    return jsonify(User = [u.serialize for u in users])


 API endpoints for all categories and items:

![All categories](/vagrant/catalog/static/images/categories.png)

@app.route('/catalog.json')
def catalogJSON():
    categories = session.query(Category).all()
    items = session.query(Item).all()
    return jsonify(Categories = [c.serialize for c in categories], Items = [i.serialize for i in items])
   API endpoints for all categories:


@app.route('/categories.json')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(Categories = [c.serialize for c in categories])

![All categories](/vagrant/catalog/static/images/items.png)

 API endpoints for all items of a specific category:


@app.route('/<category_name>/items.json')
def itemsJSON(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category=category).all()
    return jsonify(Items = [i.serialize for i in items])


  

Acknowledgments
* Udacity FSND repository
* Genie in a lamp (background image) used with permission from: http://www.tattoodaze.com/lamps-on-pinterest-genie-bottle-i-dream-of-jeannie-and-genie-lamp_RFCdp3/