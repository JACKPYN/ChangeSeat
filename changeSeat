import streamlit as st
import random

def randomize_seats(num_students=24, rows=4, cols=6):
    """학생들의 자리를 무작위로 재배치하고 테이블 형태로 반환하는 함수"""

    students = [f"학생{i+1}" for i in range(num_students)]
    random.shuffle(students)

    # 테이블 형태로 학생 목록 재구성
    table = []
    for i in range(rows):
        row = students[i*cols : (i+1)*cols]
        table.append(row)

    return table

def main():
    st.title("자리 배치 랜덤 생성기")

    if st.button("자리 재배치"):
        seat_table = randomize_seats()
        st.write("## 자리 배치 결과")

        # 테이블 형태로 결과 표시
        for row in seat_table:
            cols = st.columns(6)
            for i, student in enumerate(row):
                cols[i].write(f"{student}")

if __name__ == "__main__":
    main()
