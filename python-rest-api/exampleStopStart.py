import oci
from oci.config import from_file
import atp, regions
import sys

"""
Example scripts demonstrating how to use the ATP Rest APIs for python

Usage:
python exampleStopStart.py start 

Anything other that start parameter will stop the database
"""


#Setup
config = from_file(file_location="./oci-config")
compartment_id = config["tenancy"]

exampleId = "ocid1.autonomousdatabase.oc1.phx.abyhqljrqk5u3gcjwoun7lwdrrwtxm4tmfi4fule7dmf5o42s3d5x62is7wq"

try:
	if sys.argv[1] == "start":
		
		exampleStart = atp.startAutonomousDatabase(config, regions.dbPhoenixRegion, exampleId)

		print("Response: " + str(exampleStart) +"\nStarting the instance!")

	elif sys.argv[1] == "stop":

		exampleStop = atp.stopAutonomousDatabase(config, regions.dbPhoenixRegion, exampleId)

		print("Response: " + str(exampleStop) + "\nStoping the instance!")

	else:
		print ("Please say start or stop!")


except Exception as e: 
	print(e)



