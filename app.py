from flask import Flask, redirect, url_for, request, render_template
from pcg import yazitura


app = Flask(__name__)

@app.route('/')
def index():
   r = yazitura(42,54,65)
   print(r)
   return render_template('pcg.html')

@app.route('/pcg',methods = ['POST'])
def pcg():
   if request.method == 'POST':
      tohum_a = request.form['tohum_a']
      tohum_b = request.form['tohum_b']
      iterasyon = request.form['iterasyon']
      
      r = yazitura(int(tohum_a),int(tohum_b),int(iterasyon))
      
      T = 0
      Y = 0
      R = ''
      for l in r:
        R+=l
        if l == 'T':
            T+=1
        else:
            Y+=1

      return R + '@@@' + str(T) + '@@@' + str(Y)
     
      
if __name__ == '__main__':
   app.run(debug = True)