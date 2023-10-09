from flask import Flask, render_template, request, redirect, jsonify

from transformers import pipeline
from transformers import AutoTokenizer, T5ForConditionalGeneration

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def gen():
    content = request.form
    msg = content['msg']
    print(msg)
    pipe = pipeline("text2text-generation", model="google/flan-t5-small")
    output = pipe(msg)
    print(output)
    return jsonify(output)


@app.route('/', methods=['GET'])
def submit():
    return '''
    <!doctype html>
    <title>submit new message</title>
    <h1>submit new message</h1>
    <form action="/submit" method="post" enctype=multipart/form-data>
      <input type=text name=msg>
      <input type=submit value=Submit>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
