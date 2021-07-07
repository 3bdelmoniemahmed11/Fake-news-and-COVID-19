from imports import *
def getListOfTruth():
    webbrowser.open('https://drive.google.com/file/d/1E5OkJ-ZT79GbvZG_ELtUv69YBSYxCo-U/view?usp=sharing')


#input for the user function 
def getListOfKeyWord(keyword):
    import os
    cwd = os.getcwd()
    print(cwd)
    df=pd.read_excel("fake-news-main/final model/finaltrue.xlsx")
    corpus=[]
    for i in range(len(df)):
        if keyword in df["text"][i]:
            corpus.append(df["text"][i])
    return corpus

#def COMBO_CNN():
    mod1 = train_CNN()
    predic = PRE_CNN(mod1)
    return predic
def listing(table):
        x=0
        tab=[]
        for item in range(0,len(table)):
            x+=1
            result= f'{x}- {table[item]}' 
            tab.append(result)
        final = '<br>'.join(tab)
        #print(final)
        return final
