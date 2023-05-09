from expireddomains import User
keyword = input('Please enter keyword:\n- ')

user = User(keyword)
login = user.get_cookie()
if login == False:
    print('USER CRIDENTIALS ARE WRONG')
    quit()
data = user.get_result_data()
if data == False:
    print('No records matching keyword')
    quit()
user.scrape()