
file = open('csharp-featured.png', 'rb+')
content = file.read()
content += b'oldu goy koynekde olacagam!'
file.close()
new_file = open('csharp-featured.png', 'wb')
new_file.write(content)
new_file.close()