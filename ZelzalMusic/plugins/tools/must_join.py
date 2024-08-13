from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZelzalMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/lllcz":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("lllcz", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/lllcz".isalpha():
                link = "https://t.me/lllcz"
            else:
                chat_info = await bot.get_chat("lllcz")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ حَبيبي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة Not DoDy .\n⌯︙قناة : t.me/lllcz 🍓.\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Not Res", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat @lllcz !")