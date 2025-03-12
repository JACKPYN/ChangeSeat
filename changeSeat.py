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

        # 결과 표시 (테이블 형식)
        for row in seat_table:
            st.write(row)

if __name__ == "__main__":
    main()
