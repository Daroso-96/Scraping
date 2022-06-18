import requests
from lxml import html
encabezados = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
url = 'https://www.wikipedia.org/'
result = requests.get(url, headers=encabezados)
parse = html.fromstring(result.text)
#idiomas = parse.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")
#for idioma in idiomas:
    #print(idiomas)
idiomas = parse.find_class('central-featured-lang')
for idioma in idiomas:
 print(idioma.text_content())

