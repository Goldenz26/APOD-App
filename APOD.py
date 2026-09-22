import os
import requests
import datefunc
import pic_info
from dotenv import load_dotenv
load_dotenv("API_KEY.env")
#NOTE DATE SHOULD BE IN YYMMDD WITH NO HYPHENS THIS CAN BE DONE WITH THE APODIFY METHOD
API_KEY = os.environ.get('API_KEY')
def save_image_from_date(date):
    date=datefunc.apodify(date)
    global API_KEY
    header = {"api_key": API_KEY}
    #params = {"date": date}
    response = requests.get(f"https://science.nasa.gov/wp-json/wp/v2/apod-basic/{date}",headers=header).json()

    pic_info.title = response["title"]
    pic_info.explain = response["explanation"]
    img_url = response['hdurl']
    img_data = requests.get(img_url).content



    try:    #fr means r lets you use backslash \ and f lets you add variables
        with open(fr".\ImageCache\image_{date}.png", "xb") as filehandler:
            filehandler.write(img_data)
            filehandler.close()
            print("Image added in cache")
    except FileExistsError:
        print("Image already exists in cache")
