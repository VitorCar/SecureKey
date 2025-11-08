import qrcode


def view_qrcode(password_obtained):
    img = qrcode.make(f"SENHA SEGURA:  {password_obtained}", box_size=6)
    type(img)
    return img.save('image/image_qrcode.png')
