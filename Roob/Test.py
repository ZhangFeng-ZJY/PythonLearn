##  实现自动搜索
##  定义搜索网址


##测试网址：：
bing_url = "https://cn.bing.com/?toWww=1&redig=57ADA88975DC447CA945FBB983FB12C1"

#需要登陆的页面。
login_url = ''

#定位目标页面
target_url = ''

class Concert:
	def _init_(self):
		self.status = 0		  #状态 ； 0 origin time
		self.login_method = 1 #

		#############

def choose_ticket(self):
	if self.status == 2:
		print("="*30)
		print("###开始进行日期及票价选择###")
		while self.diver.title.find('确认订单') == -1:
			try:
				buybutton = self.driver.find_element_by_class_name('buybtn').text
				if buybutton == "提交缺货登记":
					#改变现有状态
					self.status = 
