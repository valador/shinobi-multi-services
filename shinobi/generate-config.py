#!/usr/bin/python3

import os
import json
import sys

CONFIG_SOURCE = "/config/config.default.json"

MYSQL_HOST_PARAMETER = "MYSQL_HOST"
MYSQL_PORT_PARAMETER = "MYSQL_PORT"
MYSQL_USER_PARAMETER = "MYSQL_USER"
MYSQL_PASSWORD_PARAMETER = "MYSQL_PASSWORD"
MYSQL_DATABASE_PARAMETER = "MYSQL_DATABASE"
CRON_KEY_PARAMETER = "CRON_KEY"
MOTION_KEY_PARAMETER = "MOTION_KEY"
OPENCV_KEY_PARAMETER = "OPENCV_KEY"
OPENALPR_KEY_PARAMETER = "OPENALPR_KEY"

config_destination = os.path.join(os.environ["SHINOBI_INSTALL_DIRECTORY"], "conf.json")

with open(CONFIG_SOURCE, "r") as file:
    configuration = json.load(file)

if "db" not in configuration:
    configuration["db"] = {
        "host": os.environ[MYSQL_HOST_PARAMETER],    
        "port": os.environ[MYSQL_PORT_PARAMETER],
        "user": os.environ[MYSQL_USER_PARAMETER],
        "password": os.environ[MYSQL_PASSWORD_PARAMETER],
        "database": os.environ[MYSQL_DATABASE_PARAMETER]
    }

if "cron" not in configuration:
    configuration["cron"] = {
        "key": os.environ[CRON_KEY_PARAMETER]
    }

if "pluginKeys" not in configuration:
    configuration["pluginKeys"] = {
        "Motion": os.environ[MOTION_KEY_PARAMETER],    
        "OpenCV": os.environ[OPENCV_KEY_PARAMETER],
        "OpenALPR": os.environ[OPENALPR_KEY_PARAMETER]
    }

with open(config_destination, "w") as file:
    json.dump(configuration, file, sort_keys=True, indent=4)

print("Generated Shinobi configuration: %s" % (config_destination, ), file=sys.stderr)
