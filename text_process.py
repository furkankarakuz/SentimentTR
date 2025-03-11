import re
from trnlp import TrnlpWord

stop_words = ['şu', 'şey', 'ama', 'ise', 'ürün', 'daha', 'neden', 'yani', 'de', 'niçin', 'sanki', 'ya', 'nerede', 'urun', 'da', 'tarafından', 'kez', 'hem', 'olarak', 'iki', 'nereye', 'diye', 'az', 'veya', 'acaba', 'ilk', 'en', 'nasıl', 'biz', 'nerde', 'aslında', 'hepsi', 'o', 'gibi', 'hiç', 'defa', 'kim', 'mı', 'mu', 'ki', 'bu', 'için', 'birşey', 'ile', 'hep', 'belki', 'niye', 've', 'sonra', 'çünkü', 'eğer', 'bir', 'tüm', 'bır', 'ne', 'birkaç', 'mü', 'çok', 'biri', 'her', 'siz', 'bazı']
turkish_map = str.maketrans("ÇĞIÖŞÜİ", "çğıöşüi")


stop_words = [stop_word.translate(turkish_map) for stop_word in stop_words]


def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.translate(turkish_map)
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text


def error_check(text):
    obj = TrnlpWord()
    error_word_list = []
    for word in text.split():
        obj.setword(word)
        if obj.get_stem == "":
            error_word_list.append(word)
    return error_word_list
