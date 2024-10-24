import shutil, os
from natsort import natsorted as nat

def move_img_to_dir(target_dir, dest_dir):

    if not os.path.exists(target_dir):
        return False

    if not os.path.exists(dest_dir):
        return False

    try:
        i = 0
        dest_name = nat(os.listdir(dest_dir))

        for target in nat(os.listdir(target_dir)):
            while True:
                if dest_name[i].replace("_", ".") in target:
                    print(f"{dest_name[i].replace('_', '.')} in {target}")

                    target_path = os.path.join(target_dir, target)
                    dest_path = os.path.join(dest_dir, dest_name[i])

                    shutil.move(target_path, dest_path)
                    break
                else:
                    i += 1

    except Exception as e:
        print(e)
    

def move_img_to(target_dir, dest_dir):

    if not os.path.exists(target_dir):
        return False

    if not os.path.exists(dest_dir):
        return False

    try:

        # target_dir = "output/code_img/" <-複雑
        # destination_dir = "output/split_dir/" <-単純
        dest_name = os.listdir(dest_dir)

        for target in os.listdir(target_dir):
            # print(f"target: {target}")
            # print(f"dest_name: {dest_name}")
            print(target.split("_"))
            num = dest_name.index(target.replace("_", "."))
            print("err")

            target_path = os.path.join(target_dir, target)
            dest_path = os.path.join(dest_dir, dest_name[num])

            print(f"shutil.move({target_path}, {dest_path})")
            #shutil.move(target_path, dest_path)

        return True
    
    except Exception as e:
        print(f"{e}")
        return False