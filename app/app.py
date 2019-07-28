import flask
import pickle
import sqlite3 as sql
import numpy as np
import pandas as pd

from flask import Flask, render_template, request, redirect, url_for, session
from sklearn.metrics.pairwise import cosine_similarity
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from app.lib.word_similarity import WordSimilarityClassifier
from app.lib.preprocess import IndoTextCleaner, StopWordsEliminator
from app.lib.dict import load_dict

app = Flask(__name__)
app.secret_key = "super secret key"

DATABASE_URI = 'db/evaluation.db'

target_dict, surah_dict = load_dict()

vectorizer = pickle.load(open('pkl/vectorizer.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('pkl/tfidf_vectorizer.pkl', 'rb'))
tfidf_verse_matrix = pickle.load(open('pkl/tfidf_verse_matrix.pkl', 'rb'))

tree = pickle.load(open('pkl/tree.pkl', 'rb'))
wordsim = pickle.load(open('pkl/wordsim.pkl', 'rb'))

id_quran = pd.read_csv('../quran/Indonesian_clean.csv')
ar_quran = pd.read_csv('../quran/Arabic.csv')
en_quran = pd.read_csv('../quran/English.csv')

text_cleaner = IndoTextCleaner()
sw_elim = StopWordsEliminator()
stemmer = StemmerFactory().create_stemmer()

conn = sql.connect(DATABASE_URI)
conn.execute('CREATE TABLE IF NOT EXISTS evaluation (evaluator TEXT, raw_text TEXT, labels TEXT, verse_relevance INTEGER, verse_irrelevance INTEGER)')
conn.close()

@app.route('/')
@app.route('/index')
def index():
    # return render_template('index.html')
    return render_template('new_index.html')

@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        form = request.form
        session['username'] = form['username']

    return render_template('main.html')

@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        form = request.form
        input_text = pd.Series([form['input-text']])
        amount_ayah = int(form['amount-ayah'])
        method = form['optradio']

        input_text = input_text.apply(lambda x: text_cleaner.transform(x))
        input_text = input_text.apply(lambda x: sw_elim.transform(x))
        input_text = input_text.apply(lambda x: stemmer.stem(x))

        raw_answers = []
        answers = []
        answers_txt = ''

        if (method == 'multilabel'):
            results = np.array(tree.predict(vectorizer.transform(input_text)))

            for result in results:
                idx = 0
                for label in result:
                    if label == 1:
                        for name, key in target_dict.items():
                            if key == idx:
                                answers.append(name)
                    idx = idx + 1

            answers_txt = ' '.join(answers)
            raw_answers = answers
            answers = pd.Series([answers_txt])
        else:
            answers_txt = input_text.values[0]

            answers = pd.Series([answers_txt])

        answers = answers.apply(lambda x: text_cleaner.transform(x))
        answers = answers.apply(lambda x: sw_elim.transform(x))
        answers = answers.apply(lambda x: stemmer.stem(x))

        answers_vector = tfidf_vectorizer.transform(answers)

        res_unsorted = cosine_similarity(answers_vector, tfidf_verse_matrix)

        res_sorted = sorted(range(len(res_unsorted[0])), key=lambda k: res_unsorted[0][k], reverse = True)

        similarity_score = []
        verse_results = []

        session['input_text'] = input_text.values[0]
        session['raw_answers'] = raw_answers
        session['amount_ayah'] = amount_ayah

        for i in range(0, amount_ayah):
            ar_txt = ar_quran.loc[ res_sorted[i], : ]['surah|ayah|text'].split('|')[-1]
            en_txt = en_quran.loc[ res_sorted[i], : ]['Text']
            id_txt = id_quran.loc[ res_sorted[i] , : ]['text']

            surah_idx = id_quran.loc[ res_sorted[i] , : ]['surah']
            surah_name = surah_dict.get(str(surah_idx))

            ayah_idx = id_quran.loc[ res_sorted[i] , : ]['ayah']

            similarity_score.append(res_unsorted[0][res_sorted[i]])

            verse_results.append([surah_idx, surah_name, ayah_idx, ar_txt, en_txt, id_txt])

        return render_template('results.html', input_text=input_text, answers=answers, answers_txt=answers_txt, method=method,
                                               amount_ayah=amount_ayah, verse_results=verse_results, similarity_score=similarity_score,
                                               raw_answers=raw_answers, answers_len=len(raw_answers))
    else:
        return redirect(url_for('error'))

@app.route('/evaluation', methods=['POST'])
def evaluation():
    if request.method == 'POST':
        try:
            form = request.form

            username = 'Guest'
            if 'username' in session:
                username = session['username']
            
            input_text = session['input_text']
            raw_answers = session['raw_answers']
            amount_ayah = session['amount_ayah']
            
            labels = []
            verse_relevance = 0
            verse_irrelevance = 0

            for answer in raw_answers:
                if answer in form:
                    temp = form[answer]
                    temp = temp + ':' + 'relevance'
                    labels.append(temp)
                else:
                    temp = answer + ':' + 'irrelevance'
                    labels.append(temp)

            for i in range(0,amount_ayah):
                if str(i) in form:
                    verse_relevance += 1

            verse_irrelevance = amount_ayah - verse_relevance
            labels_txt = ','.join(labels)

            with sql.connect(DATABASE_URI) as con:
                cur = con.cursor()
                cur.execute('INSERT INTO evaluation (evaluator,raw_text,labels,verse_relevance,verse_irrelevance) VALUES (?,?,?,?,?)',(username,input_text,labels_txt,verse_relevance,verse_irrelevance))
                con.commit()
                msg = 'Record successfully added.'
        except:
            con.rollback()
            msg = 'Error in insert operation.'
        finally:
            con.close()
            return render_template('evaluation.html', username=username, msg=msg)

@app.route('/list')
def list():
   con = sql.connect(DATABASE_URI)
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute('SELECT * FROM evaluation')
   
   rows = cur.fetchall()
   return render_template('list.html', rows=rows)

@app.route('/dump')
def dump():
    con = sql.connect(DATABASE_URI)
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute('SELECT * FROM evaluation')
    
    evaluator = []
    raw_text = []
    labels = []
    verse_relevance = []
    verse_irrelevance = []

    rows = cur.fetchall()
    for row in rows:
        evaluator.append(row["evaluator"])
        raw_text.append(row["raw_text"])
        labels.append(row["labels"])
        verse_relevance.append(row["verse_relevance"])
        verse_irrelevance.append(row["verse_irrelevance"])
    
    df = pd.DataFrame({
        'evaluator': evaluator,
        'raw_text': raw_text,
        'labels': labels,
        'verse_relevance': verse_relevance,
        'verse_irrelevance': verse_irrelevance
    })
    df.to_csv('res/eval-results.csv', encoding='utf-8', index=False)

    return redirect(url_for('index'))

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

