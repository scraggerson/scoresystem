# <editor-fold desc="slop">
import fileinput
from operator import truediv
import json
import os
try:
  import numpy as np
except:
  print("Installing numpy dependancy")
  os.system("pip install numpy")
  import numpy as np
eventcount = 0
eventchoice = True
teameventlist = []
individualeventlist = []
soloplayerlist = []
teamlist = []
teamstoadd = []
teamsinevent = []
emptylist = [ ]
teamscoredict = {

}
emptydict = {

}
teamranks = {

}
#   variables area  #
# </editor-fold>

# <editor-fold desc="MAIN MENU">
######  MAIN MENU    #####
def main_menu():
    print("------------MAIN MENU------------")
    print("please choose from the following options: ")
    print("1. manage events")
    print("2. manage teams and participants")
    print("3. manage competition")
    print("4. wouldnt you like to know weather boy")
    choiceidentifier = int(input("enter option here: "))
    #select user option#
    if choiceidentifier == 1:
        event_manager()
    elif choiceidentifier == 2:
        participant_manager()
    elif choiceidentifier ==3:
        competition_manager()
    elif choiceidentifier == 4:
        testing_func()
######  MAIN MENU    #####

######  DIVIDER #####
def div():
    print("-----------------------------------------")
######  DIVIDER #####

######  MENU RETURN    #####
def menureturn():
    menureturn = input("press enter to return to main menu: ")
    main_menu()
######  MENU RETURN    #####

# </editor-fold>

# <editor-fold desc="EVENT MANAGEMENT">
########### EVENT MANAGEMENT   ###########
######  EVENT MANAGER    #####
def event_manager():
    print("------------EVENT MANAGER------------")
    print("please choose from the following options: ")
    print("1. add a new team event")
    print("2. add a new individual event")
    print("3. view current team events")
    print("4. view current individual events")
    print("5. remove a team event")
    print("6. remove an individual event")
    print("7. view all events")
    print("8. add an individual to an event")
    print("9. add a team to an event")
    print("10. view teams in an event")
    print("11. view individuals in an event")
    print("12. remove a team from an event")
    print("13. remove a participant from an event")
    print("14. return to main menu")
    choiceidentifier = int(input("enter option here: "))
    if choiceidentifier == 1:
        enter_team_event()
    elif choiceidentifier == 2:
        enter_individual_event()
    elif choiceidentifier == 3:
        view_team_events()
    elif choiceidentifier == 4:
        view_individual_events()
    elif choiceidentifier == 5:
        remove_team_event()
    elif choiceidentifier == 6:
        remove_individual_event()
    elif choiceidentifier == 7:
        view_all_events()
    elif choiceidentifier == 8:
        add_individual_to_event()
    elif choiceidentifier == 9:
        add_team_to_event()
    elif choiceidentifier == 10:
        view_teams_in_event()
    elif choiceidentifier == 11:
        view_individuals_in_event()
    elif choiceidentifier == 12:
        remove_team_from_event()
    elif choiceidentifier == 13:
        remove_individual_from_event()
    elif choiceidentifier == 14:
        main_menu()
######  EVENT MANAGER    #####

######  EVENT MANAGER RETURN    #####
def eventmanreturn():
    eventmanreturn = input("press enter to return to event manager: ")
    event_manager()
######  EVENT MANAGER RETURN    #####

#####   VIEW TEAM EVENTS #####
def view_team_events():
    print("------------TEAM EVENTS------------")
    with open("teameventstore.json", 'r',) as f:
        teameventlist = json.load(f)
        if not teameventlist:
            print("no events found!")
        else:
            print(teameventlist)
    eventmanreturn()
#####   VIEW TEAM EVENTS #####

#####   VIEW INDIVIDUAL EVENTS #####
def view_individual_events():
    print("------------INDIVIDUAL EVENTS------------")
    with open("individualeventstore.json", 'r',) as f:
        individualeventlist = json.load(f)
    if not individualeventlist:
        print("no events found!")
    else:
        print(individualeventlist)
    eventmanreturn()
#####   VIEW INDIVIDUAL EVENTS #####

#####   VIEW ALL EVENTS #####
def view_all_events():
    print("------------ALL EVENTS------------")
    print("---TEAM---")
    with open("teameventstore.json", 'r',) as f:
        teameventlist = json.load(f)
        if not teameventlist:
            print("no events found!")
        else:
            print(teameventlist)
    print("---INDIVIDUAL---")
    with open("individualeventstore.json", 'r',) as f:
        individualeventlist = json.load(f)
    if not individualeventlist:
        print("no events found!")
    else:
        print(individualeventlist)
    eventmanreturn()
#####   VIEW ALL EVENTS #####

######  ENTER TEAM EVENT    #####
def enter_team_event():
    print("------------ENTER TEAM EVENT------------")
    with open("teameventstore.json", 'r',) as f:
        teameventlist = json.load(f)
    eventname = str(input("enter event name here: "))
    teameventlist.append(eventname)
    with open("teameventstore.json", 'w') as f:
        json.dump(teameventlist, f, indent=2)
    print(F"'{eventname}' has been added.")
    print("what would you like to do?")
    print("1. enter another event")
    print("2. view current team events")
    print("3. return to event manager")
    repeat = int(input("enter option here: "))
    if repeat == 1:
        enter_team_event()
    elif repeat == 2:
        view_team_events()
    elif repeat == 3:
        event_manager()
    else:
        event_manager()
