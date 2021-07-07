from imports import *
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

#if you want  to run preprocessing with stemming, replace df['text'] in the first loop  in  the function "embedding"
#after applying the comment  line (19,20)  in  "SVM.py"
def embedding(df):
    doc=[]
    for item in df['text']:
        doc.append(str(item))
            
    tokenized_doc = []
    for d in doc:
        tokenized_doc.append(word_tokenize(d.lower()))
    tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_doc)]
    model=Doc2Vec(tagged_data,vector_size=100,window=2, min_count=1,workers=4,epochs=100)
    model.save("doc2vec.model")
    list_data = []
    for index in range(0,len(model.dv)):
        list_data.append(model.dv[index])
    return list_data

def embedding_PRE(doc):
    token_words=[]
    token_words.append(word_tokenize(doc))
    model=Doc2Vec.load("doc2vec.model")
    vector = model.infer_vector(token_words[0])
    
    loaded_model = pickle.load(open('SVM_model.sav','rb'))
    output = loaded_model.predict([vector])
    return output