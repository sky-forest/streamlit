import streamlit as st

def main():
    st.title('웹 대시보드')

    print('웹 대시보스')

    st.text('웹 대시보드 개발하기')

    st.header('이 영역은 헤더영역')

    st.subheader('이 영역은 서브헤더영역')

    st.success('성공하여 메시지를 보여줄때')

    st.warning('경고 메세지를 보여주고 싶을때')

    st.info('정보 메세지를 보여주고 싶을때')

    st.error('문제가 발생했음을 보여주고싶을때')

    # 파이썬의 함수들의 설명을 보여주고싶을 때

    st.help(sum)


if __name__ == '__main__':
    main()