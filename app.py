from flask import Flask, request, jsonify
import wolframalpha
import wikipedia

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def return_request():
    d = {}
    input_chr = int(request.args['query'])
    answer = f'{input_chr**2}'
    d['output'] = answer
    return jsonify(d)


@app.route('/search', methods=['GET'])
def search():
    output = {}
    client = wolframalpha.Client('wolframalpha_key')
    query = str(request.args['query'])
    res = client.query(query)
    wolframalpha_answers = []
    for i in res.results:
        wolframalpha_answers.append(i.text)
    output['wolframalpha answers'] = wolframalpha_answers

    print(query)
    try:
        page = wikipedia.page(query)
    except:
        page = None
    wiki_search_results = wikipedia.search(query)
    wikipedia_answers = {}
    wikipedia_answers['search'] = wiki_search_results
    if page != None:
        wikipedia_answers['page'] = {'title': page.title,
                                    'content': page.content, 'summary': page.summary}
    else:
        wikipedia_answers['page'] = {'title':'page not found','content':'','summary':''}
    output['wikipedia answers'] = wikipedia_answers

    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
