# list_ = [num for num in range(1,51)]
#
# # writing to file
#
# with open('test.txt', 'w') as f:
#     for i in list_:
#         f.write(str(i) + '\n')
#
# # reading from file
#
# with open('test.txt', 'r') as file:
#     for line in file:
#         print(line)
#
# # appending to file
#
# text = 'hello world'
# write_file = open('test.txt', 'a')
# write_file.write(text)
# write_file.close()
#
# #
# import os
# #
# os.remove('/Users/er.py/PycharmProjects/vol3/test.txt')
# os.rename('/Users/er.py/PycharmProjects/vol3/test.txt', '/Users/er.py/PycharmProjects/vol3/xxx.txt')
#
# list_ = [num for num in range(1,51)]
#
# # writing to file
# try:
#     with open('test.txt', 'w') as f:
#         for i in list_:
#             f.write(i + '\n')
# except TypeError as ex:
#     print(ex)
#
#
# print('code working')

# try:
#     num = 1 / 1
#     print(Num)
# except Exception as error:
#     print(error)
#     num = 0
#
# print('Код отработал')

#
# f = open('xxx.txt')
# nums = []
# try:
#     for line in f:
#         nums.append(int(line))
# except ValueError as ex:
#     print(ex)
#     print('Это не число. Выходим')
# except Exception:
#     print('Что это вообще такое?')
# else:
#     print('Все хорошо!')
# finally:
#     f.close()
#     print('Я закрыл файл')
#     print(nums)


# print('код работает дальше')


if os.path.exists(f"{file_name}"):
            print("Папка уже существует!")
        else:
            os.mkdir(file_name)

        img_and_video_src_urls = []
        with open(f'{file_name}_set.txt') as file:
            urls_list = file.readlines()

            for post_url in urls_list:
                try:
                    browser.get(post_url)
                    time.sleep(4)

                    img_src = "/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/img"
                    video_src = "/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/div/div/video"
                    post_id = post_url.split("/")[-2]

                    if self.xpath_exists(img_src):
                        img_src_url = browser.find_element_by_xpath(img_src).get_attribute("src")
                        img_and_video_src_urls.append(img_src_url)

                        # сохраняем изображение
                        get_img = requests.get(img_src_url)
                        with open(f"{file_name}/{file_name}_{post_id}_img.jpg", "wb") as img_file:
                            img_file.write(get_img.content)

                    elif self.xpath_exists(video_src):
                        video_src_url = browser.find_element_by_xpath(video_src).get_attribute("src")
                        img_and_video_src_urls.append(video_src_url)

                        # сохраняем видео
                        get_video = requests.get(video_src_url, stream=True)
                        with open(f"{file_name}/{file_name}_{post_id}_video.mp4", "wb") as video_file:
                            for chunk in get_video.iter_content(chunk_size=1024 * 1024):
                                if chunk:
                                    video_file.write(chunk)
                    else:
                        # print("Упс! Что-то пошло не так!")
                        img_and_video_src_urls.append(f"{post_url}, нет ссылки!")
                    print(f"Контент из поста {post_url} успешно скачан!")

                except Exception as ex:
                    print(ex)
                    self.close_browser()

            self.close_browser()

        with open(f'{file_name}/{file_name}_img_and_video_src_urls.txt', 'a') as file:
            for i in img_and_video_src_urls:
                file.write(i + "\n")



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import LOGIN, PASSWORD
import time
import random

browser = webdriver.Chrome('chromedriver')


def login():
    try:
        browser.get('https://www.instagram.com')
        time.sleep(2)

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(LOGIN)
        time.sleep(2)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(PASSWORD)
        time.sleep(2)

        password_input.send_keys(Keys.ENTER)
        time.sleep(random.randrange(5, 8))
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


def like_posts():
    try:
        hashtag = input('Введите хештег: ')
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(5)
        for i in range(1, 3):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3, 5))

        hrefs = browser.find_elements_by_tag_name('a')
        post_urls = []
        for url in hrefs:
            href = url.get_attribute('href')
            if "/p/" in href:
                post_urls.append(href)
                print(href)
        # post_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]
        for url in post_urls:
            browser.get(url)
            time.sleep(3)
            like_button = browser.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
            like_button.click()
            time.sleep(random.randrange(5, 10))
            print(f"на странице {url} поставил лайк")
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


hashtag = input('Введите хештег: ')
browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
time.sleep(5)
for i in range(1, 3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.randrange(3, 5))

hrefs = browser.find_elements_by_tag_name('a')
post_urls = []


def main():
    login()
    like_posts()


if __name__ == '__main__':
    main()
