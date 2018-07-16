#!/usr/bin/env python

import os
import boto.ec2

conn = boto.ec2.connect_to_region("us-west-2",
		aws_access_key_id = os.getenv("AWS_ACCESS"),
		aws_secret_access_key = os.getenv("AWS_SECRET") )

reservations = conn.get_all_reservations()
instances = reservations[0].instances

inst = instances[0]
print (inst.instance_type)