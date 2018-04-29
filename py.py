from aip import AipImageClassify
""" 你的 APPID AK SK """
APP_ID = '10946255'
API_KEY = 'ctDAxzAnc6TIRlE0Pj9cMe8i'
SECRET_KEY = 'wyUvIGZNCkO6AXfBaltoQWzWnfGUL7pR'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('cai.jpg')

""" 调用菜品识别 """
client.dishDetect(image);

""" 如果有可选参数 """
options = {}
options["top_num"] = 3

""" 带参数调用菜品识别 """
client.dishDetect(image, options)
