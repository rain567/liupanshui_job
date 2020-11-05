import company

company.make_user_information('tom', 19, '男', 爱好='game')
company.make_user_information('jerry', 19, '女', 爱好='音乐')
company.make_user_information('rain', 19, '男', 爱好='看书')
company.make_user_information('test', 19, '女')

company.make_user_health('tom', ['遵义医学院', '省医'], '青霉素', 健康状况='良好')
company.make_user_health('jerry', ['遵义医学院'], '青霉素')
company.make_user_health('rain', ['遵义医学院'], '青霉素', 健康状况='良好')
company.make_user_health('test', ['遵义医学院'], '青霉素')

company.traversal_user_info()

for name, info in company.user_information.items():
    print(info)
