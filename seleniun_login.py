from selenium import webdriver
import time

def login(username,password):
	# url= 'https://passport.cnblogs.com/user/signin'
	# url = 'https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F'
	url='https://www.zhihu.com/signup?next=%2F'
	driver=webdriver.Firefox()
	driver.get(url)

	login_span=driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[2]/span').click()
	# name_input =driver.find_element_by_id('input1')
	name_input=driver.find_element_by_name("username")
	# pass_input =driver.find_element_by_id('input2')
	pass_input=driver.find_element_by_name("password")
	# login_button =driver.find_element_by_id('signin')
	login_button=driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button")

	name_input.clear()
	name_input.send_keys(username)
	time.sleep(0.5)
	pass_input.clear()
	pass_input.send_keys(password)
	time.sleep(0.5)
	login_button.click()

	# driver.close()

if __name__=="__main__":
	# user="kuanghai"
	# pw="zxc123456.."
	user="18933120678"
	pw="chj2338888::"
	login(user,pw)