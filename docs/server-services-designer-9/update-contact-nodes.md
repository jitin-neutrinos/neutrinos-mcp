# Update Contact Nodes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/update-contact-nodes>

The Update Contact Details consists of the following nodes:

- Update_Contact (HTTP In)
- Script
- Update
- HTTP Out

**Update_Contact (HTTP In)**

![](/resources/Storage/server-services-designer-9/updateconthttpin.png)

**Script**

**![](/resources/Storage/server-services-designer-9/update-contact-nodes-2023-05-04.png)
**

```
bh.contact = {    "contact_id": 2}bh.contact_details = {    "contact_id": 2,    "email": "customer03@gmail.com",    "phone_number": 9900336546,    "address": "bengaluru, India",    "customer_data": "string"  }
```

**Update**

**![](/resources/Storage/server-services-designer-9/update-contact-nodes-2023-05-04-1.png)
**

**HTTP Out**

**![](/resources/Storage/server-services-designer-9/update-contact-nodes-2023-05-04-2.png)
**
