from flask import Flask, render_template,request
import random
import requests
import json
from faker import Faker

app = Flask(__name__,static_url_path='/static')

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/lotto')
def lotto():
    #요부분에서 로또번호추첨하는 
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    print(lotto_dict["drwNoDate"])
    
    week_num = []
    week_format_num = []
    drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
    bnusNo = lotto_dict["bnusNo"]
    
    isBonus = False
    
    for num in drwtNo:
        number = lotto_dict[num]
        week_num.append(number)
        print(week_num)
        
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week_format_num.append(num)
        

    
        
     
    num_list = range(1,46)
    pick = random.sample(num_list, 6)
    #pick=[2,6,25,28,30,33]
    
    def intersect (a,b):
        return list(set(a)&set(b))
        
    comp = intersect(pick, week_format_num)
    comp_len = len(comp)
    
    for i in pick:
        if(i==bnusNo):
            isBonus = True
            
    
    
    if comp_len == 6:
        x="1등입니다"
        
    elif comp_len == 5 and isBonus:
        x="2등입니다"
        
    elif comp_len == 5:
        x="3등입니다"
        
    elif comp_len == 4:
        x= "4등입니다"
        
    elif comp_len == 3:
        x = "5등 입니다"
        
    else:
        x = "꽝입니다"
    
    
 
    return render_template("lotto.html",lotto=pick,week_num=week_num, week_format_num=week_format_num,x=x)
    
@app.route('/lottery')
def lottery():
    #로또 정보를 가져온다 & 필요한 것만 고른다.
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    
    #1등 당첨번호를 week 리스트에 넣는다.
    week = []
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week.append(num)
        
    #보너스 번호를 bonus 변수에 넣는다.
    bonus = lotto_dict["bnusNo"]
    
    #임의의 로또 번호를 생성한다.
    pick = random.sample(range(1,46),6)
    
    #비교해서 몇 등인지 저장한다.
    match = len(set(pick) & set(week))
    
    if match==6:
        text = "1등"
    elif match==5:
        if bonus in pick:
            text="2등"
        else:
            text="3등"
    elif match==4:
        text="4등"
    else:
        text="꽝"
    
    #사용자에게 데이터를 넘겨준다.
    return render_template("lottery.html",pick=pick, week=week, text=text)
    
    
@app.route('/ping')
def ping():
    return render_template("ping.html")
    
@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_job = fake.job()
    return render_template("pong.html", html_name=input_name, fake_job=fake_job)
    
@app.route('/hehe')
def hehe():
    input = request.args.get('name')
    fake = Faker('ko_KR')
    fake_color = fake.color_name()
    img_data = random.randrange(1,6)
    return render_template("hehe.html", html_name=input, fake_color=fake_color,img_data = img_data)
    