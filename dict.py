phonebook = {
    "치킨집":"02-000-0000",
    "피자집":"062-123-4567"
}

# print(phonebook["치킨집"])

## 가수 그룹의 딕셔너리를 만들어주세요
## 변수명 : 그룹이름(영어로)
##  key : 이름
## value : 가상의 나이

RedVelvet = {
    "웬디" :21,
    "아이린" :22, 
    "조이" : 23,
    "슬기":24,
    "예리":25
}

Twice = {
    "나연":21,
    "모모":22,
    "지효":23,
    "다현":24
}

#변수명 : idol
#두개의 그룹을 넣어주세요.

idol = {
    "RedVelvet":RedVelvet,
    "Twice":Twice
}

# print(idol)
# print(idol["Twice"]["지효"])

score={
    "수학":50,
    "국어":70,
    "영어":100
}


for key, value in score.items():
    pass
    # print(key)
    # print(value)
    
for key in score.keys():
    print(key)
    
for value in score.values():
    print(value)
    
score_sum = 0
for value in score.values():
    score_sum = score_sum + value
print(score_sum/3)

# #내가 한거
# average = sum(score.values())/len(score)
# print(average)

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

#1. ssfay 를 진행하는 지역(location)은 몇개인가요?

print(len(ssafy["location"]))

#2. python standard library 에 'requests'가 있나요?

a = ssafy["language"]["python"]["python standard library"]
if "requests" in a:
    print(True)
else:
    print(False)

#3. 광주1반의 반장이름을 출력하세요.

print(ssafy["classes"]["gj1"]["class president"])

#4. ssafy에서 배우는 언어들을 출력하세요:dictionary.keys를 활용
for lang in ssafy["language"]

#5. ssafy gj2의 강사와 매니저의 이름을 출력하세요.
