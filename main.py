from Reader import RSS


'''
Założenia:
- Program będzie czytał RSS (Rich Site Summary)
- GUI w którym będzie wprowadzony link RSS, a następnie program będzie wyświetlał podstawowe
informacje o pozycjach
- Czytnik będzie dawał możliwość pokazania większej ilości informacji na dany temat
'''

reader = RSS('https://btgigs.info/rss.php?cats=1,4,5,6,7,10,12,17,19,20,21,26,27,28,29,30,31,32,34,35&language=0&free=0&tracker=0&passkey=3d9d89924ce6cc12672a2b54db9ed526')
reader.show_titles()