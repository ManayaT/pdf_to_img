from PIL import Image, ImageDraw
import os

def crop_code(image_dir, output_dir, file_name):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    if not os.path.exists(image_dir):
        exit()

    if not os.path.exists(output_dir):
        exit()

    try:
        for i, filename in enumerate(os.listdir(image_dir)):
            if filename.lower().endswith(image_extensions):
                image_path = os.path.join(image_dir, filename)

                image = Image.open(image_path)

                # 領域の座標 (左, 上, 右, 下)
                crop_area = (118, 0, 1600, 2195)

                cropped_image = image.crop(crop_area)

                cropped_image.save(f'{output_dir}{file_name}_{i+1}.png', "PNG")

        return True
    except Exception as e:
        #print(f"{e}")
        return False

def crop_name(image_dir, output_dir, file_name):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    if not os.path.exists(image_dir):
        exit()

    if not os.path.exists(output_dir):
        exit()

    try:
        for i, filename in enumerate(os.listdir(image_dir)):
            if filename.lower().endswith(image_extensions):
                image_path = os.path.join(image_dir, filename)

                image = Image.open(image_path)

                # 領域の座標 (左, 上, 右, 下)
                crop_area = (0, 0, 850, 110)

                cropped_image = image.crop(crop_area)

                cropped_image.save(f'{output_dir}{file_name}_{i+1}.png', "PNG")

        return True
    except Exception as e:
        #print(f"{e}")
        return False