# Create Policy Nodes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/http-in-properties>

The Create Policy consists of the following nodes:

- HTTP In Node
- Script Node
- Insert Node
- HTTP Out Node

**HTTP In Node**

![](/resources/Storage/server-services-designer-9/httpin.png)

**Script Node**

The properties within the script node contains information related to customer policy.

![](/resources/Storage/server-services-designer-9/ScriptProperties.png)

```
bh.policy_data = {    "policy_id": 10,    "agent": "AG_034",    "policy_details": {      "policy_number": "ABC123",      "policy_type": "Auto",      "policy_start_date": "2022-01-01",      "policy_end_date": "2023-01-01",      "premium_amount": 1000,      "coverage": {        "liability": {          "bodily_injury": 25000,          "property_damage": 50000        }      }    },    "claims": 12,    "claim": [      {        "claim_id": 20,        "claim_type": "vehicle",        "claim_date": "2023-04-17T12:01:18.867Z",        "claim_amount": 50000,        "claim_status": true      }    ]  }
```

| ![Information](/resources/Storage/server-services-designer-9/info.png) | The values provided in the above script can be customized as per your requirement. You can also use the bh.model variable to map the body dynamically. |
| --- | --- |

**Insert Node**

**![](/resources/Storage/server-services-designer-9/Insertproperties.png)**

**HTTP Out Node**

**![](/resources/Storage/server-services-designer-9/HTTPOUT.png)**
