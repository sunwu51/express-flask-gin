from flask import Flask,request
import json

app = Flask(__name__)
# 路径参数 查询字符串 表单 json
# 纯文本 json 
@app.route('/path/<id>')
def f1(id):
    return id
@app.route('/querystring')
def f2():
    a = request.args.to_dict().get("a")
    return a
@app.route('/form',methods=['post'])
def f3():
    b = request.form.to_dict().get("b")
    return b
@app.route('/json',methods=['post'])
def f4():
    jsonstr = request.data.decode('utf-8')
    c =json.loads(jsonstr).get("c")
    return str(c)
@app.route('/')
def hello():
    print(request.headers.get('a'))
    return {'a':11,'b':'ffffff'},200,{"f":"g"}

@app.route('/post',methods=['post'])
def hello2():
    return "hello flask"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=3002)