######  ENTER TEAM EVENT    #####

######  ENTER INDIVIDUAL EVENT    #####
def enter_individual_event():
    print("------------ENTER INDIVIDUAL EVENT------------")
    eventname = str(input("enter event name here: "))
    individualeventlist.append(eventname)
    with open("individualeventstore.json", 'w') as f:
        json.dump(individualeventlist, f, indent=2)
    print("what would you like to do?")
    print("1. enter another event")
    print("2. view current individual events")
    print("3. return to event manager")
    repeat = int(input("enter option here: "))
    if repeat == 1:
        enter_individual_event()
    elif repeat == 2:
        view_individual_events()
    elif repeat == 3:
        event_manager()
    else:
        event_manager()
######  ENTER INDIVIDUAL EVENT    #####

######  REMOVE TEAM EVENT    #####
def remove_team_event():
    print("------------REMOVE TEAM EVENT------------")
    with open("teameventstore.json", 'r',) as f:
        teameventlist = json.load(f)
    if not teameventlist:
        print("no events found! returning to event manager.")
        event_manager()
    else:
        print(teameventlist)
        print("enter the name of the event you would like to remove. (case sensitive)")
        removaltarget = input("enter name here: ")
        if removaltarget in teameventlist:
            teameventlist.remove(removaltarget)
            with open("teameventstore.json", 'w') as f:
                json.dump(teameventlist, f, indent=2)
            if os.path.exists(f"{removaltarget}.json"):
                os.remove(f"{removaltarget}.json")
            print(f"{removaltarget} has been removed from the list successfully.")
            print("what would you like to do?")
            print("1. remove another event")
            print("2. return to event manager")
            repeat = int(input("enter option here: "))
            if repeat == 1:
                remove_team_event()
            elif repeat == 2:
                event_manager()
            else:
                event_manager()
        else:
            print("the data you entered was invalid or not in the list! please try again.")
            remove_team_event()
######  REMOVE TEAM EVENT    #####

######  REMOVE INDIVIDUAL EVENT    #####
def remove_individual_event():
    print("------------REMOVE INDIVIDUAL EVENT------------")
    with open("individualeventstore.json", 'r',) as f:
        individualeventlist = json.load(f)
    if not individualeventlist:
        print("no events found! returning to event manager.")
        event_manager()
    else:
        print(individualeventlist)
        print("enter the name of the event you would like to remove. (case sensitive)")
        removaltarget = input("enter name here: ")
        if removaltarget in individualeventlist:
            individualeventlist.remove(removaltarget)
            with open("individualeventstore.json", 'w') as f:
                json.dump(individualeventlist, f, indent=2)
            if os.path.exists(f"{removaltarget}.json"):
                os.remove(f"{removaltarget}.json")
            print(f"{removaltarget} has been removed from the list successfully.")
            print("what would you like to do?")
            print("1. remove another event")
            print("2. return to event manager")
            repeat = int(input("enter option here: "))
            if repeat == 1:
                remove_individual_event()
            elif repeat == 2:
                event_manager()
            else:
                event_manager()
        else:
            print("the data you entered was invalid or not in the list! please try again.")
            remove_individual_event()
######  REMOVE INDIVIDUAL EVENT    #####

######  ADD TEAM TO EVENT    #####
def add_team_to_event():
    print("------------ADD TEAM TO EVENT------------")
    print("please select an event from the following list: ")
    with open("teameventstore.json", 'r') as f:
        eventlist = json.load(f)
        if not eventlist:
            print("no events found!")
            eventmanreturn()
        else:
            print(f"AVAILABLE TEAM EVENTS: {eventlist}")
            print("-----------------------------------------")
            chosenevent = str(input("enter event name here: "))
            if chosenevent in eventlist:
                try:
                    with open(f"{chosenevent}.json", 'r') as f:
                        teamsinevent = json.load(f)
                except:
                    with open(f"{chosenevent}.json", 'w') as f:
                        json.dump(emptylist, f, indent=2)
                with open("teamstore.json", 'r') as f:
                    teamlist = json.load(f)
                with open(f"{chosenevent}.json", 'r') as f:
                    teamsinevent = json.load(f)
                print("-----------------------------------------")
                print(f"TEAMS CURRENTLY IN {chosenevent}: {teamsinevent}")
                print(f"AVAILABLE TEAMS: {teamlist}")
                print("-----------------------------------------")
                chosenteam = str(input("enter team name here: "))
                if chosenteam in teamsinevent:
                    print(f"that team is already participating in {chosenevent}!")
                    add_team_to_event()
                else:
                    teamsinevent.append(chosenteam)
                    print(f"added {chosenteam} to {chosenevent}.")
                    with open(f"{chosenevent}.json", 'w') as f:
                        json.dump(teamsinevent, f, indent=2) #dump team to event file#
                    try:
                        with open(f"{chosenteam}score.json", 'r') as f:
                            teamscoredict = json.load(f)
                        teamscoredict[f"{chosenevent}"] = 0
                        with open(f"{chosenteam}score.json", 'w') as f:
                            json.dump(teamscoredict, f, indent=2)
                        eventmanreturn()
                    except:
                        teamscoredict = {

                        }
                        teamscoredict[f"{chosenevent}"] = 0
                        with open(f"{chosenteam}score.json", 'w') as f:
                            json.dump(teamscoredict, f, indent=2)
                        eventmanreturn()
            else:
                print("event not found! please try again.")
                add_team_to_event()
