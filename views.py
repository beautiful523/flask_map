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


@app.route("/get_points", methods=["GET"])
def get_points():
    # 往CSV文件里面写入数据
    # csv_file = open('csv_test.csv', 'w')
    # writer = csv.writer(csv_file)
    # data = [
    #     (116.331398, 39.897445),
    #     (116.331398, 39.997445)
    # ]
    # writer.writerows(data)
    # csv_file.close()

    # 从CSV文件里面读取数据
    # 返回的result为如下格式：
    # [
    #     {
    #         "x": "116.331398",
    #         "y": "39.897445"
    #     },
    #     {
    #         "x": "116.331398",
    #         "y": "39.997445"
    #     }
    # ]
    result = []
    with open('haidian_dazhong.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            # print(line)  # ['116.331398', '39.897445']
            result.append({'x': line[2], 'y': line[1]})
    # with open('haidian_meituan.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for line in reader:
    #         # print(line)  # ['116.331398', '39.897445']
    #         result.append({'x': line[2], 'y': line[1]})

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8888)
