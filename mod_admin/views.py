from . import admin

@admin.route('/')
def index():
    return "Hello from admin Index"

@admin.route('/login/')
def login():
    session['name'] = 'Alireza'
    print(session)
    return "1"

