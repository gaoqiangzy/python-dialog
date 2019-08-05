import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.sina.com.cn/')
res.encoding='utf-8'

# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
header = soup.select('h1') #查找所有h1标签
selectById = soup.select('#xy-impcon')
selectByClass=soup.select('.list-a')

print(header)
print(selectById)
print(selectByClass)


