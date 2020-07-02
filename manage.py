from app import db,create_app
from flask_script import Manager

app = create_app

if __name__=="__main__":
    db.create_all()
    manager = Manager(app)
    manager.run()
    
