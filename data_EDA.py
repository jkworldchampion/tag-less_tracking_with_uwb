import pandas as pd
import numpy as np

# 데이터 추출하기
def get_data(name, file):
    data = open(file, 'r')
    data_log = []

    for line in data:
        if len(line) > 1000:   # cir data를 갖는 line은 1016개의 데이터를 갖기에 1000개 이상의 데이터를 갖는 line만 추출
            data_log.append(line)

    print("len(data_log): ", len(data_log)) # 데이터 추출 개수 확인

    processed_data = []  # 데이터 처리를 위한 리스트

    for i in data_log:
        if any(c.isalpha() for c in i):
            index = i.find("RSMPL")  # CIR log가 생성되는 과정에서 끝부분이 RSMPL(01)로 끝나는 Line이 생성되는 경우가 있음
            # RSMPL이라는 문자를 찾지 못하면 -1을 반환
            if index != -1:
                i = i[index+len("RSMPL")+4:]  # RSMPL 다음의 4개의 문자를 제외한 데이터를 추출
                processed_data.append(i)
            else:
                # 문자열이 없는 경우 바로 추가
                processed_data.append(i)
        # 알파벳이 없는 경우 바로 추가
        else:
            processed_data.append(i)
    
    data_log = processed_data # 데이터 처리된 데이터를 data_log에 저장
    raw_data = []  # 데이터 처리를 위한 리스트
    for i in range(len(data_log)):
        data_sample = [int(x) for x in data_log[i].strip().split(",") if x]  # 데이터를 ,로 분리, int로 변환하여 list로 저장
        raw_data.append(data_sample)
    
    count = 0
    for i in range(len(raw_data)):
        if len(raw_data[i]) > 1016:
            count += 1
    
    print("not 1016: ", count)  # 1016개의 데이터를 갖지 않는 데이터 확인

    if count != 0:
        for i in range(len(raw_data)):
            if len(raw_data[i]) > 1016:
                raw_data[i] = raw_data[i][1016:]  # 1016개의 데이터를 넘는 경우 중첩된 경우이므로 후자를 선택

    count = 0
    for i in range(len(raw_data)):
        if len(raw_data[i]) != 1016:
            count += 1
    print("after: ",count)  # 잘 변경 되었는지 확인
    if count != 0:
        print("error, 잘못 처리된 데이터가 있습니다.")  # 없을거 같지만 그래도 만듦, 그래서 어딘지까지는 안 알려줌
        return

    raw_data = pd.DataFrame(raw_data)  # 데이터프레임으로 변환

    # CIR data를 절대값처리한 후 정규화한 형태로 변환
    abs_normalized_data = raw_data.apply(lambda x: x*x, axis=1)  # 제곱 처리  
    abs_normalized_data = abs_normalized_data.apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=1)  # 정규화

    
    abs_normalized_data.to_csv(name)
    print(len(raw_data))


# Functions to extract raw, unnormalized data
# 정규화되지 않은 raw 데이터를 추출하는 함수
def get_raw_data(name, file):
    data = open(file, 'r')
    data_log = []

    for line in data:
        if len(line) > 1000:   # cir data를 갖는 line은 1016개의 데이터를 갖기에 1000개 이상의 데이터를 갖는 line만 추출
            data_log.append(line)

    print("len(data_log): ", len(data_log)) # 데이터 추출 개수 확인

    processed_data = []  # 데이터 처리를 위한 리스트

    for i in data_log:
        if any(c.isalpha() for c in i):
            index = i.find("RSMPL")  # CIR log가 생성되는 과정에서 끝부분이 RSMPL(01)로 끝나는 Line이 생성되는 경우가 있음
            # RSMPL이라는 문자를 찾지 못하면 -1을 반환
            if index != -1:
                i = i[index+len("RSMPL")+4:]  # RSMPL 다음의 4개의 문자를 제외한 데이터를 추출
                processed_data.append(i)
            else:
                # 문자열이 없는 경우 바로 추가
                processed_data.append(i)
        # 알파벳이 없는 경우 바로 추가
        else:
            processed_data.append(i)
    
    data_log = processed_data # 데이터 처리된 데이터를 data_log에 저장
    raw_data = []  # 데이터 처리를 위한 리스트
    for i in range(len(data_log)):
        data_sample = [int(x) for x in data_log[i].strip().split(",") if x]  # 데이터를 ,로 분리, int로 변환하여 list로 저장
        raw_data.append(data_sample)
    
    count = 0
    for i in range(len(raw_data)):
        if len(raw_data[i]) > 1016:
            count += 1
    
    print("not 1016: ", count)  # 1016개의 데이터를 갖지 않는 데이터 확인

    if count != 0:
        for i in range(len(raw_data)):
            if len(raw_data[i]) > 1016:
                raw_data[i] = raw_data[i][1016:]  # 1016개의 데이터를 넘는 경우 중첩된 경우이므로 후자를 선택

    count = 0
    for i in range(len(raw_data)):
        if len(raw_data[i]) != 1016:
            count += 1
    print("after: ",count)  # 잘 변경 되었는지 확인
    if count != 0:
        print("error, 잘못 처리된 데이터가 있습니다.")  # 없을거 같지만 그래도 만듦, 그래서 어딘지까지는 안 알려줌
        return

    raw_data = pd.DataFrame(raw_data)  # 데이터프레임으로 변환

    # CIR data를 절대값처리한 후 정규화한 형태로 변환
    raw_data.to_csv(name)
    print(len(raw_data))
    


def find_abmax_index(row):
    return np.argmax(np.abs(row))


# Find the peak based on absolute value and extract -10 to +150 from it
# 절대값을 기준으로 peak를 찾아내 그 부분부터 -10부터 +150개 추출
def same_peak(data):
    peak_same = []
    for i in range(1, len(data)):
        start = find_abmax_index(data.iloc[i])
        peak_same.append(data.iloc[i][start-10:start+150].values)
    return pd.DataFrame(peak_same)