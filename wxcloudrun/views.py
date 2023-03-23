# -*- coding:utf-8 -*-

from flask import Flask, render_template, request

import json
import requests

from datetime import datetime
import time


openaiurl = 'https://service-0l5yf4x2-1251744023.sg.apigw.tencentcs.com/v1/chat/completions'
key = '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'

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])

def generate():
    # 获取用户输入的信息
    last_name = request.form.get("last_name")
    first_name = request.form.get("first_name")
    birth_year = request.form.get("birth_year")
    birth_month = request.form.get("birth_month")
    birth_day = request.form.get("birth_day")
    birth_hour = request.form.get("birth_hour")
    gender = request.form.get("gender")
    prompt = f"请您做我的算命助手，我给你一份资料，你帮我用中国传统文化（周易、八字、五行、命理、星座、属相）进行测算，每一项给出不低于30字的内容，资料如下：{last_name}{first_name}({gender})出生于{birth_year}年{birth_month}月{birth_day}日{birth_hour}时。只要按要求回复我，没有指令的情况下不要解释任何内容。"
#    prompt = request.form.get("prompt") # 获取用户输入的文本

    data  = {
            "messages": [{"role": "user", "content": prompt}],
            "model": "gpt-3.5-turbo",
           }    
    headers = {"Authorization": "Bearer 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","Content-Type": "application/json; charset=UTF-8"}
    print(data )
    data_json=json.dumps(data)
    print(type(data_json ))
    
    rsp = requests.post(openaiurl,  headers=headers,data=data_json)
    print(rsp)
    rsp_data = rsp.json()
    message_content = rsp_data["choices"][0]["message"]["content"]
    print(rsp.status_code)
    print(rsp_data)
    print (rsp_data)
    #ad_list = rsp_data["data"]["list"] 
    
    return message_content
    

    
