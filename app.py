from flask import Flask, render_template

app = Flask(__name__) #​​__name__: 현재 모듈(파일)이름


#127.0.0.1: loop back ip
@app.route('/') #기본 url
def index():
    #return "<h1>Hello</h1>"
    return render_template('index.html')

@app.route('/page')
def page():
    return render_template('page.html')

if __name__ == "__main__": #다른 파일에서는 해당 namespace를 실행시키지 못함
    app.run(debug=True) #debug mod 새로고침시 바로 재실행