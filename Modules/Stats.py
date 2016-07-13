from Modules import PyHalo, medals, medalsDB


class service_record:

    def __init__(self, api_key='<insertAPIKey Here>'):
        self.key = api_key
        self.halo = PyHalo(self.key)

    def arena_service_record(self, gamertag):
        record = self.halo.get_arena_service_records(gamertag)
        results = record['Results']
        for result in results:
            medals = result['Result']['ArenaStats']['MedalAwards']
            totalWeaponDamage = result['Result']['ArenaStats']['TotalWeaponDamage']
            totalPowerWeaponKills = result['Result']['ArenaStats']['TotalPowerWeaponKills']
            totalKills = result['Result']['ArenaStats']['TotalKills']
            totalHeadshots = result['Result']['ArenaStats']['TotalHeadshots']
            totalShotsFired = result['Result']['ArenaStats']['TotalShotsFired']
            totalShotsLanded = result['Result']['ArenaStats']['TotalShotsLanded']
            totalMeleeKills = result['Result']['ArenaStats']['TotalMeleeKills']
            totalAssassinations = result['Result']['ArenaStats']['TotalAssassinations']
            totalGroundPoundKills = result['Result']['ArenaStats']['TotalGroundPoundKills']
            totalShoulderBashKills = result['Result']['ArenaStats']['TotalShoulderBashKills']
            totalPowerWeaponGrabs = result['Result']['ArenaStats']['TotalPowerWeaponGrabs']
            totalPowerWeaponPosessionTime = result['Result']['ArenaStats']['TotalPowerWeaponPossessionTime']
            totalDeaths = result['Result']['ArenaStats']['TotalDeaths']
            totalAssists = result['Result']['ArenaStats']['TotalAssists']
            totalGamesCompleted = result['Result']['ArenaStats']['TotalGamesCompleted']
            totalGamesWon = result['Result']['ArenaStats']['TotalGamesWon']
            totalGamesLost = result['Result']['ArenaStats']['TotalGamesLost']
            totalTimePlayed = result['Result']['ArenaStats']['TotalTimePlayed']
            spartanRank = result['Result']['SpartanRank']
            totalXP = result['Result']['Xp']
            accuracy = round((totalShotsLanded / totalShotsFired) * 100, 1)
            arena_record = {'weapon_damage': totalWeaponDamage, 'power_weapon_kills': totalPowerWeaponKills,
                            'kills': totalKills, 'headshots': totalHeadshots, 'shots_fired': totalShotsFired,
                            'shots_landed': totalShotsLanded, 'melee_kills': totalMeleeKills,
                            'assassinations': totalAssassinations, 'ground_pound_kills': totalGroundPoundKills,
                            'shoulder_bash_kills': totalShoulderBashKills, 'power_weapon_grabs': totalPowerWeaponGrabs,
                            'power_weapon_posession_time': totalPowerWeaponPosessionTime, 'deaths': totalDeaths,
                            'assists': totalAssists, 'games_completed': totalGamesCompleted,
                            'games_won': totalGamesWon, 'games_lost': totalGamesLost,
                            'time_played': totalTimePlayed, 'spartan_rank': spartanRank, 'total_XP': totalXP,
                            'accuracy': accuracy}
            return arena_record

    def warzone__service_record(self, gamertag):
        results = self.halo.get_warzone_service_records(gamertag)
        for result in results['Results']:
            totalWeaponDamage = result['Result']['WarzoneStat']['TotalWeaponDamage']
            totalPowerWeaponKills = result['Result']['WarzoneStat']['TotalPowerWeaponKills']
            totalKills = result['Result']['WarzoneStat']['TotalKills']
            totalHeadshots = result['Result']['WarzoneStat']['TotalHeadshots']
            totalShotsFired = result['Result']['WarzoneStat']['TotalShotsFired']
            totalShotsLanded = result['Result']['WarzoneStat']['TotalShotsLanded']
            totalMeleeKills = result['Result']['WarzoneStat']['TotalMeleeKills']
            totalAssassinations = result['Result']['WarzoneStat']['TotalAssassinations']
            totalGroundPoundKills = result['Result']['WarzoneStat']['TotalGroundPoundKills']
            totalShoulderBashKills = result['Result']['WarzoneStat']['TotalShoulderBashKills']
            totalPowerWeaponGrabs = result['Result']['WarzoneStat']['TotalPowerWeaponGrabs']
            totalPowerWeaponPosessionTime = result['Result']['WarzoneStat']['TotalPowerWeaponPossessionTime']
            totalDeaths = result['Result']['WarzoneStat']['TotalDeaths']
            totalAssists = result['Result']['WarzoneStat']['TotalAssists']
            totalGamesCompleted = result['Result']['WarzoneStat']['TotalGamesCompleted']
            totalGamesWon = result['Result']['WarzoneStat']['TotalGamesWon']
            totalGamesLost = result['Result']['WarzoneStat']['TotalGamesLost']
            totalTimePlayed = result['Result']['WarzoneStat']['TotalTimePlayed']
            spartanRank = result['Result']['SpartanRank']
            totalXP = result['Result']['Xp']
            accuracy = round((totalShotsLanded / totalShotsFired) * 100, 1)
            warzone_record = {'weapon_damage': totalWeaponDamage, 'power_weapon_kills': totalPowerWeaponKills,
                              'kills': totalKills, 'headshots': totalHeadshots, 'shots_fired': totalShotsFired,
                              'shots_landed': totalShotsLanded, 'melee_kills': totalMeleeKills,
                              'assassinations': totalAssassinations, 'ground_pound_kills': totalGroundPoundKills,
                              'shoulder_bash_kills': totalShoulderBashKills, 'power_weapon_grabs': totalPowerWeaponGrabs,
                              'power_weapon_posession_time': totalPowerWeaponPosessionTime, 'deaths': totalDeaths,
                              'assists': totalAssists, 'games_completed': totalGamesCompleted,
                              'games_won': totalGamesWon, 'games_lost': totalGamesLost,
                              'time_played': totalTimePlayed, 'spartan_rank': spartanRank, 'total_XP': totalXP,
                              'accuracy': accuracy}
            return warzone_record

    def get_medals(self):
        results = self.halo.get_medals()
        mdb = medalsDB()
        with mdb.transaction():
            mdb.drop_table()
        with mdb.transaction():
            mdb.create_table()
        for i in results:
            name = i['name']
            id = i['id']
            difficuly = i['difficulty']
            classification = i['classification']
            description = i['description']
            medal = medals(name=name, id=id, difficuly=difficuly, classification=classification, description=description)
            with mdb.transaction():
                mdb.insert(medal)










