from flask import Blueprint, render_template

blueprint = Blueprint("admin", __name__)


@blueprint.route("/")
def admin():
    test_data = [
        ["0801", "たけし", "takesi@gmail.com", "ともひさ"],
        ["0830", "ゆみこ", "superyumiko@gmail.com", "マイケルたけし"],
    ]
    if len(test_data) < 10:
        for _ in range(20 - len(test_data)):
            test_data.append(["0000", " ", " ", " "])
    return render_template("admin.html", datas=test_data)
