from flask import Flask,request,jsonify

app = Flask(__name__)
@app.route('/test',methods = ['GET'])
def return_request():
    d={}
    input_chr = int(request.args['query'])
    power = int(request.args['power'])
    answer = f'{input_chr**power}'
    d['output'] = answer
    return jsonify(d)

if __name__ == '__main__':
    app.run(port = 8000)