import oci
from oci.config import from_file
import atp, regions
import sys

"""
Example scripts demonstrating how to use the ATP Rest APIs for python

Usage:
python exampleUpdate.py cpuCoreCount

"""


#Setup
config = from_file(file_location="../oci-config")
compartment_id = config["tenancy"]

#Can be added as possible argument
ocid = "ocid1.autonomousdatabase.oc1.phx.abyhqljrqk5u3gcjwoun7lwdrrwtxm4tmfi4fule7dmf5o42s3d5x62is7wq"

try:

	#Example update body
	update = { "cpuCoreCount" : int(sys.argv[1]) }

	exampleUpdate = atp.updateAutonomousDatabase(config, update, regions.dbPhoenixRegion, ocid)

	print("Instance is being updated to have a CPU Core Count of" + sys.argv[1])


except Exception as e: 
	print(e)