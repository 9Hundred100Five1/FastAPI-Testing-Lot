from neispy import Neispy
from asyncio.events import get_event_loop
from datetime import *
from pytz import timezone
import sys

scname = input()

async def main():
    async with Neispy('2f15b7060c4241cca54b2d2005ecd5b7') as neis:
        schoinfo = await neis.schoolInfo(SCHUL_NM=scname)
        AE = schoinfo[0].ATPT_OFCDC_SC_CODE
        SE = schoinfo[0].SD_SCHUL_CODE
        
        date1 = datetime.now(timezone('Asia/Seoul')).strftime('%Y%m%d')
        date2 = datetime.now(timezone('Asia/Seoul'))
        schomeal = await neis.mealServiceDietInfo(AE, SE, MLSV_YMD=date1)
        meal = schomeal[0].DDISH_NM.replace("<br/>", "\n")
        schotimetable = await neis.misTimetable(AE, SE, '2021', '2',  date1, None, None, None, '2', None, '5')
        timetable = [i.ITRT_CNTNT for i in schotimetable]
        if date2.weekday() == '5' or '6':
            print('\n')
            print(meal)
            print('주말 시간표는 제공하지 않습니다.')
            sys.exit()
        else:
            pass
            
        print(meal)
        print('timetable')
        
get_event_loop().run_until_complete(main())
            