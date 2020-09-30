
from flask import Flask, render_template,request,escape
from dunder import prod

app=Flask(__name__)

def log_req(req,res):
    with open('search.log','a') as log:
        print(req,res,file=log)


@app.route('/sum4',methods=['POST'])
def a():
    n1=request.form['num1']
    n2=request.form['num2']
    r= str(prod(n1,n2))
    log_req(request,r)
    tit='AND the PRoduct be like:'
    return render_template('results.html',title=tit,result=r)

@app.route('/')
@app.route('/entry')
def page():
    return render_template('entry.html',title='Are you ready to multiply')

@app.route('/view')
def v():
    with open('search.log') as log:
        c=log.read()
        return escape(c)

if __name__=='__main__':
      app.run(debug=True) 
 