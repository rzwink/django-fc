from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from pyteamsnap.api import Event
from pyteamsnap.api import EventLineupEntry
from pyteamsnap.api import Me
from pyteamsnap.api import Member
from pyteamsnap.api import Team
from pyteamsnap.api import TeamSnap


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        client = TeamSnap(token=settings.TEAM_SNAP_TOKEN)

        # get authenticated user
        me = Me(client)

        print(str(me.data["id"]))

        teams = Team.search(client, user_id=me.data["id"])
        # print(teams)
        for team in teams:
            print(team.data["id"])
            members = Member.search(client, team_id=team.data["id"])
            for member in members:
                if not member.data["is_non_player"]:
                    print(member.data["first_name"])

            events = Event.search(client, team_id=team.data["id"])
            for event in events:
                print(f"location_id {event.data['location_id']}")
                print(f"location_name {event.data['location_name']}")
                print(f"name {event.data['name']}")
                print(f"opponent_id {event.data['opponent_id']}")
                print(f"arrival_date {event.data['arrival_date']}")

        # # get a list of team_ids for the user
        # managed_team_ids = me.data['managed_teams']
        #
        # print(managed_team_ids)

        #
        # # get a list of events for managed team
        # managed_team_id = me.data['managed_teams'][0]
        # events = Event.search(client, team_id=managed_team_id)
        #
        # # get an object with the object id of EVENT_ID
        # event = Event.get(client, id=EVENT_ID)
        #
        # # get some information about the event
        # start_date = event.data['start_date']
        #
        # # create a new member
        # member = Member.new(client)
        # member.data['first_name'] = 'Ferguson'
        # member.post()

        # perform a bulk load
        # list_of_ts_objects = client.bulk_load(team_id=TEAM_ID, types=[Event, Member], event__id=EVENT_ID)

        # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
