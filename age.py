driveing = input('請問你有沒有開過車?')
if driveing != '有' and driveing != '沒有':
	print('只能輸入  有/沒有')
	raise SystemExit # 系統離開的錯誤
age = input('請問你的年齡?')
age = int(age)
if driveing =='有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼會有開過車')
elif driveing =='沒有':
	if age >=18:
		print('你可以考駕照了啊,怎麼還不去考')
	else:
		print('很好,再過幾年就可考駕照了')
#else:
#	print('只能輸入 有/沒有')
#因為有加入 raise SystemExit 所以可以不用這行了

