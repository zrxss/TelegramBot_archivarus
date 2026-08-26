
from aiogram.filters import Filter
from aiogram import types, Bot

from config import TEACHER_ID, CHAT_ID




class IsGroupMember(Filter):
    async def __call__(self, event: types.Message | types.CallbackQuery, bot:Bot):
        if event.from_user.id == TEACHER_ID:
            return False
        member = await bot.get_chat_member(CHAT_ID, event.from_user.id)
        if member.status in ['creator', 'administrator', 'member']:
            return True
        if member.status == 'restricted' and member.is_member:
            return True
        return False