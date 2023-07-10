# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 16:02:55 2023

@author: 91748
"""

#pip install fastapi uvicorn
import uvicorn 
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def index():
    return {'message': 'Hello, World'}
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome ': f'{name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload