import os

from PIL import Image
from reportlab.pdfgen import canvas

# 현재 디렉토리와 하위 디렉토리에 있는 PNG 파일을 모두 찾습니다.
current_directory = os.getcwd()
png_files = [f for f in os.listdir(current_directory) if f.endswith('.png')]

# sort png file by name. 1.png, 2.png, 3.png, ...10.png, 11.png, ...
png_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

if not png_files:
    print("현재 디렉토리에 PNG 파일이 없습니다.")
    exit()

# print name of png files
for png_file in png_files:
    print(png_file)

# PDF 파일을 생성합니다. 파일 이름은 현재 디렉토리명으로 합니다.
output_pdf_file = f"{current_directory.split(os.path.sep)[-1]}.pdf"
c = canvas.Canvas(output_pdf_file)

for png_file in png_files:
    # PNG 파일을 엽니다.
    img = Image.open(png_file)
    img_width, img_height = img.size

    # PDF 페이지를 PNG 이미지 크기에 맞게 설정합니다.
    c.setPageSize((img_width, img_height))
    # PNG 이미지를 PDF에 추가합니다.
    c.drawInlineImage(png_file, 0, 0, width=img_width, height=img_height)
    # 다음 페이지를 추가합니다.
    c.showPage()

# PDF 파일을 저장합니다.
c.save()

print(f"{output_pdf_file} 파일이 생성되었습니다.")
