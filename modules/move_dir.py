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
        target = os.listdir(target_dir)
        modified_target = [name.replace(".", "_") for name in target]

        for dest in os.listdir(dest_dir):
            modified_dest = dest.replace(".", "_")
            indices = [i for i, s in enumerate(modified_target) if modified_dest in s]

            # for element in indices:
            #     temp2 = dest.replace(".", "_")
            #     print(f"{temp2} : {modified_target[element]}")

            dest_path = os.path.join(dest_dir, dest)

            for index in indices:
                target_path = os.path.join(target_dir, target[index])
                shutil.move(target_path, dest_path)

        return True
    
    except Exception as e:
        print(f"{e}")
        return False