def getMentByUser(name):
    if name == "김형국" or name == "조준영":
        return "☕ 한 잔의 여유, 카페에서 만나요!"
    elif name == "김건휘":
        return ["🥑 즐거운 쇼핑 경험, 슈퍼마켓에서!","🍽 맛있는 즐거움을 위한 완벽한 장소","🎬 문화의 여유로움을 느껴보세요!"]

def getStoreNameByUser(name):
    if name == "김형국" or name == "조준영":
        return ["피플스 카페", "이리로"]
    elif name == "김건휘":
        return ["가자마트 충무로점", "선미네마트", "옛날5가 홍탁과보쌈", "김치만선생 동대필동점", "대한극장", "예스골프"]

def getStoreGpsByUser(name):
    if name == "김형국" or name == "조준영":
        return {
            "store": [
                {
                    "name": "피플스 카페",
                    "latitude": "37.561138",
                    "longitude": "126.996403"
                },
                {
                    "name": "이리로",
                    "latitude": "37.558665",
                    "longitude": "126.996551"
                }
            ]
        }
    elif name == "김건휘":
        return {
            "store": [
                {
                    "name": "가자마트",
                    "latitude": "37.560850",
                    "longitude": "126.997843"
                },
                {
                    "name": "선미네마트",
                    "latitude": "37.558754",
                    "longitude": "126.996215"
                },
                {
                    "name": "옛날5가 홍탁과보쌈",
                    "latitude": "37.561365",
                    "longitude": "126.996671"
                },
                {
                    "name": "김치만선생 동대필동점",
                    "latitude": "37.558949",
                    "longitude": "126.996019"
                },
                {
                    "name": "대한극장",
                    "latitude": "37.561078",
                    "longitude": "126.995259"
                },
                {
                    "name": "예스골프",
                    "latitude": "37.560476",
                    "longitude": "126.995426"
                }
            ]
        }
