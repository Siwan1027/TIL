import webbrowser

url = 'https://search.naver.com/search.naver?query='

names = ['samsung elec stock price', 'tesla stock price', 'adobe price', 'hmm price']

for name in names:
    webbrowser.open(url + name)
