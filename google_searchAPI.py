from googleapiclient.discovery import build
my_api = 'JSON API KEY'
my_csk = 'ARAMA MOTORU KIMLIGI'

def google_arama(aranacak_text, api_anahtari, motor_kimligi, **kwargs):
  
  with  build('customsearch','v1',developerKey = api_anahtari) as service:

        arama_sonucu = service.cse().list(q=aranacak_text,cx = motor_kimligi,**kwargs).execute()
        return arama_sonucu


sonuc_metni = google_arama(aranacak_text='NASA',api_anahtari=my_api,motor_kimligi=my_csk)

veri = sonuc_metni['items']

print(veri[0].get('title')) ## başlık bilgisi için
print(veri[0].get('link')) ## link bilgisi için
print(veri[0].get('snippet')) ## özet bilgisi için
