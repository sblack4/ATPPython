import oci
from oci.config import from_file
import atp, regions
import sys

"""
Example scripts demonstrating how to use the ATP Rest APIs for python

Usage:
python exampleCreate.py DatabaseName Password CPUCount StorageSizeInTBs

"""


#Setup
config = from_file(file_location="../oci-config")
compartment_id = config["tenancy"]

try:
	#Database body to create
	body = {
		  "compartmentId" : compartment_id,
		  "displayName" : sys.argv[1],
		  "dbName" : sys.argv[1],
		  "adminPassword" : sys.argv[2],
		  "cpuCoreCount" : int(sys.argv[3]),
		  "dataStorageSizeInTBs" : int(sys.argv[4])
	}

	#Example restoreTime
	restoreTime = "2018-09-27T01:59:07.032Z"

	#Example update body
	update = { "cpuCoreCount" : 1 }
	print(regions.dbPhoenixRegion)

	exampleUpdate = atp.createAutonomousDatabase(config, body, regions.dbPhoenixRegion)

	#Get the ID of the ATP instance just created
	#exampleId = exampleCreate.json()['id']

except Exception as e: 
	print(e)


