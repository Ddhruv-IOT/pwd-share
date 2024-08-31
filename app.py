# # # # from flask import Flask, render_template, redirect, url_for, request, session, flash
# # # # import sqlite3
# # # # import os

# # # # app = Flask(__name__)
# # # # app.config['SECRET_KEY'] = 'your_secret_key'

# # # # DATABASE = 'database.db'

# # # # def init_db():
# # # #     with sqlite3.connect(DATABASE) as conn:
# # # #         cursor = conn.cursor()
# # # #         cursor.execute('''
# # # #             CREATE TABLE IF NOT EXISTS users (
# # # #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #                 username TEXT NOT NULL UNIQUE,
# # # #                 password TEXT NOT NULL
# # # #             )
# # # #         ''')
# # # #         cursor.execute('''
# # # #             CREATE TABLE IF NOT EXISTS todos (
# # # #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #                 user_id INTEGER,
# # # #                 task TEXT NOT NULL,
# # # #                 FOREIGN KEY(user_id) REFERENCES users(id)
# # # #             )
# # # #         ''')
# # # #         conn.commit()

# # # # def get_db():
# # # #     conn = sqlite3.connect(DATABASE)
# # # #     conn.row_factory = sqlite3.Row
# # # #     return conn

# # # # @app.route('/')
# # # # def home():
# # # #     return redirect(url_for('login'))

# # # # @app.route('/login', methods=['GET', 'POST'])
# # # # def login():
# # # #     if request.method == 'POST':
# # # #         username = request.form['username']
# # # #         password = request.form['password']
# # # #         with get_db() as conn:
# # # #             cursor = conn.cursor()
# # # #             cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
# # # #             user = cursor.fetchone()
# # # #             if user:
# # # #                 session['user_id'] = user['id']
# # # #                 return redirect(url_for('todo'))
# # # #             else:
# # # #                 flash('Invalid credentials', 'error')
# # # #     return render_template('login.html')

# # # # @app.route('/signup', methods=['GET', 'POST'])
# # # # def signup():
# # # #     if request.method == 'POST':
# # # #         username = request.form['username']
# # # #         password = request.form['password']
# # # #         with get_db() as conn:
# # # #             cursor = conn.cursor()
# # # #             try:
# # # #                 cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
# # # #                 conn.commit()
# # # #                 # Automatically log the user in after successful signup
# # # #                 user_id = cursor.lastrowid
# # # #                 session['user_id'] = user_id
# # # #                 flash('Signup successful! Welcome to your workspace.', 'success')
# # # #                 return redirect(url_for('todo'))
# # # #             except sqlite3.IntegrityError:
# # # #                 flash('Username already exists', 'error')
# # # #     return render_template('signup.html')

# # # # @app.route('/todo', methods=['GET', 'POST'])
# # # # def todo():
# # # #     if 'user_id' not in session:
# # # #         return redirect(url_for('login'))
    
# # # #     if request.method == 'POST':
# # # #         task = request.form['task']
# # # #         with get_db() as conn:
# # # #             cursor = conn.cursor()
# # # #             cursor.execute('INSERT INTO todos (user_id, task) VALUES (?, ?)', (session['user_id'], task))
# # # #             conn.commit()

# # # #     with get_db() as conn:
# # # #         cursor = conn.cursor()
# # # #         cursor.execute('SELECT task FROM todos WHERE user_id = ?', (session['user_id'],))
# # # #         tasks = cursor.fetchall()

# # # #     return render_template('todo.html', tasks=tasks)

# # # # @app.route('/logout')
# # # # def logout():
# # # #     session.pop('user_id', None)
# # # #     flash('You have been logged out.', 'success')
# # # #     return redirect(url_for('login'))

# # # # if __name__ == '__main__':
# # # #     init_db()
# # # #     app.run(debug=True)


# # # from flask import Flask, render_template, redirect, url_for, request, session, flash
# # # import sqlite3
# # # import os

# # # app = Flask(__name__)
# # # app.config['SECRET_KEY'] = 'your_secret_key'

