import console
import webbrowser
import requests
from bs4 import BeautifulSoup


TOP_URL = 'https://kinro.ntv.co.jp'
LINEUP_URL = 'https://kinro.ntv.co.jp/lineup'


def GetLineupInfo():
	
	req = requests.get(LINEUP_URL)
	soup = BeautifulSoup(req.text, 'html.parser')
	
	lineup_text = soup.find(attrs={'id': 'after_lineup'})
	
	cap_list = lineup_text.find_all(attrs={'class': 'cap'})
	
	lineup_list = [{'Date': cap.find(attrs={'class': 'date'}).get_text(), 'Title': cap.find(attrs={'class': 'title'}).get_text()} for cap in cap_list]
	
	return lineup_list 
	

def GetDisplayText(lineup_list):
	
	display_text = ''
	
	for lineup in lineup_list:
		lineup_text = '◆' + lineup['Date'] + '\n' + lineup['Title'] + '\n\n'
		
		display_text += lineup_text
	
	return display_text



if __name__ == '__main__':
	
	lineup_list = GetLineupInfo()
	
	display_text = GetDisplayText(lineup_list)
	
	res = console.alert(display_text, 'サイトを開きますか？', 'はい', 'いいえ', hide_cancel_button=True)
	
	if res == 1:
		webbrowser.open(TOP_URL)
	else:
		# launcherアプリを利用してホーム画面に戻る
		webbrowser.open('launcher://homescreen')