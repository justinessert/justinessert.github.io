import os

bracket_data = {
    "east": [
        "uconn",
        "north_carolina",
        "illinois",
        "iowa_state",
        "south_carolina",
        "kentucky",
        "texas",
        "michigan_state",
        "boise_state",
        "texas_a&m",
        "indiana_state",
        "mcneese_state",
        "south_florida",
        "vermont",
        "colgate",
        "green_bay"
    ],
    "west": [
        "arizona",
        "tennessee",
        "wisconsin",
        "baylor",
        "creighton",
        "byu",
        "texas_tech",
        "virginia",
        "new_mexico",
        "butler",
        "ole_miss",
        "grand_canyon",
        "akron",
        "high_point",
        "troy",
        ["north_dakota", "grambling_state"]
    ],
    "midwest": [
        "purdue",
        "kansas",
        "auburn",
        "duke",
        "florida_atlantic",
        "colorado_state",
        "clemson",
        "saint_marys",
        "tcu",
        "florida",
        "nebraska",
        "samford",
        "cornell",
        "unc_wilmington",
        "east_washington",
        ["merrimack", "nc_central"]
    ],
    "south": [
        "houston",
        "marquette",
        "alabama",
        "dayton",
        "san_diego_state",
        "oklahoma",
        "utah_state",
        "utah",
        "northwestern",
        ["mississippi_state", "cincinnati"],
        ["washington_state", "seton_hall"],
        "uc_irvine",
        "lousiana_tech",
        "morehead_state",
        "quinnipiac",
        "eastern_kentucky"
    ]
}
nicknames = {
    "akron": "zips",
    "alabama": "crimson tide",
    "arizona_state": "sun devils",
    "arizona": "wildcats",
    "arkansas": "razorbacks",
    "auburn": "tigers",
    "baylor": "bears",
    "boise_state": "broncos",
    "bryant": "bulldogs",
    "butler": "bulldogs",
    "byu": "cougars",
    "charleston": "cougars",
    "chattanooga": "mocs",
    "cincinnati": "bearcats",
    "clemson": "tigers",
    "cleveland_state": "vikings",
    "colgate": "raiders",
    "colorado_state": "rams",
    "cornell": "big red",
    "creighton": "bluejays",
    "csu_fullerton": "titans",
    "davidson": "wildcats",
    "dayton": "flyers",
    "delaware": "blue hens",
    "drake": "bulldogs",
    "duke": "blue devils",
    "eastern_kentucky": "colonels",
    "east_washington": "eagles",
    "fdu": "knights",
    "florida": "gators",
    "florida_atlantic": "owls",
    "furman": "paladins",
    "georgia_state": "panthers",
    "gonzaga": "bulldogs",
    "grambling_state": "tigers",
    "grand_canyon": "antelopes",
    "green_bay": "phoenix",
    "high_point": "purple panthers",
    "houston": "cougars",
    "howard": "bison",
    "illinois": "fighting illini",
    "indiana": "hoosiers",
    "indiana_state": "sycamores",
    "iona": "gaels",
    "iowa_state": "cardinals",
    "iowa": "hawks",
    "jacksonville_state": "gamecocks",
    "kansas_state": "wildcats",
    "kansas": "jayhawks",
    "kennesaw_state": "owls",
    "kent_state": "golden flashes",
    "kentucky": "wildcats",
    "long_beach_state": "the beach",
    "longwood": "lancers",
    "louisiana": "ragin cajuns",
    "lousiana_tech": "bulldogs",
    "loyola_chicago": "ramblers",
    "lsu": "tigers",
    "marquette": "golden eagles",
    "maryland": "terrapins",
    "mcneese_state": "cowboys",
    "memphis": "tigers",
    "merrimack": "warriors",
    "miami": "hurricanes",
    "michigan_state": "spartans",
    "michigan": "wolverines",
    "mississippi_state": "bulldogs",
    "missouri": "mizzou",
    "montana_state": "fighting bobcats",
    "morehead_state": "eagles",
    "murray_state": "racers",
    "nc_central": "eagles",
    "nc_state": "wolfpack",
    "nebraska": "cornhuskers",
    "new_mexico": "lobos",
    "new_mexico_state": "aggies",
    "new_orleans": "privateers",
    "norfolk_state": "spartans",
    "north_carolina": "tar heels",
    "north_dakota": "fighting hawks",
    "north_texas": "mean green",
    "northern_iowa": "panthers",
    "northern_kentucky": "norse",
    "northwestern": "wildcats",
    "notre_dame": "fighting irish",
    "ohio_state": "buckeyes",
    "oklahoma": "sooners",
    "ole_miss": "rebels",
    "oral_roberts": "golden eagles",
    "penn_state": "nittany lions",
    "pittsburgh": "panthers",
    "providence": "friars",
    "purdue": "boilmakers",
    "quinnipiac": "bobcats",
    "richmond": "spiders",
    "rutgers": "scarlet knights",
    "saint_marys": "gaels",
    "saint_peters": "peacocks",
    "samford": "bulldogs",
    "san_diego_state": "aztecs",
    "san_francisco": "dons",
    "seton_hall": "pirates",
    "south_carolina": "gamecocks",
    "south_dakota_state": "jackrabbits",
    "south_florida": "bulls",
    "southeast_missouri_state": "redhawks",
    "tcu": "horned frogs",
    "tennessee": "volunteers",
    "texas_a&m_cc": "islanders",
    "texas_a&m": "aggies",
    "texas_southern": "tigers",
    "texas_state": "bobcats",
    "texas_tech": "red raiders",
    "texas": "longhorns",
    "toledo": "rockets",
    "troy": "trojans",
    "uab": "blazers",
    "ucla": "bruins",
    "uconn": "huskies",
    "ucsb": "bison",
    "uc_irvine": "anteaters",
    "unc_asheville": "bulldogs",
    "unc_wilmington": "seahawks",
    "usc": "trojans",
    "utah": "utes",
    "utah_state": "aggies",
    "vcu": "rams",
    "vermont": "catamounts",
    "villanova": "wildcats",
    "virginia_tech": "hokies",
    "virginia": "cavaliers",
    "wagner": "seahawks",
    "wake_forest": "demon deacons",
    "washington_state": "cougars",
    "west_virginia": "mountaineers",
    "wisconsin": "badgers",
    "wright_state": "raiders",
    "wyoming": "cowboys",
    "xavier": "musketeers",
    "yale": "bulldogs",
    "nevada": "wolf pack",
    "princeton": "tigers"
}

if __name__ == "__main__":
    missing_files = []
    missing_nicknames = []
    for region, region_data in bracket_data.items():
        for team_names in region_data:
            team_names = team_names if isinstance(team_names, list) else [team_names]
            for team_name in team_names:
                if not os.path.exists(f"mascot/img/{team_name}.jpg"):
                    missing_files.append(team_name)
                if not team_name in nicknames:
                    missing_nicknames.append(team_name)
    
    print("Missing Nicknames:")
    for missing_nickname in missing_nicknames:
        print(f"- {missing_nickname}")

    print("Missing Files:")
    for missing_file in missing_files:
        print(f"- {missing_file}")