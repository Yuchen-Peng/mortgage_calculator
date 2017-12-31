class mortgage:
#	def __init__(self,price,rate,term):
	def __init__(self):
		price = float(input('Enter the house price:'))
		rate = float(input('Enter the interest rate:'))
		term = int(input('Enter the mortgage term in year:'))
		self.price = price
		self.rate = rate
		self.term = term
	def loan(self):
		try:
			ratio = float(input('Enter the downpayment ratio in percent:'))/100
		except:
			ratio = 0.2
		return self.price * (1-ratio)
	def month_pay(self):
		a = 1
		sum = 0
		r = self.rate/12.0
		for i in range(self.term*12):
			sum += a
			a = a/(1+r)
		return self.loan()/sum
	def __lt__(self,other):
		return self.month_pay() > other.month_pay()

