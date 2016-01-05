import ConfigParser

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.

# ---- STARTER CODE

config.add_section('robolog')

config.set('robolog', 'author', 'Dave Henry')
config.set('robolog', 'author_email', 'dshenry99@gmail.com')
config.set('robolog', 'district', 'District.PNW')
config.set('robolog', 'event', 'Event.PRACT')
config.set('robolog', 'eventlat', 'EventLat.48.101')
config.set('robolog', 'eventlon', 'EventLon.-122.799')
config.set('robolog', 'maintainer', 'Dave Henry')
config.set('robolog', 'maintainer_email', 'dshenry99@gmail.com')
config.set('robolog', 'match', 'Match.P1')    # need a separate, simple utility to set the current match from a CLI
config.set('robolog', 'notes', 'Log generated during team practice')
config.set('robolog', 'owner_org', 'team-4918')
config.set('robolog', 'robot', 'Robot.BUSTER')
config.set('robolog', 'teamname', 'TeamName.Roboctopi')
config.set('robolog', 'teamnumber', 'TeamNumber.4918')
config.set('robolog', 'version', '0.9')

# Write the configuration file to 'robolog.cfg'
with open('robolog.cfg', 'wb') as configfile:
    config.write(configfile)

# ---- END STARTER CODE

# Now read it back again
config = ConfigParser.RawConfigParser()
config.read('robolog.cfg')
print dict(config.items('robolog'))