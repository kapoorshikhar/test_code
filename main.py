import requests
import os
import time
import datetime

# Function to truncate long descriptions
def truncate_description(description, word_limit=50):
    if not description:
        return "No description available."
    
    words = description.split()
    if len(words) > word_limit:
        return ' '.join(words[:word_limit]) + '...'
    
    return description

# Function to download an image
def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {save_path}")
    except requests.RequestException as e:
        print(f"Failed to download image: {e}")

# Function to fetch news and save it in text files
def get_top_news(api_key, title_file, description_file, image_file, image_folder):
    category = 'nation'
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=in&max=10&apikey={api_key}"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        os.makedirs(image_folder, exist_ok=True)  # Ensure image folder exists

        with open(title_file, 'w') as title_f, open(description_file, 'w') as desc_f, open(image_file, 'w') as img_f:
            if articles:
                for i, article in enumerate(articles, 1):
                    title = article.get('title', 'No title available')
                    description = article.get('description', 'No description available')
                    image_url = article.get('image')
                    
                    truncated_description = truncate_description(description)

                    title_f.write(f"{title}\n\n")
                    desc_f.write(f"{truncated_description}\n\n")

                    if image_url:
                        img_f.write(f"Image URL: {image_url}\n")
                        image_filename = f"news_image_{i}.jpg"
                        image_path = os.path.join(image_folder, image_filename)
                        download_image(image_url, image_path)
                    else:
                        desc_f.write("Image: Not available\n\n")
            else:
                title_f.write("No news articles found.\n")
                desc_f.write("No news articles found.\n")
    else:
        print(f"Failed to retrieve news. Status code: {response.status_code}")

# Get the current date
def get_current_date():
    return datetime.datetime.now().strftime('%d %b %Y')

# Main execution
if __name__ == "__main__":
    api_key = '6db28cbad383869dd0d986c1ab891236'  # Replace with a valid API key
    title_file = 'titles.txt'
    description_file = 'descriptions.txt'
    image_file = 'image_urls.txt'
    image_folder = 'images'

    get_top_news(api_key, title_file, description_file, image_file, image_folder)

    print(f"News data saved in:\n- {title_file}\n- {description_file}\n- {image_file}")
