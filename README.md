# Tracardi plugin

This code can be run within Tracardi workflow.

# Sending mail with tracarti

The purpose of this plugin is valide data with custom regex. 


# Configuration

This node require configuration.
*validation_regex - Paste here your regex. 
*data - Here is data what we want to validate

# Examples
```json
    {"validation_regex":"^h",
    "data":"hello!"


```
It will return True
```json
    {"validation_regex":"^a",
    "data":"hello!"


```
It will return False

# Input payload
This node does not process input payload.

# Output

This is two output True and False.
