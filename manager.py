from modules import convertToImage as convert

def main():
    pdf_path = "input/Kadai01.pdf"
    output_path = "output/02/"
    file_name = "test"

    convert.pdf_to_images(pdf_path, output_path, file_name)

if __name__ == "__main__":
    main()