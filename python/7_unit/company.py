# 公司

user_information = {}
information = 'information'
user_health = 'health'


def make_user_information(name, age, sex, **information_info):
    user_info = {'姓名': name, '年龄': age, '性别': sex}
    user_info.update(information_info)
    user_information[name][information] = user_info


def make_user_health(name, history_hospital, drug_allergy, **health):
    health_info = {'住院使': history_hospital, '过敏药物': drug_allergy}
    health_info.update(health)
    user_information[name][user_health] = health_info


def traversal_user_info():
    for username in user_information.keys():
        print('{}准时参加我单位2020年度职工代表大会'.format(username))
