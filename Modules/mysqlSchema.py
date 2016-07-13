from contextlib import closing, contextmanager
import sqlite3
from threading import Lock
from datetime import datetime


class stats(object):

    def __init__(self, gamertag='', recordingDate=None, dict=None):
        self.gamertag = gamertag
        self.recordingDate = recordingDate
        for key, value in dict.items():
            setattr(self, key, value)

    @classmethod
    def from_row(cls, row):
        return Stat(*row)

class medals(object):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def from_row(cls, row):
        return Medals(*row)

class arenaDB(object):

    def __init__(self):
        self._connection = sqlite3.connect('stats.db', check_same_thread=False, isolation_level='DEFERRED')
        self._connection.execute('PRAGMA journal_mode = WAL')
        self._lock = Lock()

    def create_table(self):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS arena (gamertag TEXT, recordingDate REAL, total_XP REAL, "
                           "spartan_rank REAL, kills REAL, games_lost REAL, headshots REAL, shots_landed REAL, "
                           "games_won REAL, time_played REAL, assists REAL, ground_pound_kills REAL, accuracy REAL, "
                           "power_weapon_kills REAL, shots_fired REAL, melee_kills REAL, deaths REAL, "
                           "games_completed REAL, shoulder_bash_kills REAL, power_weapon_posession_time TEXT, "
                           "weapon_damage REAL, power_weapon_grabs REAL, assassinations REAL)")

    def insert(self, stat):
        places = ','.join(['?'] * len(stat.__dict__))
        keys = ','.join(stat.__dict__.keys())
        values = tuple(stat.__dict__.values())
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("INSERT INTO arena({}) VALUES ({})".format(keys, places), values)

    def lookup(self, gamertag):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute('SELECT * FROM arena WHERE gamertag = ? ORDER BY recordingDate DESC', (gamertag,))
            row = cursor.fetchall()
            if row:
                return row

    #Do not use the update function. It works, but there is not way to update these cells without overwriting other
    #    information. You will need to update the database manually.
    def update(self, stat):
        updates = []
        for key in stat.__dict__.keys():
            updates.append(key + ' = ?')
        updates = ', '.join(updates)
        values = tuple(stat.__dict__.values()) + (stat.recordingDate,)
        print('UPDATE arena SET {} WHERE gamertag = ?'.format(updates))
        with closing(self._connection.cursor()) as cursor:
            cursor.execute('UPDATE arena SET {} WHERE recordingDate = ?'.format(updates), values)


    @contextmanager
    def transaction(self):
        with self._lock:
            try:
                yield
                self._connection.commit()
            except:
                self._connection.rollback()
                raise


class warzoneDB(object):

    def __init__(self):
        self._connection = sqlite3.connect('stats.db', check_same_thread=False, isolation_level='DEFERRED')
        self._connection.execute('PRAGMA journal_mode = WAL')
        self._lock = Lock()

    def create_table(self):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS warzone (gamertag text, recordingDate REAL, total_XP real, "
                           "spartan_rank real, kills real, games_lost real, headshots real, shots_landed real, "
                           "games_won real, time_played real, assists real, ground_pound_kills real, accuracy real, "
                           "power_weapon_kills real, shots_fired real, melee_kills real, deaths real, "
                           "games_completed real, shoulder_bash_kills real, power_weapon_posession_time text, "
                           "weapon_damage real, power_weapon_grabs real, assassinations real)")

    def insert(self, stat):
        places = ','.join(['?'] * len(stat.__dict__))
        keys = ','.join(stat.__dict__.keys())
        values = tuple(stat.__dict__.values())
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("INSERT INTO warzone({}) VALUES ({})".format(keys, places), values)

    def lookup(self, gamertag):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute('SELECT * FROM warzone WHERE gamertag = ? ORDER BY recordingDate DESC', (gamertag,))
            row = cursor.fetchall()
            if row:
                return row

    #Do not use the update function. It works, but there is not way to update these cells without overwriting other
    #informaiton. You will need to update the database manually.
    def update(self, stat):
        updates = []
        for key in stat.__dict__.keys():
            updates.append(key + ' = ?')
        updates = ', '.join(updates)
        values = tuple(stat.__dict__.values()) + (stat.recordingDate,)
        print('UPDATE warzone SET {} WHERE gamertag = ?'.format(updates))
        with closing(self._connection.cursor()) as cursor:
            cursor.execute('UPDATE warzone SET {} WHERE recordingDate = ?'.format(updates), values)


    @contextmanager
    def transaction(self):
        with self._lock:
            try:
                yield
                self._connection.commit()
            except:
                self._connection.rollback()
                raise


