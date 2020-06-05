from scipy import io
import csv


def scipy():
    # annolist
    #     image
    #     annorect
    #     vididx
    #     frame_sec
    # img_train(imgidx)
    # single_person(imgidx)
    # act(imgidx)
    #     act_name
    #     cat_name
    #     act_id
    # video_list(videoidx)

    load = io.loadmat("mpii.mat")
    rel = load['RELEASE']
    data = rel[0, 0]
    final_list = list()
    final_list.append(
        ['NAME', 'r ankle_X', 'r ankle_Y', 'r knee_X', 'r knee_Y', 'r hip_X', 'r hip_Y', 'l hip_X', 'l hip_Y',
         'l knee_X', 'l knee_Y', 'l ankle_X', 'l ankle_Y', 'pelvis_X', 'pelvis_Y', 'thorax_X', 'thorax_Y',
         'upper neck_X', 'upper neck_Y', 'head top_X', 'head top_Y', 'r wrist_X', 'r wrist_Y', 'r elbow_X',
         'r elbow_Y', 'r shoulder_X', 'r shoulder_Y', 'l shoulder_X', 'l shoulder_Y', 'l elbow_X', 'l elbow_Y',
         'l wrist_X', 'l wrist_Y', 'Scale', 'Activity', 'Category', 'ActID', 'Single_person', 'image_train',
         'youtubeID', 'frame_sec', 'vidid', 'head_rectangle', 'obj_pos'])
    annolist = data['annolist']
    img_tra = data['img_train']
    act = data['act']
    single = data['single_person']
    vlist = data['video_list']

    for ix in range(annolist.shape[1]):
        temp_arr = []
        obj_list = annolist[0, ix]
        rect = obj_list['annorect']
        img_d = obj_list['image']
        vidx = obj_list['vididx'][0]
        frame = obj_list['frame_sec'][0]
        obj_img = img_d[0, 0]
        head_rec = []
        obj_pos = []
        scale = 0

        name_d = obj_img['name']
        name = name_d[0]
        temp_arr.append(name)

        # if annorect is not empty
        if rect.shape[0] != 0 and rect[0, 0] is not None:
            obj_rect = rect[0, 0]
            try:
                if 'x1' in obj_rect.dtype.fields:
                    x1 = obj_rect['x1'][0, 0]
                    x2 = obj_rect['x2'][0, 0]
                    y1 = obj_rect['y1'][0, 0]
                    y2 = obj_rect['y2'][0, 0]
                    head_rec = [x1, x2, y1, y2]
            except:
                print(type(rect[0, 0]))
                print(rect[0, 0] is None)
            if 'objpos' in obj_rect.dtype.fields:
                objpos = obj_rect['objpos']
                try:
                    obj_pos = [objpos[0, 0][0][0][0], objpos[0, 0][1][0][0]]
                except:
                    pass
            if 'scale' in obj_rect.dtype.fields:
                try:
                    scale = obj_rect['scale'][0][0]
                except:
                    pass
            if 'annopoints' in rect.dtype.fields:
                annopoints = obj_rect['annopoints']
                if annopoints.shape[0] != 0:
                    obj_points = annopoints[0, 0]
                    points = obj_points['point']
                    cnt = 0
                    px = 0
                    for n in range(0, 32):
                        temp_arr.append(-1)
                    for px in range(0, points.shape[1]):
                        po = points[0, px]
                        po_id = po['id']
                        po_x = po['x']
                        po_y = po['y']
                        ind = 2 * po_id[0][0] + 1
                        temp_arr[ind] = po_x[0][0]
                        temp_arr[ind + 1] = po_y[0][0]
            else:
                for i in range(32):
                    temp_arr.append(-1)
        else:
            for i in range(32):
                temp_arr.append(-1)

        temp_arr.append(scale)

        activity = act[ix, 0]

        a_n = activity['act_name']
        c_n = activity['cat_name']
        a_id = activity['act_id']

        if a_n.shape[0] == 0:
            temp_arr.append(a_n)
        else:
            temp_arr.append(activity['act_name'][0])
        if c_n.shape[0] == 0:
            temp_arr.append(c_n)
        else:
            temp_arr.append(activity['cat_name'][0])
        temp_arr.append(a_id[0, 0])

        singlep = single[ix, 0]
        if singlep.shape[0] == 0:
            temp_arr.append([])
        elif singlep.shape[0] > 1:
            templist = list()
            for i in range(singlep.shape[0]):
                templist.append(singlep[i, 0])
            temp_arr.append(templist)
        else:
            try:
                temp_arr.append(singlep[0, 0])
            except:
                temp_arr.append(singlep)

        temp_arr.append(img_tra[0, ix])

        if ix < vlist.shape[1]:
            temp_arr.append(vlist[0, ix][0])
        else:
            temp_arr.append(0)

        if frame.shape[0] != 0:
            temp_arr.append(frame[0])
        else:
            temp_arr.append(0)
        if vidx.shape[0] != 0:
            temp_arr.append(vidx[0])
        else:
            temp_arr.append(0)

        temp_arr.append(head_rec)

        temp_arr.append(obj_pos)
        if len(temp_arr) > 44:
            print(final_list[0])
            print(temp_arr)
        final_list.append(temp_arr)

    #Uncomment the next part if you want the complete matlab dataset.

    # with open('MPII.csv', 'w', newline='') as file:
    #     file_writer = csv.writer(file, delimiter=';')
    #     count = 0
    #     for entry in final_list:
    #         if count % 100 == 0:
    #             print(count)
    #         file_writer.writerow(entry)
    #         count += 1

    # categories we need: 34, 35, 39, 40, 41
    # 'youtubeID' : 39,
    categories = {'Activity': 34, 'Category': 35, 'frame_sec': 40, 'vidid': 41}
    # „Joggen“, „Laufen“, „mit dem Hund laufen“, „Fahrrad fahren“ und „Liegen“
    wanted_activities = ['bicycling', 'running', 'jogging', 'walking the dog', 'walking, general', 'bicycling, general']
    # wanted_activities = ['walking the dog']
    special_list = []
    # special_list.append([final_list[0][34], final_list[0][35], final_list[0][39], final_list[0][40], final_list[0][41]])
    for j, entry in enumerate(final_list):
        temp_list = []
        try:
            if not entry[categories['Activity']] in wanted_activities:
                continue
        except:
            continue
        for i, val in enumerate(entry):
            if i in categories.values():
                if i == 41:
                    temp_list.append(final_list[val][39])
                else:
                    temp_list.append(val)
        special_list.append(temp_list)
    #This writes only the filtered csv file.
    with open('MPII_youtube.csv', 'w', newline='') as file:
        file_writer = csv.writer(file, delimiter=';')
        for entry in special_list:
            file_writer.writerow(entry)


if __name__ == '__main__':
    scipy()
