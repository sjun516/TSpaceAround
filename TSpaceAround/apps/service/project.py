import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def card_history_analyze_category(name):
    # 엑셀 파일 경로
    excel_file_path = './apps/resource/card.xlsx'

    # 엑셀 파일 불러오기(입력:시간, 출력:대분류)
    df = pd.read_excel(excel_file_path, sheet_name=name, usecols=['시간', '대분류'])
    # '열 이름'에서 12~20으로 시작하는 데이터를 필터링(12~21시 까지의 데이터만 사용)
    dataset = df[df['시간'].astype(str).str.startswith(('12', '13', '14', '15', '16', '17', '18', '19', '20'))]
    # 인덱스 새로 설정
    dataset = dataset.reset_index(drop=True)
    # '열 이름'에서 12~20으로 시작하는 데이터를 12~20으로 변경
    dataset.loc[
        dataset['시간'].astype(str).str.startswith(('12', '13', '14', '15', '16', '17', '18', '19', '20')), '시간'] = \
    dataset['시간'].astype(str).str[:2].astype(int)

    # 데이터 분리
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # 모델 학습
    logreg = LogisticRegression(max_iter=1000)
    logreg.fit(X_train, y_train)

    arr2 = [0] * 9

    if name == "김형국":   # 김형국 12시
        for j in range(9):
            arr2[j] = logreg.predict_proba([[12]])[0][j]
        arr2.sort()
        for i in range(9):
            for j in range(9):
                if arr2[i] == logreg.predict_proba([[12]])[0][j]:
                    arr2[i] = j
        for i in range(9):
            arr2[i] = logreg.classes_[arr2[i]]
    elif name == "김건휘": # 김건휘 18시
        for j in range(9):
            arr2[j] = logreg.predict_proba([[20]])[0][j]
        arr2.sort()
        for i in range(9):
            for j in range(9):
                if arr2[i] == logreg.predict_proba([[20]])[0][j]:
                    arr2[i] = j
        for i in range(9):
            arr2[i] = logreg.classes_[arr2[i]]
    elif name == "조준영": # 김건휘 18시
        for j in range(9):
            arr2[j] = logreg.predict_proba([[20]])[0][j]
        arr2.sort()
        for i in range(9):
            for j in range(9):
                if arr2[i] == logreg.predict_proba([[20]])[0][j]:
                    arr2[i] = j
        for i in range(9):
            arr2[i] = logreg.classes_[arr2[i]]
    arr2.reverse()
    # 카테고리 종류 (9개)
    return arr2

def card_history_analyze_expenditure(name):
    excel_file_path = './apps/resource/card.xlsx'
    # 엑셀 파일 불러오기(입력:시간, 출력:대분류)
    df = pd.read_excel(excel_file_path, sheet_name=name, usecols=['날짜', '금액'])

    res = []

    febData = df[df['날짜'].astype(str).str.startswith(('2022-12'))]
    febData = febData.reset_index(drop=True)
    fr = abs(febData['금액'].sum())
    res.append(str(fr))
    res.append(str(fr - 200000))

    marData = df[df['날짜'].astype(str).str.startswith(('2023-01'))]
    marData = marData.reset_index(drop=True)
    mr = abs(marData['금액'].sum())
    res.append(str(mr))
    res.append(str(mr - 200000))

    aprData = df[df['날짜'].astype(str).str.startswith(('2023-02'))]
    aprData = aprData.reset_index(drop=True)
    ar = abs(aprData['금액'].sum())
    res.append(str(ar))
    res.append(str(ar - 200000))

    print(res)
    return res
