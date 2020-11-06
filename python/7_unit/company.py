# 公司

# 员工个人信息列表
user_info_list = []
# 员工健康数据列表
user_health_list = []


def make_user_information(name, age, sex, **information_info):
    user_info = {'姓名': name, '年龄': age, '性别': sex}
    user_info.update(information_info)
    user_info_list.append(user_info)
    return user_info


def make_user_health(name, history_hospital, drug_allergy, **health):
    health_info = {'住院史': history_hospital, '过敏药物': drug_allergy}
    health_info.update(health)
    user_health_list.append(health_info)
    return health_info


def traversal_user_info(user_info):
    for user in user_info:
        print('{}准时参加我单位2020年度职工代表大会'.format(user['姓名']))
