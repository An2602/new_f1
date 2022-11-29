from Race import Race
from Points import ragil_dic, sprint_dic
from Driver import Driver

# def read_file():
#     with open("F1_Project.csv", "r") as file_open:
#         file_open.readline()
#         for line in file_open:
#             race_line = line.split(",")
#             ranking = [race_line[1], race_line[2], race_line[3], race_line[4], race_line[5], race_line[6]
#                 ,race_line[7], race_line[8], race_line[9],race_line[10], race_line[11]]
#             race = Race(type=race_line[0], ranking=ranking, fastest_driver=race_line[11], name = race_line[12][:-1])
#             print(race)
#             race.save()


def get_driver_score(all_races):
        for race in all_races:
            dict_of_drivers = {}
            if race.type == Race.SPRINT:
                for race, name_of_driver in enumerate(race.ranking[0:8]):
                    driver = {{ Driver.name }}
                    driver.score += sprint_dic[race]


            elif race.type == Race.RAGIL:
                for race,name_of_driver in enumerate(race.ranking):
                    driver = Driver.all_drivers[name_of_driver]
                    driver.score += ragil_dic[race]