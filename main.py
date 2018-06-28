from Reader import RSS


'''
Założenia:
- Program będzie czytał RSS (Rich Site Summary)
- GUI w którym będzie wprowadzony link RSS, a następnie program będzie wyświetlał podstawowe
informacje o pozycjach
- Czytnik będzie dawał możliwość pokazania większej ilości informacji na dany temat
'''

reader = RSS('http://www.reddit.com/r/python/.rss')
reader.show_title_and_link()