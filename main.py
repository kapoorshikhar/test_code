import requests
import os
import pyautogui as p
import time as t

import datetime
def main():
    def truncate_description(description, word_limit=50):
        if not description:
            return "No description available."
        
        words = description.split()
        if len(words) > word_limit:
            return ' '.join(words[:word_limit]) + '...'
        
        return description

    def download_image(image_url, save_path):
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image successfully downloaded: {save_path}")
        except requests.RequestException as e:
            print(f"Failed to download image: {e}")

    def get_top_news(api_key, title_file_path, description_file_path, image_file_path, image_folder):
        category='nation'
        # general, world, nation, business, technology, entertainment, sports, science and health.
        url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=ins&max=10&apikey={api_key}"
        
        params = {
            'country': 'in',
            'lang': 'en',
            'max': 5,
            'apikey': api_key,
            
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            
            with open(title_file_path, 'a') as title_file, open(description_file_path, 'a') as description_file, open(image_file_path, 'a') as image_file:
                if articles:
                    for i, article in enumerate(articles, 1):
                        title = article.get('title', 'No title available')
                        description = article.get('description', 'No description available')
                        image_url = article.get('image')
                        
                        truncated_description = truncate_description(description, word_limit=50)
                        
                        title_file.write(f"{title}\n\n")
                        description_file.write(f"{truncated_description}\n")
                        
                        if image_url:
                            image_file.write(f"Image URL: {image_url}\n")
                            # Uncomment the following lines if you want to download the images
                            image_filename = f"news_image_{i}.jpg"
                            image_path = os.path.join(image_folder, image_filename)
                            download_image(image_url, image_path)
                            # description_file.write(f"Image saved as: {image_filename}\n\n")
                        else:
                            description_file.write("Image: Not available\n\n")
                else:
                    title_file.write("No news articles found.\n")
                    description_file.write("No news articles found.\n")
        else:
            print(f"Failed to retrieve news. Status code: {response.status_code}")

    api_key = '6db28cbad383869dd0d986c1ab891236'
    title_file_path = '2_titles.txt'
    description_file_path = '4_descriptions.txt'
    image_file_path = '3_image_urls.txt'
    image_folder = 'bg_img'

    file_path= r'C:\\Users\\Public\\Documents\\CUsersPublicDocuments\\Version_0\\2_titles.txt'
    os.makedirs(image_folder, exist_ok=True)
    get_top_news(api_key, title_file_path, description_file_path, image_file_path, image_folder)

def open_canva():
    p.hotkey('win','5')
    t.sleep(1)
    p.hotkey('ctrl','2')
    t.sleep(2)
    p.hotkey('ctrl','l')
    p.typewrite("https://www.canva.com/design/DAGaFCrCUNc/bX0HGZen82RpX4N__zJFyg/edit?ui=eyJEIjp7IlAiOnsiQiI6ZmFsc2V9fX0")
    p.hotkey("enter")
    t.sleep(2)
    for i in range(12):
        p.press('left')
    t.sleep(5)
def get_p_date():
    previous_day = (datetime.datetime.now().strftime('%d %b %Y'))
    return previous_day
def get_t_date():
    today_date = datetime.datetime.now().strftime('%d %b %Y')
    return today_date

def set_date(e):
    t.sleep(1)
    p.moveTo(674,367, duration=1)# pervious
    p.click()
    p.click()
    t.sleep(1)
    p.hotkey("delete")
    p.moveTo(687,415, duration=1)# new location for date 17% visible
    p.click()
    p.click()
    t.sleep(1)
    p.hotkey("ctrl","a")
    p.hotkey("delete")
    p.typewrite(f"{e}")

def count_lines_in_file():
    try:
        file_name = r"C:\\Users\\Public\Documents\\CUsersPublicDocuments\\2_titles.txt"
        with open(file_name, 'r') as file:
            lines = file.readlines()
        line_count = len(lines)
        # print(line_count)
        return line_count
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def copy_title(i):
    p.hotkey('win','4')
    p.hotkey('ctrl','p')
    p.typewrite('2_titles.txt')
    t.sleep(2)
    p.hotkey('enter')
    t.sleep(2)
    p.hotkey('ctrl','g')
    p.typewrite(f'{i}')
    t.sleep(2)
    p.hotkey('enter')
    p.hotkey('ctrl','l')
    t.sleep(1)
    p.hotkey('ctrl','c')
    
def past_title():
    p.hotkey('win','5')
    t.sleep(1)
    p.moveTo(693,450, duration=1)
    p.click()
    p.doubleClick()
    t.sleep(1)
    p.hotkey("ctrl","a")
    p.hotkey('ctrl','v')
    t.sleep(5)
    p.moveTo(186,634,duration=1)
    # p.moveTo(493,410)
    p.click()
    p.hotkey('right')

# p.displayMousePosition()687,415
main()
# open_canva()
# t.sleep(3)
# e=get_t_date()
# n= count_lines_in_file()
# print(n)
# p.moveTo(207,698,duration=1)
# p.click()
# p.click()
# for i in range(1,n,2):
#     set_date(e) 
#     copy_title(i)
#     past_title()
    
