import streamlit as st
import os
import template_list as tl
import text_input as ti


def main():
    st.title("🖼️ 짤/밈 생성기 - 템플릿 클릭 선택")
    
    selected_image_path = tl.selected_image_path
    
    if selected_image_path:
        selected_name = os.path.basename(selected_image_path)
        st.markdown(f"### ✅ 선택된 템플릿: {tl.template_map[selected_name]}")
        
        positions = ti.text_positions.get(selected_name, [(50, 50)])
        highlighted_image = ti.highlight_positions(selected_image_path, positions)
        st.image(highlighted_image, caption="텍스트 삽입 가능 위치 표시", use_column_width=True)
        
        texts, colors, font_sizes, bolds = [], [], [], []
        st.sidebar.subheader("📝 텍스트 설정")
        
        for i in range(len(positions)):
            text = st.sidebar.text_input(f"텍스트 {i+1}")
            color = st.sidebar.color_picker(f"텍스트 {i+1} 색상", "#FFFFFF")
            font_size = st.sidebar.slider(f"텍스트 {i+1} 크기", 10, 100, 30)
            bold = st.sidebar.checkbox(f"텍스트 {i+1} 굵게", value=False)
            
            texts.append(text)
            colors.append(color)
            font_sizes.append(font_size)
            bolds.append(bold)
        
        if st.button("Generate Image"):
            meme_image = ti.add_texts_to_image(selected_image_path, texts, colors, font_sizes, bolds)
            
            st.image(meme_image, caption="Generated Meme", use_column_width=True)
            
if __name__ == "__main__":
    main()