import cv2

if __name__ == '__main__':
    f = open('output/' + 'test_demo_flow_statistic.txt', 'r')
    with open('output/' + 'test_demo_flow_statistic.txt', 'r') as f1:
        list = f1.readlines()
    # 当前的人数计数
    current_count_list_y = []
    for i in range(len(list)):
        new_temp_list = list[i].strip('\n').split(' ')
        current_count = new_temp_list[len(new_temp_list) - 1]
        current_count_list_y.append(current_count)
    # print(current_count_list_y)
    f.close()
    cap = cv2.VideoCapture('test_demo.mp4')
    ret, frame = cap.read()
    print(len(frame))
    frames_num = cap.get(7)
    fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
    # print(frames_num)
    # for i in range(101):
    #     progressPos = i / 100
    #     print(progressPos)
    # import datetime
    #
    # starttime = datetime.datetime.now()
    #
    # endtime = datetime.datetime.now()
    #
    # print((endtime - starttime).seconds)
