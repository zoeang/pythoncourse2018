#Homework 1

#---------------------------------------------------------------
# Define portfolio class
# Inclue variable cash with add and withdraw functions
#---------------------------------------------------------------

#===============================================================
# class MutualFund
#===============================================================
class MutualFund(object):
	def __init__(self, symbol):
		self.symbol=symbol


#===============================================================
#class Stock
#===============================================================

class Stock(object):
	def __init__(self, price, symbol):
		self.price=price
		self.symbol=symbol

from random import uniform #to be used for sale prices

#===============================================================
#class portfolio
#===============================================================
class Portfolio(object): 
	###initialize
	def __init__(self, cash):
		self.cash=float(cash)
		self.stock={}
		self.mutualfund={}
		self.history_list=['Created portfolio containing %d dollars.'%cash] #make list of empty directory; append transactions; history function will print this list
	###add cash------------------------------------------------------
	def addCash(self, cash):  #should this be called cash?
		self.cash += cash
		hist_item='Added cash :'+ str(cash)
		self.history_list.append(hist_item)
	### withdraw cash
	def withdrawCash(self, cash):
		self.cash -= cash
		if self.cash<0: 
			print "Insufficient funds. No action taken."
			self.cash+=cash #add cash back; as if the transaction did not occur
		else: 
			hist_item= 'Withdrew cash : '+ str(cash)
			self.history_list.append(hist_item)#append action to self.history
	### history function-----------------------------------------------
	def history(self):
		print '\n'.join(self.history_list)

	### Buy stock--------------------------------------------------------
	def buyStock(self, shares, stock_object):
			if (type(shares)==int)==False: 
				print "Fractions of shares cannot be bought."
			else:
				self.cash-= shares* stock_object.price
				#test if there is enough money
				if self.cash<0:
					print "Insufficient funds. No action taken."
					self.cash+=shares*stock_object.price
				else:
					if stock_object.symbol in self.stock: #if the stock symbol already exists in the portfolio
						self.stock[stock_object.symbol]+=shares
					else: ##if the stock symbol is new to the portfolio
						self.stock[stock_object.symbol]=shares
					hist_item= 'Bought '+ str(shares)+ ' ' + str(stock_object.symbol)+ ' for '+ str(stock_object.price) + ' dollars.'
					self.history_list.append(hist_item)
	### sell stock--------------------------------------------------------
	def sellStock(self, shares, stock_object):
		if (type(shares)==int)==False: #test that share is an integer
			print "Fractions of shares cannot be sold."
		else: 
			if shares>self.stock[stock_object.symbol]:###check that there are enough to sell
				print "Insufficient number of stocks. No action taken."
			else:
				sprice=uniform(.9,1.2) #sell price
				self.cash+=sprice*shares #add cash to portfolio
				self.stock[stock_object.symbol]-=shares
				#append action to self.history_list
				hist_item= 'Sold '+ str(shares)+ ' ' + str(stock_object.symbol)+ ' at '+ str(sprice)+ ' per share.'
				self.history_list.append(hist_item)
				if self.stock[stock_object.symbol]==0:
					del self.stock[stock_object.symbol]
	#### Buy Mutual Fund--------------------------------------------------
	def buyMutualFund(self, shares, mutualfund_object):
		self.cash-=shares
		if self.cash<0:
			print "Insufficient funds. No action taken."
			self.cash+=shares
		else:
			if mutualfund_object.symbol in self.mutualfund:
				self.mutualfund[mutualfund_object.symbol]+=shares #add shares to existing ticker
			else:
				self.mutualfund[mutualfund_object.symbol]=shares #create new key and value
			hist_item= 'Bought '+ str(shares)+ ' shares of mutual fund ' + str(mutualfund_object.symbol)+ ' for $1.00 per share.'
			self.history_list.append(hist_item)
	###sellf mutual fund---------------------------------------------------
	def sellMutualFund(self, shares, mutualfund_object):
		if (mutualfund_object in self.mutualfund)==False:
			print "No mutual fund shares of %r to sell."%mutualfund_object
		elif shares>self.mutualfund[mutualfund_object] :
			print "Insufficient shares of mutual fund. No action taken."
		else:
			mfprice=uniform(.5,1.5)
			self.cash+=mfprice*shares
			self.mutualfund[mutualfund_object]-=shares
			hist_item= 'Sold '+ str(shares)+ ' of mutual fund %s at %.2f per share.'%(mutualfund_object, mfprice)
			self.history_list.append(hist_item)
			if self.mutualfund[mutualfund_object]==0:
					del self.mutualfund[mutualfund_object]
### print function------------------------------------------------
	def __str__(self): ###this is super ugly
		cash_item='Cash: $%.2f' %self.cash
		stock_item= 'Stocks: %r' %self.stock
		mutualfund_item= "Mutual Funds: %r" %self.mutualfund
		portfolio_list=[cash_item, stock_item, mutualfund_item]
		return '\n'.join(portfolio_list)

#======================================================================
#test
#======================================================================

portfolio=Portfolio(0)
portfolio.addCash(300.50)
s=Stock(20, 'HFH')
portfolio.buyStock(5,s)
mf1=MutualFund("BRT")
mf2=MutualFund("GHT")
portfolio.buyMutualFund(10.3,mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund(3,'BRT')
portfolio.sellStock(1, s)
portfolio.withdrawCash(50)
portfolio.history()

#------------------------
# Comments/concerns
#------------------------
# 1. How to I initialize an object of class Portfolio with no arguments.
#	def __init__(self, cash=None) causes problems with self.cash=float(cash) and self.history, which uses cash
# 2. My print function looks dumb. I know there is a better way to do it, but I don't know how to think through
#	what I need to do to present this best. (This is a coding issue I have in general. "What is the best way to do this thing I don't really understand?")
# 3. I think the argument for sellStock should take a stock object, rather than 
#	the ticker because I made objects of class Stock to have variables of the symbol and price.
#	The sellStock() function relies on the variables to calculate cash to subtract
