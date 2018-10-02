
# Introduction

This lab walks you through some examples using the Oracle Cloud Infrastructure Command Line Interface for Autonomous Transaction Processing

# Oracle Cloud Infrastructure Command Line Interface

The CLI is a small footprint tool that you can use by itself, or with the Console to complete Oracle Cloud Infrastructure tasks. The CLI provides much the same functionality as the Console and includes additional advanced commands. Some of these commands, such as the ability to run scripts, extend the Console's functionality.

### **STEP 1**: Install Oracle Cloud Infrastructure Command Line Interface (THIS IS DONE BY THE DOCKER IMAGE)


-	To Install OCI CLI, run the following command in your putty session:

```

  bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

```

### **STEP 2**: Configure OCI CLI

-	To use OCI CLI Commands you must create a public key and add it to your Oracle Cloud Infrastructure user settings. This can be completed using the following command:

```

  oci setup config

```

- Follow the prompts. If you are unsure of what you should enter, most is available in the browser OCI console

#### Refer to this guide:

**USER OCID** = located on your user information page in OCI console

**TENANCY OCID** = Located in the bottom left of your OCI console

**KEY_FILE** = this is the path to your private key that you configured during oci setup

**COMPARTMENT ID** = you can find this in Identity -> Compartments -> <your-compartment> -> select **Show** under OCID

**REGION** = located at the top of the OCI Console next to tenancy


### **STEP 3**: Provide Oracle Autonoumous with the OCI CLI public key that was created in oci setup config.

Now that you have a private / public key combo , you must add it to OCI Console:

- Add it to your OCI user settings:
  - Go to your Oracle Cloud Infrastructure console and select User Settings on the user dropdown in the top right corner.
  - Select Add Public Key and add the public key you copied from the command line interface.
- You should now be able to access your Autonomous instances from the command line.

- If for whatever reason you still cannot connect, try running the following command and follow the prompts:

```
oci setup autocomplete
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

 oci db autonomous-database delete --autonomous-database-id [OCID]

```

**Get Database**
```

oci db autonomous-database get --autonomous-database-id [OCID]

```

**Listing Databases**
```

oci db autonomous-database list --compartment-id [OCID]

```

**Restore Database**
```

oci db autonomous-database restore --autonomous-database-id [OCID] --timestamp [datetime]

```

**Start Database**
```

oci db autonomous-database start --autonomous-database-id [OCID]

```

**Stop Database**
```

oci db autonomous-database stop --autonomous-database-id [OCID]

```

**Update Database**
```

oci db autonomous-database update --autonomous-database-id [OCID] --cpu-core-count [integer]

```


# What you Learned

How to:
-	Create Autonomous Database in Oracle Cloud Infrastructure console
-	Download OCI CLI and use it to interact with object Autonomous Database.


# Want to Learn More?

- [OCI CLI Documentation](https://raw.githubusercontent.com/oracle/oci-cli/master/tests/output/inline_help_dump.txt)

- [Autonomous Database Overview](https://docs.cloud.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/db/autonomous-database.html)

- [The Power of Oracle Cloud Infrastructure CLI](https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/cliconcepts.htm)
