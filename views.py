# coding:utf8
import csv
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "123456"
app.config["UP"] = os.path.join(os.path.dirname(__file__), "static/uploads")


# mass_feature.html是将坐标点一次性全部标注，显示效果与map.html一样，效率更高，但不能缩放移动。
@app.route("/mass/", methods=["GET"])
def mass_feature():
    return render_template("mass_features.html")


# map.html是将坐标逐个显示，可缩放可移动
@app.route("/", methods=["GET"])
def one_by_one():
    return render_template("map.html")


# square.html的标注物是正方形
@app.route("/squ", methods=["GET"])
def square():
    return render_template("square.html")


@app.route("/get_points", methods=["GET"])
def get_points():
    result = []
    with open('/home/zyw/test/flask_map/haidian_meituan.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            # print(line)  # ['116.331398', '39.897445']
            result.append({'x': line[2], 'y': line[1]})

    return jsonify(result)


@app.route("/get_points_b", methods=["GET"])
def get_points_b():
    result = []
    with open('/home/zyw/test/flask_map/haidian_dazhong.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            # print(line)  # ['116.331398', '39.897445']
            result.append({'x': line[2], 'y': line[1]})

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8888)