######  ADD TEAM TO EVENT    #####

######  REMOVE TEAM FROM EVENT    #####
def remove_team_from_event():
    print("------------REMOVE TEAM FROM EVENT------------")
    print("please select an event from the following list: ")
    with open("teameventstore.json", 'r') as f:
        eventlist = json.load(f)
        if not eventlist:
            print("no events found!")
            eventmanreturn()
        else:
            print(f"AVAILABLE TEAM EVENTS: {eventlist}")
            print("-----------------------------------------")
            chosenevent = str(input("enter event name here: "))
            if chosenevent in eventlist:
                try:
                    with open(f"{chosenevent}.json", 'r') as f:
                        teamsinevent = json.load(f)
                except:
                    with open(f"{chosenevent}.json", 'w') as f:
                        json.dump(emptylist, f, indent=2)
                with open("teamstore.json", 'r') as f:
                    teamlist = json.load(f)
                with open(f"{chosenevent}.json", 'r') as f:
                    teamsinevent = json.load(f)
                print("-----------------------------------------")
                print(f"TEAMS CURRENTLY IN {chosenevent}: {teamsinevent}")
                print("-----------------------------------------")
                chosenteam = str(input("enter team name here: "))
                if chosenteam in teamsinevent:
                    teamsinevent.remove(chosenteam)
                    with open(f"{chosenevent}.json", 'w') as f:
                        json.dump(teamsinevent, f, indent=2)
                    print(f"removed {chosenteam} from {chosenevent}!")
                    eventmanreturn()
                else:
                    print(f"{chosenteam} is not in {chosenevent}!")
                    eventmanreturn()
            else:
                print("event not found! please try again.")
                remove_team_from_event()
######  REMOVE TEAM FROM EVENT    #####

######  REMOVE INDIVIDUAL FROM EVENT    #####
def remove_individual_from_event():
    print("------------REMOVE PARTICIPANT FROM EVENT------------")
    print("please select an event from the following list: ")
    with open("individualeventstore.json", 'r') as f:
        eventlist = json.load(f)
        if not eventlist:
            print("no events found!")
            eventmanreturn()
        else:
            print(f"AVAILABLE TEAM EVENTS: {eventlist}")
            print("-----------------------------------------")
            chosenevent = str(input("enter event name here: "))
            if chosenevent in eventlist:
                try:
                    with open(f"{chosenevent}.json", 'r') as f:
                        playersinevent = json.load(f)
                except:
                    with open(f"{chosenevent}.json", 'w') as f:
                        json.dump(emptylist, f, indent=2)
                with open("soloplayerstore.json", 'r') as f:
                    playerlist = json.load(f)
                with open(f"{chosenevent}.json", 'r') as f:
                    playersinevent = json.load(f)
                print("-----------------------------------------")
                print(f"PARTICIPANTS CURRENTLY IN {chosenevent}: {playersinevent}")
                print("-----------------------------------------")
                chosenplayer = str(input("enter participant name here: "))
                if chosenplayer in playersinevent:
                    playersinevent.remove(chosenplayer)
                    with open(f"{chosenevent}.json", 'w') as f:
                        json.dump(playersinevent, f, indent=2)
                    print(f"removed {chosenplayer} from {chosenevent}!")
                    eventmanreturn()
                else:
                    print(f"{chosenplayer} is not in {chosenevent}!")
                    eventmanreturn()
            else:
                print("event not found! please try again.")
                remove_individual_from_event()
######  REMOVE INDIVIDUAL FROM EVENT    #####

