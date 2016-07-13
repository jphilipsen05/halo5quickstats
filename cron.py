from Modules import stats, arenaDB, warzoneDB, service_record
from Config import stat_tracking, spartans, gametype
from datetime import datetime


def main():
    service = service_record()
    date = datetime.now()
    '''update medals_id table'''
    service.get_medals()
    '''get service records'''
    for spartan in spartans:
        '''record arena stats'''
        arena_service = service.arena_service_record(spartan)
        arena_tracking = {}
        if 'arena' or 'Arena' in gametype:
            for key, value in arena_service.items():
                if key in stat_tracking:
                    temp = {key: value}
                    arena_tracking.update(temp)
            arenastat = stats(gamertag=spartan, recordingDate=date, dict=arena_tracking)
            adb = arenaDB()
            with adb.transaction():
                adb.create_table()
            with adb.transaction():
                adb.insert(arenastat)
        '''record warzone stats'''
        warzone_service = service.warzone__service_record(spartan)
        warzone_tracking = {}
        if 'warzone' or 'Warzone' in gametype:
            for key, value in warzone_service.items():
                if key in stat_tracking:
                    temp = {key: value}
                    warzone_tracking.update(temp)
            warzonestat = stats(gamertag=spartan, recordingDate=date, dict=warzone_tracking)
            wdb = warzoneDB()
            with wdb.transaction():
                wdb.create_table()
            with wdb.transaction():
                wdb.insert(warzonestat)


if __name__ == '__main__':
    main()