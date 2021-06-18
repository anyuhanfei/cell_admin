from flask import render_template

from . import admin, check_admin_login


@admin.route('/')
@check_admin_login
def homepage():
    return render_template('admin/homepage.html')


@admin.route('/admin/error')
def error():
    return render_template('admin/error.html')
