from modules import pdf_to_img as convert
from modules import img_crop as crop
from modules import det_name as detection
from modules import move_dir as move

def main():
    pdf_path = "input/Kadai3-2024.pdf"
    output_dir = "output/temp/"
    file_name = "raw_img"

    print("call: pdf_to_images")
    convert.pdf_to_images(pdf_path, output_dir, file_name)

    image_dir = 'output/temp/'
    output_dir = 'output/code_img/'
    file_name = "code_img"
    crop_area = (118, 0, 1600, 2195)

    print("call: crop")
    crop.crop(image_dir, output_dir, file_name, crop_area)

    image_dir = 'output/temp/'
    output_dir = "output/name_img/"
    file_name = "name_img"
    crop_area = (0, 0, 850, 110)

    print("call: crop")
    crop.crop(image_dir, output_dir, file_name, crop_area)

    input_dir = "output/name_img/"
    output_dir = "output/code_img/"

    print("call: det_name")
    # コード画像のファイル名変更
    detection.det_name(input_dir, output_dir)

    input_dir = "output/name_img/"
    output_dir = "output/split_dir/"
    print("call: make_dir")
    detection.make_dir(input_dir, output_dir)

    target_dir = "output/code_img/"
    destination_dir = "output/split_dir/"
    print("call: move_img_to_dir")
    move.move_img_to(target_dir, destination_dir)
    

if __name__ == "__main__":
    main()