import copy

from api.login import login
from api.courseList import get_course_list
from api.courseDetail import get_course_detail
from api.packageList import get_package_list
from api.lesson import get_lesson_list
import pandas as pd

if __name__ == "__main__":
    username = input("请输入用户名：\n")
    password = input("请输入密码：\n")
    token = login(username, password)
    courses = get_course_list(token)['data']
    order_num_list = []
    for item in courses:
        order_num = {}
        order_num['name'] = item["name"]
        order_num["system_order_num"] = item["system_order_num"]
        order_num_list.append(order_num)

    course_info_list = []
    for system_order in order_num_list:
        details = get_course_detail(token, system_order['system_order_num'])['data']
        for list in details:
            for i in list["list"]:
                system_order['subName'] = i['name']
                system_order['coding'] = i['coding']
                course_info_list.append(copy.deepcopy(system_order))

    packages_list = []
    for course_info in course_info_list:
        packages = get_package_list(token, course_info['system_order_num'], course_info['coding'])
        if packages:
            for package in packages:
                course_info["id"] = package['id']
                course_info["packageName"] = package['name']
                packages_list.append(copy.deepcopy(course_info))

    download_url_list = []
    for package in packages_list:
        print("开始下载")
        lessons = get_lesson_list(token, package['id'], package['system_order_num'])['outline_info']
        total = len(lessons)
        print("一共{}组数据".format(total))
        count = 1
        for lesson in lessons:
            print("现在开始下载第{}组数据".format(count))
            for child in lesson['child']:
                if child['level_name'] == '讲义下载点这里':
                    package['level_name'] = child['level_name']
                    package[
                        'download_url'] = 'https://xue.eoffcn.com/web/download.html?lesson_id={}&package_id={}&course_type=1&coding={}&system_order={}'.format(
                        child['id'], child['package_id'], package['coding'], package['system_order_num'])
                    download_url_list.append(copy.deepcopy(package))
                else:
                    package['level_name'] = child['level_name']
                    package[
                        'download_url'] = 'https://xue.eoffcn.com/web/video.html?lesson_id={}&package_id={}&course_type=1&coding={}&system_order={}&is_task={}'.format(
                        child['id'], child['package_id'], package['coding'], package['system_order_num'],
                        child['is_task'])
                    download_url_list.append(copy.deepcopy(package))
            count = count + 1

    data = pd.DataFrame(download_url_list)
    data.to_excel('{}.xlsx'.format(username))
