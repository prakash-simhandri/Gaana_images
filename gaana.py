from bs4 import BeautifulSoup
from urllib.request import urlopen
import pprint,webbrowser,os.path
import urllib.request
import tkinter as tk
from PIL import ImageTk, Image
# * * * * * * * * * * * * * * * * *#

gaana_com_url=urlopen('https://gaana.com/')
soup=BeautifulSoup(gaana_com_url,'html.parser')
h2_link=soup.find('h2',{'id':'themechange','class':'themechange'}).find('a').get('href')
top_charts=('https://gaana.com'+h2_link)
link=urlopen(top_charts)
next_soup=BeautifulSoup(link,'html.parser')
gaana_ul=next_soup.find('ul',class_='content-container artworkload clearfix a-list')
gaana_li=gaana_ul.findAll('div',class_='card_layout_data')
def scrape_songs_names(gaana):
	All_Songs_list=[]
	number=1
	for tital in gaana:
		print(number, tital.text.strip())
		number+=1
		All_Songs_list.append('https://gaana.com'+tital.find('a').get('href'))
	return(All_Songs_list)
All_type_songs=scrape_songs_names(gaana_li)
# pprint.pprint(All_type_songs)

def scrape_songs_link(gaana):
	user_chose=int(input('#########   What du you want to lesten  ########## >'))
	get_url=urlopen(gaana[user_chose-1])
	top_songs=BeautifulSoup(get_url,'html.parser')
	songs_total_list=top_songs.find('div',class_='s_c')
	gaana_names=songs_total_list.findAll('div',class_='playlist_thumb_det')
	images=songs_total_list.findAll('div',class_='playlist_thumb')
	count=1
	song_link=[]
	for songs_name in gaana_names:
		song_title=songs_name.find('a').get_text()
		song_link.append(songs_name.find('a').get('href'))
		print(count,song_title)
		count+=1
	images_index=0
	for img_ in images:
		img_link=img_.find('img',class_='img').get('data-src')
		caleat=''
		for id_ in img_link[::-1]:
			if '_' != id_:
				caleat+=id_
			else:
				break
		full_name=(caleat[::-1])
		if os.path.exists(full_name):
			images_index+=1
			img_user=(input('you se a {} image ?[yes/no] >'.format(images_index)))
			if 'yes' == img_user:
				window = tk.Tk()
				window.title("Join")
				window.geometry("300x300")
				window.configure(background='grey')
				img = ImageTk.PhotoImage(Image.open(full_name))
				panel = tk.Label(window, image = img)
				panel.pack(side = "bottom", fill = "both", expand = "yes")
				window.mainloop()
			else:
				break
		else:
			urllib.request.urlretrieve(img_link,full_name)


	return song_link
All_songs_links=scrape_songs_link(All_type_songs)
# print(All_songs_links)


def play_the_song(gaana):
	second_user_chose=int(input('~~~~~~~~~~~~~  Which song do you want to listen to  ~~~~~~~~~~~~~ >'))
	play=webbrowser.open(gaana[second_user_chose-1])
	print(play)

play_the_song(All_songs_links)