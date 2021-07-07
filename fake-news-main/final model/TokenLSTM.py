from imports import *



df = readDataset.read_data()
df["text"] = df["text"].apply(preprocessing_process.remove_contractions)
df["text"] = df["text"].apply(preprocessing_process.clean_text)

df.drop_duplicates(subset=["text"], inplace=True)
df.dropna(inplace=True)
sent_length=100
X_train, X_test, y_train, y_test = train_test_split(df.text, df.target, test_size=0.3, random_state=37)
tk = Tokenizer()
tk.fit_on_texts(X_train)
X_train_seq = tk.texts_to_sequences(X_train)
X_test_seq = tk.texts_to_sequences(X_test)

X_train_seq_trunc = pad_sequences(X_train_seq, maxlen=sent_length)
X_test_seq_trunc = pad_sequences(X_test_seq, maxlen=sent_length)
model = Sequential()  # initilaizing the Sequential nature for CNN model

model.add(Embedding(len(tk.index_word)+3, 32, input_length=sent_length))
model.add(LSTM(sent_length))
model.add(Dense(1, activation='sigmoid'))
model.compile( loss='binary_crossentropy',optimizer='adam',
                metrics=['accuracy'])

X_train_array = np.asarray(X_train_seq_trunc, dtype=np.int)
y_train_array = np.asarray(y_train, dtype=np.int)

X_test_array = np.asarray(X_test_seq_trunc, dtype=np.int)
y_test_array = np.asarray(y_test, dtype=np.int)
model.fit(X_train_array, y_train_array,validation_data=(X_test_array,y_test_array), epochs=5, batch_size=64)
model.save("tokLSTM.h5")

with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tk, handle, protocol=pickle.HIGHEST_PROTOCOL)