######  ADD INDIVIDUAL TO EVENT    #####
def add_individual_to_event():
    print("------------ADD INDIVIDUAL TO EVENT------------")
    print("please select an event from the following list: ")
    with open("individualeventstore.json", 'r') as f:
        eventlist = json.load(f)
        if not eventlist:
            print("no events found!")
            eventmanreturn()
        else:
            print(f"AVAILABLE INDIVIDUAL EVENTS: {eventlist}")
            print("-----------------------------------------")
            chosenevent = str(input("enter event name here: "))
            if chosenevent in eventlist:
                try:
                    with open(f"{chosenevent}.json", 'r') as f:
                        playersinevent = json.load(f)
                except:
                    with open(f"{chosenevent}.json", 'w') as f:
                        json.dump(emptylist, f, indent=2)
                with open("soloplayerstore.json", 'r') as f:
                    soloplayerlist = json.load(f)
                with open(f"{chosenevent}.json", 'r') as f:
                    playersinevent = json.load(f)
                print("-----------------------------------------")
                print(f"PARTICIPANTS CURRENTLY IN {chosenevent}: {playersinevent}")
                print(f"AVAILABLE PARTICIPANTS: {soloplayerlist}")
                print("-----------------------------------------")
                chosenplayer = str(input("enter participant name here: "))
                if chosenplayer in playersinevent:
                    print(f"that team is already participating in {chosenevent}!")
                    add_team_to_event()
                else:
                    playersinevent.append(chosenplayer)
                    print(f"added {chosenplayer} to {chosenevent}.")
                    with open(f"{chosenevent}.json", 'w') as f:
                        json.dump(playersinevent, f, indent=2)  # dump team to event file#
                    try:
                        with open(f"{chosenplayer}score.json", 'r') as f:
                            playerscoredict = json.load(f)
                        playerscoredict[f"{chosenevent}"] = 0
                        with open(f"{chosenplayer}score.json", 'w') as f:
                            json.dump(playerscoredict, f, indent=2)
                        eventmanreturn()
                    except:
                        playerscoredict = {

                        }
                        playerscoredict[f"{chosenevent}"] = 0
                        with open(f"{chosenplayer}score.json", 'w') as f:
                            json.dump(playerscoredict, f, indent=2)
                        eventmanreturn()
            else:
                print("event not found! please try again.")
                add_team_to_event()

######  VIEW TEAMS IN EVENT    #####
def view_teams_in_event():
    print("------------VIEW TEAMS IN EVENT------------")
    print("please choose an event to view its competitors.")
    with open("teameventstore.json", 'r', ) as f:
        teameventlist = json.load(f)
        if not teameventlist:
            print("no events found!")
        else:
            print(teameventlist)
            eventtoview = str(input("enter option here: "))
            try:
                with open(f"{eventtoview}.json", 'r') as f:
                    teamlist = json.load(f)
                if not teamlist:
                    print(f"no teams found in {eventtoview}!")
                else:
                    print(f"teams in {eventtoview}: {teamlist}")
                    eventmanreturn()
            except:
                print(f"no event file for '{eventtoview}' could be found, please add a team to '{eventtoview}' and try again.")
                eventmanreturn()
######  VIEW TEAMS IN EVENT    #####

######  VIEW INDIVIDUALS IN EVENT    #####
def view_individuals_in_event():
    print("------------VIEW INDIVIDUALS IN EVENT------------")
    print("please choose an event to view its competitors.")
    with open("individualeventstore.json", 'r', ) as f:
        soloplayerlist = json.load(f)
        if not soloplayerlist:
            print("no events found!")
        else:
            print(soloplayerlist)
            eventtoview = str(input("enter option here: "))
            try:
                with open(f"{eventtoview}.json", 'r') as f:
                    playerlist = json.load(f)
                if not playerlist:
                    print(f"no participants found in {eventtoview}!")
                else:
                    print(f"participants in {eventtoview}: {playerlist}")
                    eventmanreturn()
            except:
                print(
                    f"no event file for '{eventtoview}' could be found, please add participants to '{eventtoview}' and try again.")
                eventmanreturn()
######  VIEW INDIVIDUALS IN EVENT    #####

########### EVENT MANAGEMENT    ###########
# </editor-fold>

# <editor-fold desc="PARTICIPANT MANAGEMENT">
######  PARTICIPANT MANAGER    #####
def participant_manager():
    print("------------PARTICIPANT MANAGER------------")
    print("please choose from the following options: ")
    print("1. add a new participant")
    print("2. view individual participants")
    print("3. remove individual participants")
    print("4. add new team")
    print("5. remove a team")
    print("6. view current teams")
    print("7 add a new participant to a team")
    print("8. view participants in a team")
    print("9. remove a player from a team")
    print("10. return to main menu")
    
    choiceidentifier = int(input("enter option here: "))
    if choiceidentifier == 1:
        enter_solo_player()
    elif choiceidentifier == 2:
        view_solo_players()
    elif choiceidentifier == 3:
        remove_solo_player()
    elif choiceidentifier == 4:
        add_team()
    elif choiceidentifier == 5:
        remove_team()
    elif choiceidentifier == 6:
        view_teams()
    elif choiceidentifier == 7:
        add_player_to_team()
    elif choiceidentifier == 8:
        view_players_in_team()
    elif choiceidentifier == 9:
        remove_player_from_team()
    elif choiceidentifier == 10:
        main_menu()
######  PARTICIPANT MANAGER    #####

######  PARTICIPANT MANAGER RETURN    #####
def participantmanreturn():
    playermanreturn = input("press enter to return to participant manager: ")
    participant_manager()
######  PARTICIPANT MANAGER RETURN    #####

#####   VIEW INDIVIDUAL PARTICIPANTS #####
def view_solo_players():
    print("------------INDIVIDUAL PARTICIPANTS------------")
    with open("soloplayerstore.json", 'r',) as f:
        soloplayerlist = json.load(f)
    if not soloplayerlist:
        print("no participants found!")
    else:
        print(soloplayerlist)
    participantmanreturn()
