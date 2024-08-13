import os
import glob
import random
import requests
import yt_dlp
import logging
from pyrogram import filters
from strings.filters import command
from youtube_search import YoutubeSearch
from ZelzalMusic import app

def get_cookies_file():
    folder_path = f"{os.getcwd()}/cookies"
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    cookie_txt_file = random.choice(txt_files)
    return cookie_txt_file

@app.on_message(command(["/song", "بحث", "تحميل", "تنزيل", "يوت", "yt"]))
async def song(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = message.from_user.mention

    query = " ".join(message.command[1:])
    print(query)
    
    m = await message.reply("جاري البحث لحظة...")
    
    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "cookiefile": get_cookies_file()
    }
    
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

    except Exception as e:
        await m.edit("لم يتم العثور على الأغنية، يرجى المحاولة مرة أخرى!")
        logging.error(f"Failed to fetch YouTube video: {str(e)}")
        return
    
    await m.edit("جارٍ التنزيل... الرجاء الانتظار!")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        
        rep = f"الاسم: {title[:25]}\nبواسطة: {chutiya}"
        
        await message.reply_audio(
            audio_file,
            caption=rep,
            performer="@mmmsc.",
            thumb=thumb_name,
            title=title,
        )
        await m.delete()
    
    except Exception as e:
        await m.edit(f"[Victorious] **\n\**خطأ :** {e}")
        logging.error(f"Error while downloading audio: {str(e)}")

    finally:
        try:
            os.remove(audio_file)
            os.remove(thumb_name)
        except Exception as e:
            logging.error(f"Failed to delete temporary files: {str(e)}")

__mod_name__ = "اليوتيوب"
__help__ = """
بحث أو تحميل مع رابط الأغنية أو اسمها
"""