# # # DATABASE = 'database.db'

# # # def init_db():
# # #     with sqlite3.connect(DATABASE) as conn:
# # #         cursor = conn.cursor()
# # #         cursor.execute('''
# # #             CREATE TABLE IF NOT EXISTS users (
# # #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #                 username TEXT NOT NULL UNIQUE,
# # #                 password TEXT NOT NULL
# # #             )
# # #         ''')
# # #         cursor.execute('''
# # #             CREATE TABLE IF NOT EXISTS passwords0 (
# # #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #                 user_id INTEGER,
# # #                 site_name TEXT NOT NULL,
# # #                 username TEXT NOT NULL,
# # #                 password TEXT NOT NULL,
# # #                 FOREIGN KEY(user_id) REFERENCES users(id)
# # #             )
# # #         ''')
# # #         conn.commit()

# # # def get_db():
# # #     conn = sqlite3.connect(DATABASE)
# # #     conn.row_factory = sqlite3.Row
# # #     return conn

# # # @app.route('/')
# # # def home():
# # #     return redirect(url_for('login'))

# # # @app.route('/login', methods=['GET', 'POST'])
# # # def login():
# # #     if request.method == 'POST':
# # #         username = request.form['username']
# # #         password = request.form['password']
# # #         with get_db() as conn:
# # #             cursor = conn.cursor()
# # #             cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
# # #             user = cursor.fetchone()
# # #             if user:
# # #                 session['user_id'] = user['id']
# # #                 return redirect(url_for('password_manager'))
# # #             else:
# # #                 flash('Invalid credentials', 'error')
# # #     return render_template('login.html')

# # # @app.route('/signup', methods=['GET', 'POST'])
# # # def signup():
# # #     if request.method == 'POST':
# # #         username = request.form['username']
# # #         password = request.form['password']
# # #         with get_db() as conn:
# # #             cursor = conn.cursor()
# # #             try:
# # #                 cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
# # #                 conn.commit()
# # #                 user_id = cursor.lastrowid
# # #                 session['user_id'] = user_id
# # #                 flash('Signup successful! Welcome to your password manager.', 'success')
# # #                 return redirect(url_for('password_manager'))
# # #             except sqlite3.IntegrityError:
# # #                 flash('Username already exists', 'error')
# # #     return render_template('signup.html')

# # # @app.route('/password_manager', methods=['GET', 'POST'])
# # # def password_manager():
# # #     if 'user_id' not in session:
# # #         return redirect(url_for('login'))
    
# # #     if request.method == 'POST':
# # #         site_name = request.form['site_name']
# # #         username = request.form['username']
# # #         password = request.form['password']
# # #         with get_db() as conn:
# # #             cursor = conn.cursor()
# # #             cursor.execute('INSERT INTO passwords0 (user_id, site_name, username, password) VALUES (?, ?, ?, ?)', 
# # #                            (session['user_id'], site_name, username, password))
# # #             conn.commit()

# # #     with get_db() as conn:
# # #         cursor = conn.cursor()
# # #         cursor.execute('SELECT * FROM passwords0 WHERE user_id = ?', (session['user_id'],))
# # #         passwords = cursor.fetchall()

# # #     return render_template('password_manager.html', passwords=passwords)

# # # @app.route('/logout')
# # # def logout():
# # #     session.pop('user_id', None)
# # #     flash('You have been logged out.', 'success')
# # #     return redirect(url_for('login'))

# # # if __name__ == '__main__':
# # #     init_db()
# # #     app.run(debug=True)


# # from flask import Flask, render_template, redirect, url_for, request, session, flash
# # import sqlite3
# # import os

# # app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'your_secret_key'

# # DATABASE = 'database.db'

