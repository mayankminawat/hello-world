
"""
Created By  : Chandru Basavaraju
Created ON  : 4/17/2019
Objective   : Notify orphan HCRs (HCR with no LO)
Description : The following procedure extracts the orphan HCRs and notifies the owners for
                corrective action
Change Log  :
09/22/2019 - Removed Zone filter for the network wide launch of AHA - Chandru Basavaraju
"""

import sys
import datetime

import pandas as pd
import pytz
import os
import numpy as np

from wfs3_data_pipeline import getaccess
from wfs3_data_pipeline import errorlog
from wfs3_data_pipeline import logger
from wfs3_data_pipeline import email
from wfs3_data_pipeline import db_connect
from wfs3_data_pipeline import read_from_s3
from wfs3_data_pipeline import redshift_to_s3
from wfs3_data_pipeline import s3_to_df
import json,subprocess,shlex


def notify_orphan_hcr_v2():
    try:
        e = ''

        file = open(os.getcwd() + '/env.txt', 'r')  # get environment to execute in
        exec_env = str(file.read())

        logger.log('orphan_hcr_notification', 'start', str(e).replace("'", ""))

        new_email = "mminawat@amazon.com"

        # this will act as a default dictionary and then we will append other email addresses to this dict variable
        data = {
            "Source": "wfs-businessintel@amazon.com",
            "Template": "WFS_BI_AHA_HCR_Notification_HCR_Only",
            "ConfigurationSetName": "AHA_HCR_Notification_Cofig_Set",
            "Destinations": [
                {
                    "Destination": {
                        "ToAddresses": [
                            ""
                        ]
                    },
                    "ReplacementTemplateData": "{\"table_hcr\":\"HCR_Table\", \"table_lo\":\"LO_Table\"}"
                }
            ],
            "DefaultTemplateData": "{ \"table_hcr\":\"HCR_Table\", \"table_lo\":\"LO_Table\" }"
        }

        data['Destinations'].insert(1, {'Destination': {'ToAddresses': [new_email]}, 'ReplacementTemplateData': "{\"table_hcr\":\"HCR_Table\", \"table_lo\":\"LO_Table\"}"})

        print("Writing JSON file")
        with open('/home/temp/mybulkemail_aha_hcr.json', 'w+') as outfile:
            outfile.truncate(0)
            json.dump(data, outfile)

        cmd = '/apollo/env/AmazonAwsCli/bin/aws ses send-bulk-templated-email --cli-input-json file:///home/temp/mybulkemail_aha_hcr.json'

        # execution of command
        print("Sending out emails now..")
        subprocess.check_output(shlex.split(cmd), shell=False, stderr=subprocess.STDOUT)
        # log process to database after each run
        logger.log('orphan_hcr_notification', 'end', str(e).replace("'", ""))

    except Exception as e:
        raise (e)
        # log error to database on run
        logger.log('orphan_hcr_notification', 'end', str(e).replace("'", ""))
        # log process to a local file for email notification
        # errorlog.log_error('orphan_hcr_notification', 'none', e, 'orphan_hcr_notification.csv')
        # error email will be sent if error occured.
        # email.notify_error('orphan_hcr_notification.csv')
        # exit with error
        # sys.exit(1)


def main():
    notify_orphan_hcr_v2()


if __name__ == "__main__":
    main()