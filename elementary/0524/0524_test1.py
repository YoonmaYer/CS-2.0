heroes = []
heroes.append("아이언맨")
heroes.append("닥터 스트레인지")
heroes.append("헐크")
heroes.append("스칼렛 위치")
heroes.append("스파이더맨")

heroes.insert(1,"배트맨")
heroes.remove("스칼렛 위치")
heroes.remove("헐크")
heroes.remove("스파이더맨")
if "배트맨" in heroes:
    heroes.remove("배트맨")
del heroes[0]
heroes.pop()
print(heroes)
