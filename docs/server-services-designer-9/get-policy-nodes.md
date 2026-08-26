# Get Policy Nodes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/get-policy-nodes>

The Get Policy consists of the following nodes:

- HTTP In
- Find
- Script
- HTTP Out

**HTTP In**

**![](/resources/Storage/server-services-designer-9/Getpost.png)
**

**Find**

Contains information with regards to retrieving details about customer policy.

**Get Policy Script**

**![](/resources/Storage/server-services-designer-9/Getpolicyscript.png)
**

```
console.log("Policy Details",bh.policy_result)
```

HTTP Out

![](/resources/Storage/server-services-designer-9/Getpolicyhttpout.png)
