from tkinter import messagebox
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

	lineup_list = [{
			'Date' : cap.find(attrs={'class': 'date'}).get_text(),
			'Title': cap.find(attrs={'class': 'title'}).get_text()
		} for cap in cap_list]
	
	return lineup_list


def GetDisplayText(lineup_list):

	display_text = ''

	for lineup in lineup_list:
		lineup_text = '◆{}\n{}\n\n'.format(lineup['Date'], lineup['Title'])
		display_text += lineup_text
	
	return display_text


def HiddenTkRootWindow():

	from tkinter import Tk
	import platform

	# ダイアログ用のルートウィンドウの作成
	root = Tk()
	# ウィンドウサイズを0にする（Windows用の設定）
	root.geometry("0x0")
	# ウィンドウのタイトルバーを消す（Windows用の設定）
	root.overrideredirect(1)
	# ウィンドウを非表示に
	root.withdraw()
	system = platform.system()


if __name__ == '__main__':

	lineup_list = GetLineupInfo()
	display_text = GetDisplayText(lineup_list)
	
	HiddenTkRootWindow()
	ret = messagebox.askyesno('完了', '{}{}'.format(display_text, 'サイトを開きますか？'))
	
	if ret == True:
		webbrowser.open(TOP_URL)
	
