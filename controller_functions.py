from flask import Flask, render_template, redirect, request, session, flash, send_from_directory, url_for
from models import Users
from config import db, app
from flask_sqlalchemy import SQLAlchemy

import os
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'png'])


def index():
    print(f"ROUTE: index")
    return render_template("index.html")





