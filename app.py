from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

users = []

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        users.append({'id': len(users) + 1, 'name': name, 'email': email})
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update(user_id):

    user = None
    for u in users:
        if u['id'] == user_id:
            user=u
            break
    # user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return "User not found", 404

    if request.method == 'POST':
        user['name'] = request.form['name']
        user['email'] = request.form['email']
        return redirect(url_for('index'))
    return render_template('update.html', user=user)

@app.route('/delete/<int:user_id>')
def delete(user_id):
    global users
    users = [u for u in users if u['id'] != user_id] 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
