from flask import Flask, request, render_template, session
import os,io
app = Flask(__name__)
app.secret_key = "ProjectWEGO-SEAL"
@app.route('/insert/<figure>')
def insert(figure):
    f = open(os.getcwd()+"/xml/Figure{}-center.xml".format(figure),'r',encoding='utf8').read()
    print(f)
    return render_template('test.html',data=f)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, True)