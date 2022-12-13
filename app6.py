import streamlit as st

# 유저에게 데이터를 입력받는 방법

def main():
    # 텍스트를 입력받는 방법
    name= st.text_input('이름을 입력하세요.')
    st.title(name)

    name= st.text_input('자기소개를 입력하세요.', max_chars= 20)
    st.title(name)


    name2= st.text_area('메세지를 입력하세요.')
    st.header(name2)

    year= st.number_input('출생년도를 입력하세요.', 1900, 2020)
    st.subheader(year)

    number= st.number_input('실수를 입력하세요.', 0.5, 100.0, step= 0.5)
    st.text(number)

    # 날짜를 입력받는 방법
    my_data= st.date_input('약속날짜 입력')
    st.text(my_data)

    # 시간을 입력받는 방법
    my_time= st.time_input('약속시간 입력')
    st.write(my_time)

    st.text(my_time.strftime('%H %M'))

    # 비밀번호를 입력받는 방법

    password= st.text_input('비밀번호 입력', type='password')
    st.text(password)

    # 색 입력받기
    color= st.color_picker('색을 입력하세요.')
    st.text(color)


if __name__ == '__main__':
    main()