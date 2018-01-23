class mortgage:
    def __init__(self):
        price = float(input('Enter the house price:'))
        rate = float(input('Enter the interest rate:'))
        term = int(input('Enter the mortgage term in year:'))
        try:
            ratio = float(input('Enter the downpayment ratio in percent:'))/100
        except:
            ratio = 0.2
        self.price = price
        self.rate = rate
        self.term = term
        self.downpayment = price*ratio
        self.loan = self.price - self.downpayment
        a = 1
        sum = 0
        r = self.rate/100/12.0
        for i in range(self.term*12):
            a = a/(1+r)
            sum += a
        self.month_pay = self.loan/sum
    def __lt__(self,other):
        return self.month_pay() > other.month_pay()
    def remain(self,month):
        if month == 0:
            return self.price - self.downpayment
        else:
            return self.remain(month-1)*(1+self.rate/100/12.0) - self.month_pay

