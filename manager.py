from modules import pdf_to_img as convert
from modules import img_crop as crop

def main():
    pdf_path = "input/Kadai01.pdf"
    output_path = "output/01/"
    file_name = "test"

    convert.pdf_to_images(pdf_path, output_path, file_name)

    image_dir = 'output/01/'
    output_dir = 'output/test/'

    crop.crop_code(image_dir, output_dir, file_name)

    output_dir = 'output/test/'
    output_dir = "output/file_name_test/"
    file_name = "name"

    crop.crop_name(image_dir, output_dir, file_name)

if __name__ == "__main__":
    main()