from flask import render_template, request, Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yogikadikar@localhost/xltocsv'
db = SQLAlchemy(app)

#xltocsv = db.Table('xltocsv', db.metadata, autoload = True, autoload_with = db.engine)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
new = Base.classes.test

@app.route('/')
def my_form():

    search= db.session.query(new).all()
    for siten in search:
        print (siten.Indussite_id, siten.sitename, siten.techname, siten.technumber)
    return '' 

if __name__ == "__main__":
    app.run(debug = True)