#####   VIEW INDIVIDUAL PARTICIPANTS #####

###### ENTER NEW PARTICIPANT    #####
def enter_solo_player():
    print("------------ENTER INDIVIDUAL PARTICIPANT------------")
    with open("soloplayerstore.json", 'r',) as f:
        soloplayerlist = json.load(f)
    playername = str(input("enter participant name here: "))
    if len(soloplayerlist)>=20:
        print("only 20 individual participants may be added!")
        participantmanreturn()
    else:
        soloplayerlist.append(playername)
        print(f"CURRENT PARTICIPANTS: {soloplayerlist}")
        with open("soloplayerstore.json", 'w') as f:
            json.dump(soloplayerlist, f, indent=2)
        playerscoredict = {

        }
        with open(f"{playername}score.json", 'w') as f:
            json.dump(playerscoredict, f, indent=2)
        print(F"'{playername}' has been added.")
        print("what would you like to do?")
        print("1. enter another participant")
        print("2. view current participants")
        print("3. return to participant manager")
        repeat = int(input("enter option here: "))
        if repeat == 1:
            enter_solo_player()
        elif repeat == 2:
            view_solo_players()
        elif repeat == 3:
            participant_manager()
        else:
            participant_manager()
###### ENTER NEW PARTICIPANT    #####

######  REMOVE INDIVIDUAL PARTICIPANT    #####
def remove_solo_player():
    print("------------REMOVE INDIVIDUAL PARTICIPANT------------")
    with open("soloplayerstore.json", 'r',) as f:
        soloplayerlist = json.load(f)
    if not soloplayerlist:
        print("no participants found! returning to participant manager.")
        participant_manager()
    else:
        print(soloplayerlist)
        print("enter the name of the participant you would like to remove. (case sensitive)")
        removaltarget = input("enter name here: ")
        if removaltarget in soloplayerlist:
            soloplayerlist.remove(removaltarget)
            with open("soloplayerstore.json", 'w') as f:
                json.dump(soloplayerlist, f, indent=2)
            if os.path.exists(f"{removaltarget}.json"):
                os.remove(f"{removaltarget}.json")
            print(f"{removaltarget} has been removed from the list successfully.")
            print("what would you like to do?")
            print("1. remove another participant")
            print("2. return to participant manager")
            repeat = int(input("enter option here: "))
            if repeat == 1:
                remove_solo_player()
            elif repeat == 2:
                participant_manager()
            else:
                participant_manager()
        else:
            print("the data you entered was invalid or not in the list! please try again.")
            remove_solo_player()
######  REMOVE INDIVIDUAL PARTICIPANT    #####

######  ADD NEW TEAM    #####
def add_team():
    print("------------ADD NEW TEAM------------")
    with open("teamstore.json", 'r',) as f:
        teamlist = json.load(f)
    teamname = str(input("enter new team name here: "))
    if len(teamlist)>=4:
        print("only 4 teams may be added!")
        participant_manager()
    else:
        teamlist.append(teamname)
        print(teamlist)
        with open ("teamstore.json", 'w') as f:
            json.dump(teamlist, f, indent=2)
        teamscoredict = {

        }
        with open(f"{teamname}score.json", 'w') as f:
            json.dump(teamscoredict, f, indent=2)
        print(f"'{teamname}' has been added.")
        print("what would you like to do?")
        print("1. enter another team")
        print("2. view current teams")
        print("3. return to participant manager")
        choice = int(input("enter option here: "))
        if choice == 1:
            add_team()
        elif choice == 2:
            view_teams()
        elif choice == 3:
            participant_manager()
        else:
            participant_manager()
######  ADD NEW TEAM    #####

######  REMOVE TEAM    #####
def remove_team():
    print("------------REMOVE TEAM------------")
    with open("teamstore.json", 'r',) as f:
        teamlist = json.load(f)
    if not teamlist:
        print("no teams found! returning to participant manager.")
        participant_manager()
    else:
        print(f"CURRENT TEAMS: {teamlist}")
        div()
        print("enter the name of the team you would like to remove. (case sensitive)")
        removaltarget = input("enter name here: ")
        if removaltarget in teamlist:
            teamlist.remove(removaltarget)
            with open("teamstore.json", 'w') as f:
                json.dump(teamlist, f, indent=2)
            if os.path.exists(f"{removaltarget}.json"):
                os.remove(f"{removaltarget}.json")
            if os.path.exists(f"{removaltarget}score.json"):
                os.remove(f"{removaltarget}score.json")
            print(f"{removaltarget} has been removed from the list successfully.")
            print("what would you like to do?")
            print("1. remove another team")
            print("2. return to participant manager")
            repeat = int(input("enter option here: "))
            if repeat == 1:
                remove_team()
            elif repeat == 2:
                participant_manager()
            else:
                participant_manager()
        else:
            print("the data you entered was invalid or not in the list! please try again.")
            remove_team()
######  REMOVE TEAM    #####

