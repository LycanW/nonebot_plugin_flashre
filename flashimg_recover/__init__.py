from nonebot.adapters.cqhttp import Bot, Event, MessageEvent
from nonebot.adapters.cqhttp import message
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.plugin import export
from nonebot.rule import Rule
from nonebot.typing import T_State
from nonebot import on_message
import asyncio
import re

export = export()
export.name = '防闪照小助手'
export.usage = '你发个闪照就知道了[]~(￣▽￣)~*'

async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
    msg = str(event.get_message())
    return True if 'type=flash' in msg else False

flashimg = on_message(priority=1,rule=Rule(_checker))
@flashimg.handle()
async def _(bot: Bot, event: MessageEvent or Event, state: T_State):
    await asyncio.sleep(0.1)
    msg = str(event.get_message())
    comment = re.compile(r'file=(.*?).image',re.S)
    comment1 = str(comment.findall(msg))
    reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
    text = comment1
    x=str(re.sub(reg, '', text.upper()))
    id = event.get_user_id()
    url = ('https://gchat.qpic.cn/gchatpic_new/'+id+'/2640570090-2264725042-'+x.upper()+'/0?term=3')

    await flashimg.send((MessageSegment.image(url)),at_sender=False)
