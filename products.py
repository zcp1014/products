products = []
while  True:
	pr = input('請輸入商品名稱')
	if pr == 'q':
		break
	pi = input('請輸入價格')
	p = []	
	p.append(pr)
	p.append(pi)
	products.append(p)
print(products)	

with open('products.csv', 'w') as file:
	for p in products:
		file.write(p[0] + ',' + p[1] + '\n')