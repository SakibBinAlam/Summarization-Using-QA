from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
app.config['UPLOAD_FOLDER'] = 'static/files' 

import torch
import transformers
from transformers import pipeline


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import T5Tokenizer, T5ForConditionalGeneration

# # model for summary generation
model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base', model_max_length=987)

# # Create a pipeline for generating summaries
summary_generator = pipeline('text2text-generation', model=model, tokenizer=tokenizer)

# create a pipeline for generating qa
qa_generator = pipeline('text2text-generation', model='mojians/E2E-QA-Mining')

@app.route('/')
def index():
    return redirect(url_for('autocomplete'))


class MyForm(FlaskForm):
    name = StringField('Type something', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/home', methods = ['GET','POST'])
def autocomplete():
    form = MyForm()
    code = False
    name = False
    qa = False

    name = form.name.data 
    
    qa_pairs = qa_generator(str(name), max_length=50, num_beams=4, do_sample=True, top_p=0.95, top_k=60)
    
    for qa_pair in qa_pairs:
        qa = qa_pair['generated_text']

    summary_input = f"summarize: {qa} {name}"
    summary_ids = summary_generator(summary_input, max_length=50, num_beams=4, do_sample=True, top_p=0.95, top_k=60)[0]['generated_text']
    #code = pipe(name, num_return_sequences=50)[0]["generated_text"]

    form.name.data = ""

    return render_template("home.html",form=form,name =name, qa=qa, code=summary_ids)

if __name__ == "__main__":
    app.run(debug=True)