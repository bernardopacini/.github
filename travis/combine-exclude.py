import configparser
import sys

# the file to merge with .flake8
FL8 = sys.argv[1]
# default config
config_def = configparser.ConfigParser()
config_def.read(".flake8")
# project config
config_prj = configparser.ConfigParser()
config_prj.read(FL8)

# add the exclude sections together
config_prj[".flake8"]["exclude"] += config_def[".flake8"]["exclude"]
# overwrite the project config with added section from default config
with open(FL8, "w") as configfile:
    config_prj.write(configfile)