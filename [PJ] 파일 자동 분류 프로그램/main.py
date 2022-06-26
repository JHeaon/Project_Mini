import sys
import os
import shutil
input = lambda: sys.stdin.readline().rstrip()


def func():
    # os.listdir을 통해 해당 경로에 있는 모든 파일, 폴더를 리스트로 반환
    dirs = './'
    file_list = os.listdir(dirs)

    # 각 확장자에 맞는 폴더 만들기 etc는 예외
    os.mkdir('png')
    os.mkdir('csv')
    os.mkdir('etc')
    os.mkdir('jpg')

    # shutil을 이용하여 각 폴더에 맞게 분류해서 넣어주기
    for file in file_list:
        if file.endswith(".png"):
            shutil.move(file, "./png")
        elif file.endswith(".csv"):
            shutil.move(file, "./csv")
        elif file.endswith(".JPG"):
            shutil.move(file, "./jpg")

if __name__ == "__main__":
    func()
