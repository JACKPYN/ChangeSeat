import streamlit as st
import random
import time
import pandas as pd

def randomize_seats(num_students=24, rows=4, cols=6):
    """학생들의 자리를 무작위로 재배치하고 테이블 형태로 반환하는 함수"""

    students = [f"{i+1}" for i in range(num_students)]
    random.shuffle(students)

    table = []
    for i in range(rows):
        row = students[i * cols: (i + 1) * cols]
        table.append(row)

    return table

def main():
    st.title("자리 배치 랜덤 생성기")

    if st.button("자리 재배치"):
        with st.empty():
            for i in range(3, 0, -1):
                st.write(f"자리 배치 {i}초 전...")
                time.sleep(1)
            st.write("자리 배치 완료!")

        seat_table = randomize_seats()
        st.write("## 자리 배치 결과")

        # pandas DataFrame으로 변환
        df = pd.DataFrame(seat_table)

        # 스타일 적용을 위한 CSS
        st.markdown(
            """
            <style>
            .dataframe td {
                text-align: center; /* 가운데 정렬 */
            }
            .dataframe th {
                display: none; /* 행/열 이름 숨김 */
            }
            .dataframe td:nth-child(3), .dataframe td:nth-child(5) {
                border-left: 2px solid lightgray; /* 간격 띄우기 */
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # 테이블 형태로 결과 표시 (열 이름 숨김)
        st.dataframe(df.style.hide(axis="columns"))

if __name__ == "__main__":
    main()
