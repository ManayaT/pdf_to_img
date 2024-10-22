from modules import pdf_to_img as convert
from modules import img_crop as crop
from modules import det_name as detection

def main():
    pdf_path = "input/Kadai01.pdf"
    output_dir = "output/temp/"
    file_name = "raw_img"

    convert.pdf_to_images(pdf_path, output_dir, file_name)

    image_dir = 'output/temp/'
    output_dir = 'output/code_img/'
    file_name = "code_img"
    crop_area = (118, 0, 1600, 2195)

    crop.crop(image_dir, output_dir, file_name, crop_area)

    image_dir = 'output/temp/'
    output_dir = "output/name_img/"
    file_name = "name_img"
    crop_area = (0, 0, 850, 110)

    crop.crop(image_dir, output_dir, file_name, crop_area)

    input_dir = "output/name_img/"
    output_dir = "output/code_img/"

    # コード画像のファイル名変更
    detection.det_name(input_dir, output_dir)

if __name__ == "__main__":
    main()