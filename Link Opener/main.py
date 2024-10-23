import webbrowser

# Dosya adı (aynı klasörde olduğunu varsayarak)
file_name = 'links.txt'

# Chrome'un tam yolunu belirt
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Web tarayıcısını kaydet
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Dosyayı aç ve linkleri oku
with open(file_name, 'r') as file:
    links = file.readlines()

# Her bir linki Google Chrome'da yeni bir sekmede aç
for link in links:
    # Satır sonu boşluklarını temizle
    link = link.strip()
    # Linki Google Chrome'da yeni bir sekmede aç
    webbrowser.get('chrome').open_new_tab(link)
    break