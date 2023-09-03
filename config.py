import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    
    #f0070b9d436a04dc77d6337eb127638b
    