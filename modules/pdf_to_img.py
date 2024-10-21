from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_dir, file_name):

        if not ".pdf" in pdf_path:
            exit()

        if not os.path.exists(pdf_path):
            exit()

        if not os.path.exists(output_dir):
            exit()

        try:
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                image.save(f'{output_dir}{file_name}_{i+1}.png', 'PNG')

            return True
        except Exception as e:
            #print(f"{e}")
            return False