#####   VIEW TEAMS #####
def view_teams():
    print("------------VIEW TEAMS------------")
    with open("teamstore.json", 'r',) as f:
        teamlist = json.load(f)
        if not teamlist:
            print("no teams found!")
        else:
            print(teamlist)
    participantmanreturn()
#####   VIEW TEAMS #####

#####   VIEW PLAYERS IN TEAM #####
def view_players_in_team():
    print("------------VIEW PLAYERS IN TEAM------------")
    print("please select a team from the following list: ")
    with open("teamstore.json", 'r') as f:
        teamlist = json.load(f)
        if not teamlist:
            print("no teams found!")
            participantmanreturn()
        else:
            print(f"AVAILABLE TEAMS: {teamlist}")
            div()
            chosenteam = str(input("enter team name here: "))
            if chosenteam in teamlist:
                try:
                    with open(f"{chosenteam}.json", 'r') as f:
                        playersinteam = json.load(f)
                except:
                    with open(f"{chosenteam}.json", 'w') as f:
                        json.dump(emptylist, f, indent=2)
                with open("soloplayerstore.json", 'r') as f:
                    soloplayerlist = json.load(f)
                with open(f"{chosenteam}.json", 'r') as f:
                    playersinteam = json.load(f)
                div()
                print(f"PARTICIPANTS CURRENTLY IN {chosenteam}: {playersinteam}")
                print(f"{chosenteam} has {len(playersinteam)} participants.")
                div()
                participantmanreturn()
            else:
                print("team not found! please try again.")
                add_player_to_team()
#####   VIEW PLAYERS IN TEAM #####

#####   ADD PLAYER TO TEAM  #####
def add_player_to_team():
    print("------------ADD NEW MEMBER TO TEAM------------")
    print("please select a team from the following list: ")
    with open("teamstore.json", 'r') as f:
        teamlist = json.load(f)
        if not teamlist:
            print("no teams found!")
            participantmanreturn()
        else:
            print(f"AVAILABLE TEAMS: {teamlist}")
            div()
            chosenteam = str(input("enter team name here: "))
            if chosenteam in teamlist:
                try:
                    with open(f"{chosenteam}.json", 'r') as f:
                        playersinteam = json.load(f)
                except:
                    with open(f"{chosenteam}.json", 'w') as f:
                        json.dump(emptylist, f, indent=2)
                with open("soloplayerstore.json", 'r') as f:
                    soloplayerlist = json.load(f)
                with open(f"{chosenteam}.json", 'r') as f:
                    playersinteam = json.load(f)
                div()
                print(f"PARTICIPANTS CURRENTLY IN {chosenteam}: {playersinteam}")
                div()
                playertoadd = str(input("enter new participant name here: "))
                if playertoadd in playersinteam:
                    print(f"{playertoadd} is already a member of {chosenteam}!")
                    add_player_to_team()
                elif len(playersinteam)>=5:
                    print(f"{chosenteam} is full! please remove a member or make a new team.")
                    participantmanreturn()
                else:
                    playersinteam.append(playertoadd)
                    print(f"added {playertoadd} to {chosenteam}.")
                    with open(f"{chosenteam}.json", 'w') as f:
                        json.dump(playersinteam, f, indent=2)
                    print("what would you like to do?")
                    print("1. add another member")
                    print("2. view current members")
                    print("3. return to participant manager")
                    choice = int(input("enter option here: "))
                    if choice == 1:
                        add_player_to_team()
                    elif choice == 2:
                        with open(f"{chosenteam}.json", 'r') as f:
                            playersinteam = json.load(f)
                        div()
                        print(f"PARTICIPANTS CURRENTLY IN {chosenteam}: {playersinteam}")
                        div()
                        participantmanreturn()
                    elif choice == 3:
                        participant_manager()
                    else:
                        participant_manager()
            else:
                print("team not found! please try again.")
                add_player_to_team()
#####   ADD PLAYER TO TEAM  #####

#####   REMOVE PLAYER FROM TEAM  #####
def remove_player_from_team():
    print("------------REMOVE MEMBER FROM TEAM------------")
    print("please select a team from the following list: ")
    with open("teamstore.json", 'r') as f:
        teamlist = json.load(f)
        if not teamlist:
            print("no teams found!")
            participantmanreturn()
        else:
            print(f"AVAILABLE TEAMS: {teamlist}")
            div()
            chosenteam = str(input("enter team name here: "))
            if chosenteam in teamlist:
                try:
                    with open(f"{chosenteam}.json", 'r') as f:
                        playersinteam = json.load(f)
                except:
                    with open(f"{chosenteam}.json", 'w') as f:
                        json.dump(emptylist, f, indent=2)
                with open("soloplayerstore.json", 'r') as f:
                    soloplayerlist = json.load(f)
                with open(f"{chosenteam}.json", 'r') as f:
                    playersinevent = json.load(f)
                div()
                print(f"PARTICIPANTS CURRENTLY IN {chosenteam}: {playersinteam}")
                div()
                playertokill = str(input("enter the participant you wish to remove here here: "))
                if playertokill in playersinteam:
                    playersinteam.remove(playertokill)
                    with open(f"{chosenteam}.json", 'w') as f:
                        json.dump(playersinteam, f, indent=2)
                    print(f"{playertokill} has been removed from {chosenteam}.")
                    print("what would you like to do?")
                    print("1. remove another member")
                    print("2. view current members")
                    print("3. return to participant manager")
                    choice = int(input("enter option here: "))
                    if choice == 1:
                        remove_player_from_team()
                    elif choice == 2:
                        with open(f"{chosenteam}.json", 'r') as f:
                            playersinteam = json.load(f)
                        div()
                        print(f"PARTICIPANTS CURRENTLY IN {chosenteam}: {playersinteam}")
                        div()
                        participantmanreturn()
                    elif choice == 3:
                        participant_manager()
                    else:
                        participant_manager()
                else:
                    print(f"could not find {playertokill} in {chosenteam}!")
                    participantmanreturn()
            else:
                print("team not found! please try again.")
                remove_player_from_team()
