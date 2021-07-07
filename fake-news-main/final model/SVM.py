from pickle import load
from keras.layers import embeddings
from imports import *
import Embedding
from sklearn.metrics import plot_confusion_matrix,recall_score, precision_score
import matplotlib.pyplot as plt
from sklearn import svm
import preprocessing


filename = 'SVM_model.sav'
def Train_DATA():
    df = readDataset.read_data()
    df["text"] = df["text"].apply(preprocessing_process.remove_contractions)
    df["text"] = df["text"].apply(preprocessing_process.clean_text)

    df.drop_duplicates(subset=["text"], inplace=True)
    df.dropna(inplace=True)
    #if  you want to run the preprocessing  with stemming, uncomment the following comment
    #And comment lines (14,15,24)
    '''for text in df['text']:
        list_data.append(preprocessing.text_preprocessing(text)) 
    list_data=Embedding.embedding(list_data)'''
    list_data=Embedding.embedding(df)
    
    X_train, X_test, y_train, y_test = train_test_split(list_data, df.target, test_size=0.3, random_state=37)
    #Create a svm Classifier
    clf = svm.SVC(kernel='linear') # Linear Kernel
    #Train the model using the training sets
    clf.fit(X_train, y_train)
    # save the model to disk
    
    pickle.dump(clf, open(filename, 'wb'))
    
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    # Model Accuracy: how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    y_pred2 =clf.predict(X_test)
    precision = precision_score(y_test, y_pred2)
    # Model Precision
    print('Precision: %f' % precision)
    recall = recall_score(y_test, y_pred2)
    print('Recall: %f' % recall)
    # Model Precision
    plot_confusion_matrix(clf, X_test, y_test,cmap=plt.cm.Blues)  
    plt.show()
    return clf 
    


def PRE_SVM():
    
    doc= '''COVID-19: The Immune System Can Fight Back  '''
    doc=[doc]
    doc[0]=preprocessing_process.remove_contractions(doc[0])
    doc[0] = preprocessing_process.clean_text(doc[0])
    output=Embedding.embedding_PRE(doc[0])
    if (output == 0):
        print ("Real News")
    else:
        print("Fake News")

    print(output)
    
    

    
Train_DATA()
PRE_SVM()