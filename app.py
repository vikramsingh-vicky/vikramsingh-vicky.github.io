from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
with app.app_context():
    db = SQLAlchemy(app)

class Tasks(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self) :
        return f"{self.sno} - {self.task_name}"

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        print(request.form['taskname'])
        task = Tasks(task_name=request.form['taskname'], desc=request.form['desc'])
        db.session.add(task)
        db.session.commit()
    allTasks = Tasks.query.all()
        # print(allTasks)
    return render_template('index.html', allTasks = allTasks)
        # return 'Hello World!'
@app.route('/delete/<int:sno>')
def delete(sno):
    delTasks = Tasks.query.filter_by(sno=sno).first()
    db.session.delete(delTasks)
    db.session.commit()
    # print(allTasks)
    return redirect("/")

@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        updtTasks = Tasks.query.filter_by(sno=sno).first()
        updtTasks.task_name = request.form['taskname']
        updtTasks.desc = request.form['desc']
        # task = Tasks(task_name=request.form['taskname'], desc=request.form['desc'])
        db.session.add(updtTasks)
        db.session.commit()
        return redirect("/")
    updtTasks = Tasks.query.filter_by(sno=sno).first()
    return render_template('update.html', updtTasks = updtTasks)
    

if __name__=="__main__":
    app.run(debug=True)