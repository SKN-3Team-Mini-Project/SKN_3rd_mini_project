from PIL import Image, ImageDraw, ImageFont
import os
import cv2

# 각 이미지별 텍스트 위치 프리셋
text_positions = {
    "drake.jpg": [(120, 50), (120, 150)],
    "fry.png": [(55, 25), (55, 230)],
    "muscle.jpg": [(40, 20), (300, 50)],
    "squirrel.png": [(630, 200)],
    "chillguy.jpg": [(40, 20), (40, 180)],
    "disappointed-guy.jpg": [(50, 100), (50, 350)]
}

def add_texts_to_image(image_path, texts, colors, font_sizes, bolds):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font_path = "C:/Windows/Fonts/malgun.ttf"  # 윈도우 기본 한글 폰트

    image_name = os.path.basename(image_path)
    positions = text_positions.get(image_name, [(50, 50)])

    for text, position, color, font_size, bold in zip(texts, positions, colors, font_sizes, bolds):
        font_weight = "bold" if bold else "normal"
        font = ImageFont.truetype(font_path, font_size)
        draw.text(position, text, fill=color, font=font)

    return image

def highlight_positions(image_path, positions):
    image =  cv2.imread(image_path)
    for pos in positions:
        cv2.circle(image, pos, 10, (0, 255, 0), -1)

    return image