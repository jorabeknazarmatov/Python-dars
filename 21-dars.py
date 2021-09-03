from googletrans import Translator
tarjimon=Translator()
matn_uz='bugun'
tarjima=tarjimon.translate(matn_uz)
print(tarjima.text)
