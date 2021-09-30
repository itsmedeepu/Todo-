
from datetime import datetime
from flask import Flask,render_template,request,redirect
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo= Todo.query.all()
    print(allTodo)
    return render_template('index.html',allTodo=allTodo)
@app.route("/show")
def products():
    allTodo= Todo.query.all()
    print(allTodo)
    return 'this is product page'


@app.route("/update")
def update():
    allTodo= Todo.query.all()
    print(allTodo)
    return 'this is product page'


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True,port=8000)