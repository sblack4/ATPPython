
# OCI PYTHON

These scripts are intended to help any python developer get started connecting to Oracle Autonomous Database, as well as easily creating, updating, restoring, starting, stopping, etc. Follow the instructions to use the scripts already created here. Feel free to go into the code and learn for yourself as you get started.

# Getting Started - OCI-CONFIG

Open up your oci-config file to ensure that you have the correct information in place in order to get started

### **STEP 1**: OCI-CONFIG


-	Below is an example oci-config file. It is standard practice to leave all variables in this file lowercase

```

  [DEFAULT]
  user=ocid1.user.oc1..aaaaaaaa4tfljmeejbutmrydmms62ooqdl2ay4x52m2xutb35nylnn6vupja
  fingerprint=d3:5b:36:21:2e:82:4b:b2:cf:de:31:4f:df:f2:ba:ad
  key_file=./oci_api_key.pem
  tenancy=ocid1.tenancy.oc1..aaaaaaaawrgt5au6hbledhhyas2secm3q2atqiuvihck45rbi3jyc5tfyfga
  region=us-phoenix-1
  compartmentId=ocid1.tenancy.oc1..aaaaaaaawrgt5au6hbledhhyas2secm3q2atqiuvihck45rbi3jyc5tfyfga



```


```


### **STEP 4**: Interact with Autonomous Database.

Now that you have setup OCI CLI, try your hand at using Autonomous Database


-	Here is a list of several OCI commands with their **required** options:

**Creating Database**
```

oci db autonomous-database create --admin-password [password] --compartment-id [OCID] --cpu-core-count [integer] --data-storage-size-in-tbs [integer] --db-name [Database Name]

```


**Deleting Database**
```

