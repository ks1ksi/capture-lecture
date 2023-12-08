import os
from concurrent.futures import ThreadPoolExecutor

from PIL import Image
from reportlab.pdfgen import canvas


def create_pdf_from_pngs(directory):
    output_pdf_file = os.path.join(
        directory, f"{directory.split(os.path.sep)[-1]}.pdf")
    pdf_filename = os.path.basename(output_pdf_file)

    if os.path.exists(output_pdf_file):
        print(f"{pdf_filename} 파일이 이미 존재합니다.")
        return

    png_files = [f for f in os.listdir(directory) if f.endswith('.png')]
    png_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

    if not png_files:
        directory_name = os.path.basename(directory)
        print(f"{directory_name} 디렉토리에 PNG 파일이 존재하지 않습니다.")
        return

    c = canvas.Canvas(output_pdf_file)

    for png_file in png_files:
        png_path = os.path.join(directory, png_file)
        img = Image.open(png_path)

        # Convert PNG to JPG
        jpg_path = png_path.replace('.png', '.jpg')
        img.convert('RGB').save(jpg_path, 'JPEG', quality=75)

        img_width, img_height = img.size
        c.setPageSize((img_width, img_height))
        c.drawInlineImage(jpg_path, 0, 0, width=img_width, height=img_height)
        c.showPage()

        # Optionally, delete the JPG file after adding it to the PDF
        os.remove(jpg_path)

    c.save()
    print(f">>{pdf_filename} 파일이 생성되었습니다.<<")


def main(directory):
    with ThreadPoolExecutor() as executor:
        for item in os.listdir(directory):
            item_full_path = os.path.join(directory, item)
            if os.path.isdir(item_full_path) and not item.startswith('.'):
                print(f"디렉토리: {item_full_path}")
                executor.submit(create_pdf_from_pngs, item_full_path)
        executor.shutdown(wait=True)


if __name__ == '__main__':
    current_directory = os.getcwd()
    main(current_directory)
