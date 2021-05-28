from flask import render_template, request, session

from . import admin
from configs.common import return_data


@admin.route('/')
def homepage():
    return render_template('admin/homepage.html')