#####   REMOVE PLAYER FROM TEAM  #####
# </editor-fold>

# <editor-fold desc="COMPETITION MANAGEMENT">
#####   COMPETITION MANAGER ######
def competition_manager():
    print("------------COMPETITION MANAGER------------")
    print("please choose from the following options: ")
    print("1. view team scores")
    print("2. view individual scores")
    print("3. edit team scores")
    print("4. edit individual scores")
    print("5. view team rankings")
    print("6. view individual rankings")
    print("6. return to main menu")
    div()
    choiceidentifier = int(input("enter option here: "))
    if choiceidentifier == 1:
        view_team_scores()
    elif choiceidentifier == 2:
        view_individual_scores()
    elif choiceidentifier == 3:
        edit_team_scores()
    elif choiceidentifier == 4:
        edit_individual_scores()
    elif choiceidentifier == 5:
        view_team_ranking()
    elif choiceidentifier == 6:
        view_individual_ranking()
    elif choiceidentifier == 7:
        main_menu()
#####   COMPETITION MANAGER ######

######  COMPETITION MANAGER RETURN    #####
def compmanreturn():
    compmanreturn = input("press enter to return to competition manager: ")
    competition_manager()
######  COMPETITION MANAGER RETURN    #####

#####   VIEW TEAM SCORES  #####
def view_team_scores():
    print("------------VIEW TEAM SCORES------------")
    print("please select a team from the following list: ")
    with open("teamstore.json", 'r') as f:
        teamlist = json.load(f)
        if not teamlist:
            print("no teams found!")
            compmanreturn()
        else:
            print(f"AVAILABLE teams: {teamlist}")
            div()
            chosenteam = str(input("enter team name here: "))
            with open(f"{chosenteam}score.json", 'r') as f:
                teamscoredict = json.load(f)
            if not teamscoredict:
                print("no scores found! please try again")
                compmanreturn()
            else:
                print(f"------------SCORES FOR {chosenteam}------------")
                print(teamscoredict)
                div()
                compmanreturn()
#####   VIEW TEAM SCORES  #####

#####   VIEW INDIVIDUAL SCORES  #####
def view_individual_scores():
    print("------------VIEW INDIVIDUAL SCORES------------")
    print("please select an individual from the following list: ")
    with open("soloplayerstore.json", 'r') as f:
        playerlist = json.load(f)
        if not playerlist:
            print("no participants found!")
            compmanreturn()
        else:
            print(f"AVAILABLE PARTICIPANTS: {playerlist}")
            div()
            chosenplayer = str(input("enter player name here: "))
            with open(f"{chosenplayer}score.json", 'r') as f:
                playerscoredict = json.load(f)
            if not playerscoredict:
                print("no scores found! please try again")
                compmanreturn()
            else:
                print(f"------------SCORES FOR {chosenplayer}------------")
                print(playerscoredict)
                div()
                compmanreturn()
#####   VIEW INDIVIDUAL SCORES  #####

#####   EDIT TEAM SCORES    #####
def edit_team_scores():
    print("------------EDIT TEAM SCORES------------")
    print("please select a team from the following list: ")
    with open("teamstore.json", 'r') as f:
        teamlist = json.load(f)
        if not teamlist:
            print("no teams found!")
            compmanreturn()
        else:
            print(f"AVAILABLE TEAMS: {teamlist}")
            div()
            chosenteam = str(input("enter team name here: "))
            div()
            with open(f"{chosenteam}score.json", 'r') as f:
                teamscoredict = json.load(f)
            if not teamscoredict:
                print("no scores found! please try again.")
                compmanreturn()
            else:
                print(f"------------SCORES FOR {chosenteam}------------")
                print(teamscoredict)
                div()
                print("please select a score to change: ")
                chosenscore = str(input("enter event name here: "))
                currentscore = teamscoredict[f"{chosenscore}"]
                print(f"the current score for {chosenscore} is: {currentscore}.")
                print("please enter the amount you would like to change the score by.")
                change = int(input("enter amount here: "))
                teamscoredict[f"{chosenscore}"] = currentscore + change
                print(f"{chosenscore} has been changed by {change}. current scores for {chosenteam}: {teamscoredict}")
                with open(f"{chosenteam}score.json", 'w') as f:
                    json.dump(teamscoredict, f, indent=2)
                with open("teamranks.json", 'r') as f:
                    teamranks = json.load(f)
                scoresum = sum(teamscoredict.values())
                teamranks.update({chosenteam:scoresum})
                print(teamranks)
                with open("teamranks.json", 'w') as f:
                    json.dump(teamranks, f, indent=2)
                compmanreturn()
