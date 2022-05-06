import base64


def pic2str(file, functionName):
    pic = open(file, 'rb')
    content = '{} = {}\n'.format(functionName, base64.b64encode(pic.read()))
    pic.close()

    with open('images.py', 'a') as f:
        f.write(content)

for i in range(8):
    pic2str(f"icon//i{i+1}.png", f"i{i+1}")
    

# image_data = BytesIO(byte_data)
# image = Image.open(image_data)
