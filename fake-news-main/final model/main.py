from imports import *
from predication import*
from extra_features import*
#import TokenLSTM

app=Flask(__name__)

loaded_model = keras.models.load_model('tokLSTM.h5')
with open('tokenizer.pickle', 'rb') as handle:
    loaded_tk = pickle.load(handle)

#if u want to predict with CNN Model, just Uncomment the next 3 lines, BUT don't forget to comment lines(8,9,10)

#loaded_model = keras.models.load_model('tokCNN.h5')
#with open('tokenizerCNN.pickle', 'rb') as handle:
#    loaded_tk = pickle.load(handle)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])

def predict():
    if request.method == 'POST':
        message = request.form['message']
        
        pred = PRE_LSTM(loaded_model,loaded_tk,message)
        print(pred)
        return render_template('home.html',info=pred)
    else: 
        return render_template('home.html',info="Something went wrong!")

@app.route('/download',methods=['POST'])
def download():
    if request.method=='POST':
        getListOfTruth()
        return render_template('home.html')
    else: 
        return render_template('home.html',info="Something went wrong!")

@app.route('/advance_search',methods=['GET','POST'])

def advance_search():

    if request.method=='POST':
        word = request.form['kword']
        result=getListOfKeyWord(word)
        table=listing(result)
        return render_template('advance_search.html',key=table)
    return render_template('advance_search.html')

   
        

if __name__ == '__main__':
    app.run(debug=True)
