import qrcode

def generate_qrcode():
    url = input("Enter a text or URL: ")
    filename = input("Enter the file name: ")

    img = qrcode.make(url)
    img.save(filename)

    print(f"QRcode saved as {filename}")

generate_qrcode()