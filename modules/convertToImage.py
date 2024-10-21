from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_path, file_name):
        #pdf_path = 'input/Kadai01.pdf'
        #output_path = "2"

        if not ".pdf" in pdf_path:
            exit()

        if not os.path.exists(pdf_path):
            exit()

        if not os.path.exists(output_path):
            exit()

        try:
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                image.save(f'{output_path}{file_name}_{i+1}.png', 'PNG')

            return True
        except Exception as e:
            #print(f"{e}")
            return False