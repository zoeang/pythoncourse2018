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
	### Buy Stock----------------------------------------------------------------------
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
				hist_item= 'Bought '+ str(shares)+ ' shares of stock ' + str(stock_object.symbol)+ ' for '+ str(stock_object.price) + ' dollars.'
				self.history_list.append(hist_item)
	### sell Stocks------------------------------------------------------------------------
	def sellStock(self, shares, stock_object):
	if (type(shares)==int)==False: #test that share is an integer
		print "Fractions of shares cannot be sold."
	else: 
		if shares>self.stock[stock_object.symbol]:###check that there are enough to sell
			print "Insufficient number of stocks. No action taken."
		else:
		#sell price
			sprice=uniform(.9,1.2)
			self.cash+=sprice*shares #add cash to portfolio
			self.stock[stock_object.symbol]-=shares
			#append action to self.history_list
			hist_item= 'Sold '+ str(shares)+ ' shares of stock ' + str(stock_object.symbol)+ ' at '+ str(sprice)+ ' per share.'
			self.history_list.append(hist_item)
			if self.stock[stock_object.symbol]==0:
				del self.stock[stock_object.symbol]
#************************************************
# Works up to here
#************************************************
### Buy--------------------------------------------------------
	#### Mutual Fund: float
	def buyMutualFund(self, shares, mutualfund_object):
		#subtract 1/share from cash
		self.cash-=shares
		if self.cash<0:
			print "Insufficient funds. No action taken."
			self.cash+=shares
		else:
			if mutualfund_object.symbol in self.mutualfund:
				self.mutualfund[mutualfund_object.symbol]+=shares #add shares to existing ticker
			else:
				self.mutualfund[mutualfund_object.symbol]=shares #create new key and value
			#append action to self.history_list
			hist_item= 'Bought '+ str(shares)+ ' of mutual fund ' + str(mutualfund_object.symbol)+ ' for '+ str(mutualfund_object.price)+' dollars.'
			self.history_list.append(hist_item)
	
	###sell--------------------------------------------------------
	#### Mutual fund: float
	def sellMutualFund(self, MutualFund, shares):

		###check that there are enough to sell

		#sell price
		mfprice=uniform(.5,1.5)
		###should there be a feature that tells the selling price and asks the user to procede?
		#add cash to portfolio
		self.cash+=mfprice*shares

		#update dictionary
		###how?----------------------------------------------------
		###subtract shares number of MutualFund.symbol from the key in the self.dictionary['mutual funds']
		#append action to self.history_list
		hist_item= 'Sold '+ str(shares)+ ' ' + str(MutualFund.symbol)+ ' at ', str(mfprice), ' per share.'
		self.history_list.append(hist_item)

### print function------------------------------------------------
	def __str__(self):
		portfolio_list=[self.cash, self.mutualfund, self.stocks]
		return '\n'.join(portfolio_list)




#------------------------
#add new key to dictionary
#------------------------
dictionary['newkey']= value
del dictionary['key']