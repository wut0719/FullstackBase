#!/usr/bin/env
# -*- coding: utf-8 -*-
from flask import Flask, render_template, make_response

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route("/", methods=['GET'])
def index():
    response = make_response(render_template("index.html"),200)
    response.headers["Cache-Control"] = 'no-store'
    return response

if __name__ == "__main__":
    app.run()