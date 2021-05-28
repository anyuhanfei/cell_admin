from flask import Blueprint


admin = Blueprint('admin', __name__)


import apps.admin.login
import apps.admin.homepage
import apps.admin.resource
