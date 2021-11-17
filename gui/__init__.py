import cv2

if __name__ == '__main__':
    # f = open('output/' + 'test_demo_flow_statistic.txt', 'r')
    # with open('output/' + 'test_demo_flow_statistic.txt', 'r') as f1:
    #     list = f1.readlines()
    # # 当前的人数计数
    # current_count_list_y = []
    # test = int(len(list)/50) + 1
    # iter = 0
    # print(test)
    # for i in range(test):
    #     new_temp_list = list[iter - 1].strip('\n').split(' ')
    #     print(iter)
    #     print(new_temp_list)
    #     current_count = new_temp_list[len(new_temp_list) - 1]
    #     current_count_list_y.append(current_count)
    #     iter = iter + 50
    # print(current_count_list_y)
    from matplotlib import pyplot

    f = open('output/'  + 'test_demo_flow_statistic.txt', 'r')
    with open('output/'+ 'test_demo_flow_statistic.txt', 'r') as f1:
        list = f1.readlines()
    import matplotlib.pyplot as plt
    current_count_list_y = []
    current_count_list_x = []
    y_test = []
    test = int(len(list) / 50) + 1
    iter = 0
    for i in range(test):
        new_temp_list = list[iter - 1].strip('\n').split(' ')
        current_count = new_temp_list[len(new_temp_list) - 1]
        print(new_temp_list)
        temp_current_count = current_count.split(',')
        print(temp_current_count[0])
        current_count = int(temp_current_count[0])
        current_count_list_y.append(current_count)
        current_count_list_x.append(i)
        iter = iter + 50
    for i in range(len(current_count_list_y)):
        y_test.append(10)
    print(current_count_list_y)
    print(y_test)
    plt.plot(current_count_list_x, current_count_list_y, mec='r', mfc='w', label='people')
    plt.plot(current_count_list_x, y_test, ms=10, label='Boundary')
    plt.legend()  # 让图例生效
    plt.margins(0)
    plt.subplots_adjust(bottom=0.10)
    plt.savefig('people_image.png')
    plt.show()
    # f.close()
    # cap = cv2.VideoCapture('test_demo.mp4')
    # ret, frame = cap.read()
    # print(len(frame))
    # frames_num = cap.get(7)
    # fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
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

    # encoding=utf-8
    # from matplotlib import pyplot
    # import matplotlib.pyplot as plt
    #
    # names = range(8, 21)
    # names = [str(x) for x in list(names)]
    #
    # x = range(len(names))
    # y_train = [0.140, 0.839, 0.834, 0.832, 0.824, 0.831, 0.823, 0.817, 0.814, 0.812, 0.812, 0.807, 0.805]
    # y_test = []
    # for i in range(len(y_train)):
    #     y_test.append(0.7)
    # print(y_test)
    # # plt.plot(x, y, 'ro-')
    # # plt.plot(x, y1, 'bo-')
    # # pl.xlim(-1, 11)  # 限定横轴的范围
    # # pl.ylim(-1, 110)  # 限定纵轴的范围
    #
    # plt.plot(x, y_train, marker='o', mec='r', mfc='w', label='people')
    # plt.plot(x, y_test, marker='*', ms=10, label='object')
    # plt.legend()  # 让图例生效
    # plt.xticks(x, names, rotation=1)
    # plt.margins(0)
    # plt.subplots_adjust(bottom=0.10)
    # plt.xlabel('the length')  # X轴标签
    # plt.ylabel("f1")  # Y轴标签
    # pyplot.yticks([0.750, 0.800, 0.850])
    # # plt.title("A simple plot") #标题
    # # plt.savefig('D:\\f1.jpg', dpi=900)
    #
    # plt.show()
