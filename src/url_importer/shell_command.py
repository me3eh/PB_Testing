# # import subprocess
# # import os
# # import sys
# # #
# #
# # def command_validity(command):
# #     process = subprocess.call(command, shell=True, env={'PYTHONPATH': cwd}, cwd=cwd)
# #     process.wait(timeout=10)
# #     # breakpoint()
# #
# #     if process.returncode != 0:
# #         return False
# #     return True
#
#
# # def execute_command_django(command):
# #     urls = []
# #     stream = os.popen(command)
# #
# #     for word in stream.readlines():
# #         url = word.split()[0]
# #         urls.append(url)
# #
# #     return urls
# #
# # def execute_command_and_put_into_file_rails(command, column_read):
# #     stream = os.popen(command)
# #     format_string = '(.:format)'
# #     with open("resources_for_testing/url.txt", 'w') as file:
# #         for word in stream.readlines():
# #             checked_line = word.split()
# #             if len(checked_line) <= 2 or checked_line[1] != 'GET':
# #                 continue
# #             urls = checked_line[column_read]
# #             if format_string in urls:
# #                 urls = urls.strip(format_string)
# #             file.write(urls)
# #             file.write("\n")
#
#
# # def execute_command_rails(command):
# #     urls = []
# #     stream = os.popen(command)
# #     format_string = '(.:format)'
# #
# #     # starting from second position, because there are headers in this command
# #     for word in stream.readlines()[1:]:
# #         checked_line = word.split()[2]
# #         urls.append(checked_line.replace(format_string, ""))
# #     return urls
#
#
# # def kekw(command):
# #     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='/home/me3eh/som/SRPD')
# #     process.wait(timeout=10)
# #     breakpoint()
# #
# # path = os.path.abspath("~")
# # kekw('python3 manage.py show_urls')
# # home = '~'
#
# import subprocess
# import os
# cwd_of_project = r'/home/me3eh/RecruitsReport'
# cwd = os.getcwd()
# os.chdir(cwd_of_project)
# # subprocess.Popen('tool.exe')
# # command = ['python3 manage.py show_urls']
# r_command = [f'rails routes']
# kk = subprocess.Popen(r_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # d = os.popen('(cd ~/RecruitsReport; rails routes)')
# out, err = kk.communicate()
# os.chdir(cwd)
#
# breakpoint()
# # for word in d.readlines()[1:]:
# #     print('da')
# # kk.wait(10)
# # breakpoint()
# # execute_command_django('(cd /home/me3eh/som/SRPD && python3 manage.py show_urls)')