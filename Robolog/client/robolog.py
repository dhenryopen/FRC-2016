# Shared functions

import ConfigParser

# Used with the configuration files (e.g. robolog.cfg)

Config = ConfigParser.RawConfigParser()


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


def ParseConfig(cfg_file):
    dict1 = {}
    Config.read(cfg_file)  # e.g. read robolog.cfg

    # Assign configuration values to dictionary variables
    # Values should be set by set_robolog_config.py using set_robolog_config.sh

    # Specific to CKAN
    section_ckan = "robolog:ckan"

    dict1['ckan_apikey'] = ConfigSectionMap(section_ckan)['ckan_apikey']
    dict1['ckan_package_id'] = ConfigSectionMap(section_ckan)['ckan_name']
    dict1['ckan_apikey'] = ConfigSectionMap(section_ckan)['ckan_apikey']
    dict1['ckan_author'] = ConfigSectionMap(section_ckan)['ckan_author']
    dict1['ckan_author_email'] = ConfigSectionMap(section_ckan)['ckan_author_email']
    dict1['ckan_maintainer'] = ConfigSectionMap(section_ckan)['ckan_maintainer']
    dict1['ckan_maintainer_email'] = ConfigSectionMap(section_ckan)['ckan_maintainer_email']
    dict1['ckan_name'] = ConfigSectionMap(section_ckan)['ckan_name']
    dict1['ckan_notes'] = ConfigSectionMap(section_ckan)['ckan_notes']
    dict1['ckan_owner_org'] = ConfigSectionMap(section_ckan)['ckan_owner_org']
    dict1['ckan_title'] = ConfigSectionMap(section_ckan)['ckan_title']
    dict1['ckan_version'] = ConfigSectionMap(section_ckan)['ckan_version']

    # Specific to Robolog
    section_frc = "robolog:frc"

    dict1['cfg_file'] = ConfigSectionMap(section_frc)['cfg_file']
    dict1['district'] = ConfigSectionMap(section_frc)['district']
    dict1['driver'] = ConfigSectionMap(section_frc)['driver']
    dict1['event'] = ConfigSectionMap(section_frc)['event']
    dict1['eventlat'] = ConfigSectionMap(section_frc)['eventlat']
    dict1['eventlon'] = ConfigSectionMap(section_frc)['eventlon']
    dict1['match'] = ConfigSectionMap(section_frc)['match']
    dict1['robot'] = ConfigSectionMap(section_frc)['robot']
    dict1['server'] = ConfigSectionMap(section_frc)['server']
    dict1['station'] = ConfigSectionMap(section_frc)['station']
    dict1['teamname'] = ConfigSectionMap(section_frc)['teamname']
    dict1['teamnumber'] = ConfigSectionMap(section_frc)['teamnumber']
    return dict1
