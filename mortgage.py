class mortgage:
	def __init__(self,price,rate,term):
		self.price = price
		self.rate = rate
		self.term = term
	def month_pay(self):
		a = 1
		sum = 0
		r = self.rate/12.0
		for i in range(self.term*12):
			sum += a
			a = a/(1+r)
		return self.price/sum
	def __lt__(self,other):
		return self.month_pay() > other.month_pay()

