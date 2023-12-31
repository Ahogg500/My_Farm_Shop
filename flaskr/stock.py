from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('stock', __name__)

@bp.route('/stock')
@login_required
def index():
    # look at all stock
    return render_template('stock/index.html')
