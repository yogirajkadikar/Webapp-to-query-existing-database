from flask import render_template, request, Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yogikadikar@localhost/xltocsv'
db = SQLAlchemy(app)

#xltocsv = db.Table('xltocsv', db.metadata, autoload = True, autoload_with = db.engine)

#AUTO-MAP technique used to fetch existing database
Base = automap_base()
Base.prepare(db.engine, reflect=True)
new = Base.classes.test

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/post_user', methods=['POST'])
def my_form_post():
    siten = request.form['siten'] #keyword is taken from user
    print (siten)

    
    search= db.session.query(new).all() #db table is stored in variable

    # here I want to display entire row which matches the keyword provided by user input, 
    #but i am getting whole list and last row is printed
    for siten in search:
        print ( siten.sitename)
    
    return siten.sitename


if __name__ == "__main__":
    app.run(debug = True)