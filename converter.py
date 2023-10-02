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
        img_width, img_height = img.size

        c.setPageSize((img_width, img_height))
        c.drawInlineImage(png_path, 0, 0, width=img_width, height=img_height)
        c.showPage()

    c.save()
    print(f">>{pdf_filename} 파일이 생성되었습니다.<<")


def main(directory):
    with ThreadPoolExecutor() as executor:
        # 현재 디렉토리의 모든 항목을 가져옵니다.
        for item in os.listdir(directory):
            item_full_path = os.path.join(directory, item)

            # 항목이 디렉토리이고 숨김 폴더가 아니라면 처리합니다.
            if os.path.isdir(item_full_path) and not item.startswith('.'):
                executor.submit(create_pdf_from_pngs, item_full_path)


if __name__ == '__main__':
    current_directory = os.getcwd()
    main(current_directory)
