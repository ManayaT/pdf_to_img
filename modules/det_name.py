from PIL import Image
import pytesseract
import os

def det_name(image_dir, target_dir):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    if not os.path.exists(image_dir):
        exit()

    if not os.path.exists(target_dir):
        exit()

    try:
        target = os.listdir(target_dir)

        for i, filename in enumerate(os.listdir(image_dir)):
            if filename.lower().endswith(image_extensions):

                image_path = os.path.join(image_dir, filename)
                target_path = os.path.join(target_dir, target[i])
                img = Image.open(image_path)
                text = pytesseract.image_to_string(img, lang='eng')

                os.rename(target_path, f"{target_dir}{text}_{i+1}.png")

        return True
    except Exception as e:
        #print(f"{e}")
        return False