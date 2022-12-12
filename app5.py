# 웹 대시보드에 이미지, 동영상파일 넣는 방법

import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main():
    img= Image.open('streamlit_data/Image_03.jpg')

    st.image(img)

    st.image(img, use_column_width= True)

    img_url= 'https://s.pstatic.net/shopping.phinf/20221212_7/4b837ad2-42a1-4106-b13e-b4e3aa319e7a.jpg?type=f214_292'
    st.image(img_url)

    # 동영상
    video_file= open('streamlit_data/secret_of_success.mp4', 'rb')
    st.video(video_file)

if __name__ == '__main__':
    main()