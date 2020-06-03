from app import app
from app.models import User, Submission
from app import ui,db

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User': User, 'Submission':Submission}

if __name__=="__main__":
    #app.run(host='0.0.0.0')
    ui.run()
