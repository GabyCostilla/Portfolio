# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9dgVVwjCT0fvbJr0To1K'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://uas59bvc16i354zm:9dgVVwjCT0fvbJr0To1K@bfh2y9kingnqvbeyakut-mysql.services.clever-cloud.com:3306/bfh2y9kingnqvbeyakut'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