class medalsDB(object):

    def __init__(self):
        self._connection = sqlite3.connect('stats.db', check_same_thread=False,
                                           isolation_level='DEFERRED')
        self._connection.execute('PRAGMA journal_mode = WAL')
        self._lock = Lock()

    def create_table(self):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS medals_id (name text, id real, difficuly text, classification text, "
                "description text)")

    def drop_table(self):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("DROP TABLE IF EXISTS medals")

    def insert(self, medals):
        places = ','.join(['?'] * len(medals.__dict__))
        keys = ','.join(medals.__dict__.keys())
        values = tuple(medals.__dict__.values())
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("INSERT INTO medals_id({}) VALUES ({})".format(keys, places), values)

    @contextmanager
    def transaction(self):
        with self._lock:
            try:
                yield
                self._connection.commit()
            except:
                self._connection.rollback()
                raise

# placeholder for future expansions
'''class campaignDB(object):

    def __init__(self):
        self._connection = sqlite3.connect('stats.db', check_same_thread=False, isolation_level='DEFERRED')
        self._connection.execute('PRAGMA journal_mode = WAL')
        self._lock = Lock()

    def create_table(self):
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS campaign (gamertag text, recordingDate REAL, headshots real)")

    def insert(self, stat):
        places = ','.join(['?'] * len(stat.__dict__))
        keys = ','.join(stat.__dict__.keys())
        values = tuple(stat.__dict__.values())
        with closing(self._connection.cursor()) as cursor:
            cursor.execute("INSERT INTO campaign({}) VALUES ({})".format(keys, places), values)

    def lookup(self, gamertag):
        """Return stock if found, else None"""
        with closing(self._connection.cursor()) as cursor:
            cursor.execute('SELECT * FROM campaign WHERE gamertag = ? ORDER BY recordingDate DESC', (gamertag,))
            row = cursor.fetchall()
            if row:
                return row

    #Do not use the update function. It works, but there is not way to update these cells without overwriting other
    #    informaiton. You will need to update the database manually.
    def update(self, stat):
        updates = []
        for key in stat.__dict__.keys():
            updates.append(key + ' = ?')
        updates = ', '.join(updates)
        values = tuple(stat.__dict__.values()) + (stat.recordingDate,)
        print('UPDATE arena SET {} WHERE gamertag = ?'.format(updates))
        with closing(self._connection.cursor()) as cursor:
            cursor.execute('UPDATE campaign SET {} WHERE recordingDate = ?'.format(updates), values)


    @contextmanager
    def transaction(self):
        with self._lock:
            try:
                yield
                self._connection.commit()
            except:
                self._connection.rollback()
                raise'''

'''def main():
    db = arenaDB()
    db.create_table()
    date = datetime.now()
    stat = arena_stats('Lazerhawk05', date, headshots=1006, kills=50, deaths=25)
    with db.transaction():
        db.insert(stat)
    with db.transaction():
        print(db.lookup('Lazerhawk05'))
    stat.headshots += 50
    with db.transaction():
        print(db.lookup('Lazerhawk05'))
    campaign = campaignDB()
    warzone = warzoneDB()
    campaign.create_table()
    warzone.create_table()
    with campaign.transaction():
        campaign.insert(stat)
    with campaign.transaction():
        print(campaign.lookup('Lazerhawk05'))
    with warzone.transaction():
        warzone.insert(stat)
    with warzone.transaction():
        print(warzone.lookup('Lazerhawk05'))




if __name__ == '__main__':
    main()'''