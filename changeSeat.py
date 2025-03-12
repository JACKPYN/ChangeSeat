import streamlit as st
import random
import time

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

        # 스타일 적용을 위한 CSS
        st.markdown(
            """
            <style>
            .seat-table {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .seat-row {
                display: flex;
                justify-content: center;
                margin-bottom: 10px;
            }
            .seat-item {
                background-color: #f0f2f6;
                padding: 15px;
                text-align: center;
                border-radius: 8px;
                font-weight: 500;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin: 5px;
                width: 80px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # 테이블 형태의 자리 배치 결과 출력
        st.markdown("<div class='seat-table'>", unsafe_allow_html=True)
        for row in seat_table:
            st.markdown("<div class='seat-row'>", unsafe_allow_html=True)
            for student in row:
                st.markdown(f"<div class='seat-item'>{student}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
