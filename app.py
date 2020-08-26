from flask import Flask
import config

# 创建一个flask对象
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')  # 装饰器
def hello_world():
    # a = 1
    # b = 0
    # c = a/b
    return 'Hello World!'

#
if __name__ == '__main__':
    app.run()
