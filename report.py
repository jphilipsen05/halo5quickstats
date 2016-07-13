from Config import gametype
import os
if 'arena' or 'Arena' in gametype:
    os.system('sqlite3 -header -csv stats.db "select * from arena;" > arena.csv')
if 'warzone' or 'Warzone' in gametype:
    os.system('sqlite3 -header -csv stats.db "select * from warzone;" > warzone.csv')
