import shutil, os

target = "output/code_img/sample01-01.php_16.png"
destination = "output/split_dir/sample01-01_php"
shutil.move(target, destination)

def det_name(target_dir, dest_dir):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    if not os.path.exists(target_dir):
        return False

    if not os.path.exists(dest_dir):
        return False

    try:
        target = os.listdir(dest_dir)

        for i, filename in enumerate(os.listdir(target_dir)):
            if filename.lower().endswith(image_extensions):

                image_path = os.path.join(target_dir, filename)
                target_path = os.path.join(dest_dir, target[i])


        return True
    except Exception as e:
        #print(f"{e}")
        return False