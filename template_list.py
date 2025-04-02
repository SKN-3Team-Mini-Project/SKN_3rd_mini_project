import os
from streamlit_image_select import image_select

TEMPLATE_DIR = "images"

# 이미지 이름 딕셔너리
template_map = {
    "drake.jpg": "드레이크 HotBling 밈",
    "fry.png": "닥치고 내 돈 가져가 밈",
    "muscle.jpg": "공부는 접는다 밈",
    "squirrel.png": "람쥐썬더 밈",
    "chillguy.jpg": "chill guy 밈",
    "disappointed-guy.jpg": "실망한 남자 밈"
}

# 실제 이미지 파일 경로 리스트
image_paths = [os.path.join(TEMPLATE_DIR, fname) for fname in template_map.keys()]
captions = list(template_map.values())

def selected_image_path():
    selected_image_path_info = image_select(
        label="원하는 템플릿 이미지를 클릭하세요",
        images=image_paths,
        captions=captions,
        use_container_width=False
    )

    return selected_image_path_info