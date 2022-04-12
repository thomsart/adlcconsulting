""" !/usr/bin/env python3
    -*- coding: utf-8 -*-

This module is use to execute the server of the site www.thomsart.tech """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """ The path to return the home template """

    return render_template('home.html')


@app.route('/mentions_legales')
def mentions_legales():
    """ The path to return the mentions legales template """

    return render_template('mentions_legales.html')


if __name__ == '__main__':
    app.run()