# # def init_db():
# #     with sqlite3.connect(DATABASE) as conn:
# #         cursor = conn.cursor()
# #         cursor.execute('''
# #             CREATE TABLE IF NOT EXISTS users (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 username TEXT NOT NULL UNIQUE,
# #                 password TEXT NOT NULL
# #             )
# #         ''')
# #         cursor.execute('''
# #             CREATE TABLE IF NOT EXISTS passwords (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 user_id INTEGER,
# #                 site_name TEXT NOT NULL,
# #                 username TEXT NOT NULL,
# #                 password TEXT NOT NULL,
# #                 FOREIGN KEY(user_id) REFERENCES users(id)
# #             )
# #         ''')
# #         cursor.execute('''
# #             CREATE TABLE IF NOT EXISTS shared_passwords (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 password_id INTEGER NOT NULL,
# #                 shared_with_user_id INTEGER NOT NULL,
# #                 FOREIGN KEY(password_id) REFERENCES passwords(id),
# #                 FOREIGN KEY(shared_with_user_id) REFERENCES users(id)
# #             )
# #         ''')
# #         conn.commit()

# # def get_db():
# #     conn = sqlite3.connect(DATABASE)
# #     conn.row_factory = sqlite3.Row
# #     return conn

# # @app.route('/')
# # def home():
# #     return redirect(url_for('login'))

# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         with get_db() as conn:
# #             cursor = conn.cursor()
# #             cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
# #             user = cursor.fetchone()
# #             if user:
# #                 session['user_id'] = user['id']
# #                 return redirect(url_for('password_manager'))
# #             else:
# #                 flash('Invalid credentials', 'error')
# #     return render_template('login.html')

# # @app.route('/signup', methods=['GET', 'POST'])
# # def signup():
# #     if request.method == 'POST']:
# #         username = request.form['username']
# #         password = request.form['password']
# #         with get_db() as conn:
# #             cursor = conn.cursor()
# #             try:
# #                 cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
# #                 conn.commit()
# #                 user_id = cursor.lastrowid
# #                 session['user_id'] = user_id
# #                 flash('Signup successful! Welcome to your workspace.', 'success')
# #                 return redirect(url_for('password_manager'))
# #             except sqlite3.IntegrityError:
# #                 flash('Username already exists', 'error')
# #     return render_template('signup.html')

# # @app.route('/password_manager', methods=['GET', 'POST'])
# # def password_manager():
# #     if 'user_id' not in session:
# #         return redirect(url_for('login'))

# #     if request.method == 'POST':
# #         site_name = request.form['site_name']
# #         username = request.form['username']
# #         password = request.form['password']
# #         with get_db() as conn:
# #             cursor = conn.cursor()
# #             cursor.execute('INSERT INTO passwords (user_id, site_name, username, password) VALUES (?, ?, ?, ?)',
# #                            (session['user_id'], site_name, username, password))
# #             conn.commit()

# #     with get_db() as conn:
# #         cursor = conn.cursor()

# #         # Get passwords created by the user
# #         cursor.execute('SELECT * FROM passwords WHERE user_id = ?', (session['user_id'],))
# #         passwords = cursor.fetchall()

# #         # Get passwords shared with the user
# #         cursor.execute('''
# #             SELECT p.site_name, p.username, p.password FROM passwords p
# #             INNER JOIN shared_passwords sp ON p.id = sp.password_id
# #             WHERE sp.shared_with_user_id = ?
# #         ''', (session['user_id'],))
# #         shared_passwords = cursor.fetchall()

# #     return render_template('password_manager.html', passwords=passwords, shared_passwords=shared_passwords)

# # @app.route('/share_password/<int:password_id>', methods=['POST'])
# # def share_password(password_id):
# #     if 'user_id' not in session:
# #         return redirect(url_for('login'))

# #     share_with_username = request.form['share_with_username']

# #     with get_db() as conn:
# #         cursor = conn.cursor()

# #         cursor.execute('SELECT id FROM users WHERE username = ?', (share_with_username,))
# #         share_with_user = cursor.fetchone()

# #         if share_with_user:
# #             share_with_user_id = share_with_user['id']

# #             cursor.execute('''
# #                 SELECT * FROM shared_passwords 
# #                 WHERE password_id = ? AND shared_with_user_id = ?
# #             ''', (password_id, share_with_user_id))