#####   EDIT TEAM SCORES    #####

#####   EDIT INDIVIDUAL SCORES    #####
def edit_individual_scores():
    print("------------EDIT INDIVIDUAL SCORES------------")
    print("please select an individual from the following list: ")
    with open("soloplayerstore.json", 'r') as f:
        playerlist = json.load(f)
        if not playerlist:
            print("no participants found!")
            compmanreturn()
        else:
            print(f"AVAILABLE PARTICIPANTS: {playerlist}")
            div()
            chosenplayer = str(input("enter player name here: "))
            div()
            with open(f"{chosenplayer}score.json", 'r') as f:
                playerscoredict = json.load(f)
            if not playerscoredict:
                print("no scores found! please try again.")
                compmanreturn()
            else:
                print(f"------------SCORES FOR {chosenplayer}------------")
                print(playerscoredict)
                div()
                print("please select a score to change: ")
                chosenscore = str(input("enter event name here: "))
                currentscore = playerscoredict[f"{chosenscore}"]
                print(f"the current score for {chosenscore} is: {currentscore}.")
                print("please enter the amount you would like to change the score by.")
                change = int(input("enter amount here: "))
                playerscoredict[f"{chosenscore}"] = currentscore + change
                print(f"{chosenscore} has been changed by {change}. current scores for {chosenplayer}: {playerscoredict}")
                with open(f"{chosenplayer}score.json", 'w') as f:
                    json.dump(playerscoredict, f, indent=2)
                with open("soloranks.json", 'r') as f:
                    soloranks = json.load(f)
                scoresum = sum(playerscoredict.values())
                soloranks.update({chosenplayer: scoresum})
                print(soloranks)
                with open("soloranks.json", 'w') as f:
                    json.dump(soloranks, f, indent=2)
                    compmanreturn()
#####   EDIT INDIVIDUAL SCORES    #####

#####   VIEW TEAM RANKING   #####
def view_team_ranking():
    with open("teamranks.json", 'r') as f:
        teamranks = json.load(f)
    print("------------VIEW TEAM RANKING------------")
    if not teamranks:
        print("no team rankings found! please add teams or assign scores.")
        compmanreturn()
    else:
        print("TEAM RANKINGS: ")
        keys = list(teamranks.keys())
        values = list(teamranks.values())
        sorted_ascending = np.argsort(values)
        sorted_descending = sorted_ascending[::-1]
        sorted_dict = {keys[i]: values[i] for i in sorted_descending}
        for index, (key, value) in enumerate(sorted_dict.items(), start=1):
            print(f"{index}: {key}-{value}")
#####   VIEW TEAM RANKING   #####

#####   VIEW INDIVIDUAL RANKING   #####
def view_individual_ranking():
    with open("soloranks.json", 'r') as f:
        soloranks = json.load(f)
    print("------------VIEW INDIVIDUAL RANKING------------")
    if not soloranks:
        print("no individual rankings found! please add individuals or assign scores.")
        compmanreturn()
    else:
        print("INDIVIDUAL RANKINGS: ")
        keys = list(soloranks.keys())
        values = list(soloranks.values())
        sorted_ascending = np.argsort(values)
        sorted_descending = sorted_ascending[::-1]
        sorted_dict = {keys[i]: values[i] for i in sorted_descending}
        for index, (key, value) in enumerate(sorted_dict.items(), start=1):
            print(f"{index}: {key}-{value}")
#####   VIEW INDIVIDUAL RANKING   #####
# </editor-fold>

def testing_func():
    with open("soloranks.json", 'r') as f:
        soloranks = json.load(f)
    print("------------VIEW INDIVIDUAL RANKING------------")
    print("INDIVIDUAL RANKINGS: ")
    keys = list(soloranks.keys())
    values = list(soloranks.values())
    sorted_ascending = np.argsort(values)
    sorted_descending = sorted_ascending[::-1]
    sorted_dict = {keys[i]: values[i] for i in sorted_descending}
    for index, (key, value) in enumerate(sorted_dict.items(), start=1):
        print(f"{index}: {key}-{value}")

# <editor-fold desc="MAIN CODE">
#####   MAIN CODE   #####
with open("teameventstore.json", 'r',) as f:
    teameventlist = json.load(f)
with open("individualeventstore.json", 'r',) as f:
    individualeventlist = json.load(f)
with open("soloplayerstore.json", 'r',) as f:
    soloplayerlist = json.load(f)
with open("teamstore.json", 'r',) as f:
    teamlist = json.load(f)
main_menu()
######  MAIN CODE   #####
# </editor-fold>