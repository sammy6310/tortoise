
# 파일의 확장자를 변경하는 파이썬 코드입니다.

import os

def changeExtention(path, ext, chExt, check):
    if ext == chExt:
        return

    for file in os.listdir(path):
        filePath = os.path.join(path, file)
        if os.path.isfile(filePath):
            fileName, fileExt = os.path.splitext(filePath)
            if fileExt[1:] == ext:
                newFile = f'{fileName}.{chExt}'
                if check:
                    print(newFile)
                else:
                    os.rename(filePath, newFile)


if __name__ == '__main__':
    path = input('확장명을 변경하려는 경로를 입력해주세요 : ')
    ext = input('변경하려는 확장명을 입력해주세요 (대소문자 구분) : ')
    chExt = input('변경될 확장명을 입력해주세요 (대소문자 구분) : ')
    
    # 변경 미리 확인
    changeExtention(path, ext, chExt, True)
    answer = input('다음과 같이 변경됩니다 (y/n) : ')

    if answer.lower() == 'y':
        changeExtention(path, ext, chExt, False)
