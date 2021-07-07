from imports import *

def PRE_LSTM(modle,tk1,doc):
    #tk1=TokenLSTM.Save_Tokenizer()
    #doc= '''Alfalfa is the only cure for COVID-19. '''
    doc=[doc]
    doc[0]=preprocessing_process.remove_contractions(doc[0])
    doc[0] = preprocessing_process.clean_text(doc[0])
    test_text = tk1.texts_to_sequences(doc)
    print(test_text)
    test_seq = pad_sequences(test_text, maxlen=100)
    predications = modle.predict(test_seq)
    print(test_seq)
    print(predications)

    # print(predications)
    predications = (predications < 0.5)
    print(predications)
    return predications

def PRE_CNN(modle,tk1,doc):
    #tk1=TokenLSTM.Save_Tokenizer()
    #doc= '''Alfalfa is the only cure for COVID-19. '''
    doc=[doc]
    doc[0]=preprocessing_process.remove_contractions(doc[0])
    doc[0]=preprocessing_process.clean_text(doc[0])
    test_text = tk1.texts_to_sequences(doc)
    print(test_text)
    test_seq = pad_sequences(test_text, maxlen=100)
    predications = modle.predict(test_seq)
    print(test_seq)
    print(predications)

    # print(predications)
    predications = (predications < 0.5)
    print(predications)
    return predications