# #             existing_share = cursor.fetchone()

# #             if existing_share:
# #                 flash(f'This password is already shared with {share_with_username}.', 'info')
# #             else:
# #                 cursor.execute('''
# #                     INSERT INTO shared_passwords (password_id, shared_with_user_id)
# #                     VALUES (?, ?)
# #                 ''', (password_id, share_with_user_id))
# #                 conn.commit()
# #                 flash(f'Password shared with {share_with_username}.', 'success')
# #         else:
# #             flash(f'User {share_with_username} does not exist.', 'error')

# #     return redirect(url_for('password_manager'))

# # @app.route('/logout')
# # def logout():
# #     session.pop('user_id', None)
# #     flash('You have been logged out.', 'success')
# #     return redirect(url_for('login'))

# # if __name__ == '__main__':
# #     init_db()
# #     app.run(debug=True)
# from flask import Flask, render_template, redirect, url_for, request, session, flash
# import sqlite3
# import os

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'

# DATABASE = 'database.db'

# def init_db():
#     with sqlite3.connect(DATABASE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT NOT NULL UNIQUE,
#                 password TEXT NOT NULL
#             )
#         ''')
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS passwords (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 user_id INTEGER,
#                 site_name TEXT NOT NULL,
#                 username TEXT NOT NULL,
#                 password TEXT NOT NULL,
#                 FOREIGN KEY(user_id) REFERENCES users(id)
#             )
#         ''')
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS shared_passwords (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 password_id INTEGER NOT NULL,
#                 shared_with_user_id INTEGER NOT NULL,
#                 FOREIGN KEY(password_id) REFERENCES passwords(id),
#                 FOREIGN KEY(shared_with_user_id) REFERENCES users(id)
#             )
#         ''')
#         conn.commit()

# def get_db():
#     conn = sqlite3.connect(DATABASE)
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route('/')
# def home():
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         with get_db() as conn:
#             cursor = conn.cursor()
#             cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#             user = cursor.fetchone()
#             if user:
#                 session['user_id'] = user['id']
#                 return redirect(url_for('password_manager'))
#             else:
#                 flash('Invalid credentials', 'error')
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         with get_db() as conn:
#             cursor = conn.cursor()
#             try:
#                 cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
#                 conn.commit()
#                 user_id = cursor.lastrowid
#                 session['user_id'] = user_id
#                 flash('Signup successful! Welcome to your workspace.', 'success')
#                 return redirect(url_for('password_manager'))
#             except sqlite3.IntegrityError:
#                 flash('Username already exists', 'error')
#     return render_template('signup.html')

# @app.route('/password_manager', methods=['GET', 'POST'])
# def password_manager():
#     if 'user_id' not in session:
#         return redirect(url_for('login'))

#     if request.method == 'POST':
#         site_name = request.form['site_name']
#         username = request.form['username']
#         password = request.form['password']
#         with get_db() as conn:
#             cursor = conn.cursor()
#             cursor.execute('INSERT INTO passwords (user_id, site_name, username, password) VALUES (?, ?, ?, ?)',
#                            (session['user_id'], site_name, username, password))
#             conn.commit()

#     with get_db() as conn:
#         cursor = conn.cursor()

#         # Get passwords created by the user
#         cursor.execute('SELECT * FROM passwords WHERE user_id = ?', (session['user_id'],))
#         passwords = cursor.fetchall()

#         # Get passwords shared with the user
#         cursor.execute('''
#             SELECT p.site_name, p.username, p.password FROM passwords p
#             INNER JOIN shared_passwords sp ON p.id = sp.password_id
#             WHERE sp.shared_with_user_id = ?
#         ''', (session['user_id'],))
#         shared_passwords = cursor.fetchall()

#     return render_template('password_manager.html', passwords=passwords, shared_passwords=shared_passwords)

# @app.route('/share_password/<int:password_id>', methods=['POST'])
# def share_password(password_id):
#     if 'user_id' not in session:
#         return redirect(url_for('login'))

#     share_with_username = request.form['share_with_username']

#     with get_db() as conn:
#         cursor = conn.cursor()

#         cursor.execute('SELECT id FROM users WHERE username = ?', (share_with_username,))
#         share_with_user = cursor.fetchone()

#         if share_with_user:
#             share_with_user_id = share_with_user['id']

#             cursor.execute('''
#                 SELECT * FROM shared_passwords 
#                 WHERE password_id = ? AND shared_with_user_id = ?
#             ''', (password_id, share_with_user_id))

#             existing_share = cursor.fetchone()

#             if existing_share:
#                 flash(f'This password is already shared with {share_with_username}.', 'info')
#             else:
#                 cursor.execute('''
#                     INSERT INTO shared_passwords (password_id, shared_with_user_id)
#                     VALUES (?, ?)
#                 ''', (password_id, share_with_user_id))
#                 conn.commit()
#                 flash(f'Password shared with {share_with_username}.', 'success')
#         else:
#             flash(f'User {share_with_username} does not exist.', 'error')

#     return redirect(url_for('password_manager'))

# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)
#     flash('You have been logged out.', 'success')
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)


from flask import Flask, render_template, redirect, url_for, request, session, flash
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

DATABASE = 'database.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                site_name TEXT NOT NULL,
                password TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS shared_passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password_id INTEGER NOT NULL,
                shared_with_user_id INTEGER NOT NULL,
                FOREIGN KEY(password_id) REFERENCES passwords(id),
                FOREIGN KEY(shared_with_user_id) REFERENCES users(id)
            )
        ''')
        conn.commit()

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user['id']
                return redirect(url_for('password_manager'))
            else:
                flash('Invalid credentials', 'error')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with get_db() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                user_id = cursor.lastrowid
                session['user_id'] = user_id
                flash('Signup successful! Welcome to your workspace.', 'success')
                return redirect(url_for('password_manager'))
            except sqlite3.IntegrityError:
                flash('Username already exists', 'error')
    return render_template('signup.html')

@app.route('/password_manager', methods=['GET', 'POST'])
def password_manager():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        site_name = request.form['site_name']
        password = request.form['password']
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO passwords (user_id, site_name, password) VALUES (?, ?, ?)',
                           (session['user_id'], site_name, password))
            conn.commit()

    with get_db() as conn:
        cursor = conn.cursor()

        # Get passwords created by the user
        cursor.execute('SELECT * FROM passwords WHERE user_id = ?', (session['user_id'],))
        passwords = cursor.fetchall()

        # Get passwords shared with the user
        cursor.execute('''
            SELECT p.site_name, p.password FROM passwords p
            INNER JOIN shared_passwords sp ON p.id = sp.password_id
            WHERE sp.shared_with_user_id = ?
        ''', (session['user_id'],))
        shared_passwords = cursor.fetchall()

    return render_template('password_manager.html', passwords=passwords, shared_passwords=shared_passwords)

@app.route('/share_password/<int:password_id>', methods=['POST'])
def share_password(password_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    share_with_username = request.form['share_with_username']

    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM users WHERE username = ?', (share_with_username,))
        share_with_user = cursor.fetchone()

        if share_with_user:
            share_with_user_id = share_with_user['id']

            cursor.execute('''
                SELECT * FROM shared_passwords 
                WHERE password_id = ? AND shared_with_user_id = ?
            ''', (password_id, share_with_user_id))

            existing_share = cursor.fetchone()

            if existing_share:
                flash(f'This password is already shared with {share_with_username}.', 'info')
            else:
                cursor.execute('''
                    INSERT INTO shared_passwords (password_id, shared_with_user_id)
                    VALUES (?, ?)
                ''', (password_id, share_with_user_id))
                conn.commit()
                flash(f'Password shared with {share_with_username}.', 'success')
        else:
            flash(f'User {share_with_username} does not exist.', 'error')

    return redirect(url_for('password_manager'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
