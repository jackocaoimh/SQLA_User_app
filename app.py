from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jackocaoimh:turner12345@localhost/blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

@app.route('/')
def list_users():
    users = User.query.all()
    return render_template('list.html', users=users)

@app.route('/new_user_form')
def show_new_user_form():
    return render_template('new_user.html')

@app.route('/new_user', methods=["POST"])
def new_user():
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    img_url = request.form['img_url']

    user = User(first_name=first_name, second_name=second_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()
    
    return redirect('/')

@app.route('/<int:user_id>')
def show_user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('detail.html', user=user)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id) 
    db.session.delete(user)  
    db.session.commit()  
    return redirect('/') 

@app.route('/edit_user/<int:user_id>')
def edit_user_form(user_id):
    user = User.query.get_or_404(user_id)  
    return render_template('edit_user.html', user=user) 

@app.route('/edit_user/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    user.first_name = request.form['first_name']
    user.second_name = request.form['second_name']
    user.img_url = request.form['img_url']

    db.session.commit()
    return redirect(f'/{user_id}')
