# Create Handlebars for cid

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/handlebar-apis>

Handlebars is a templating mechanism used to dynamically render content by binding structured data to predefined templates. Handlebars enables platforms to generate consistent, data-driven output (such as web pages, emails, notifications, or documents) without hardcoding content logic into the presentation layer.

## Create Handlebars for cid

To create handlebars for cid, follow the steps:

In the Swagger file downloaded from the platform, provide the required details in the JSON payload to generate an HTML template using data fetched for a specific CID. The following JSON example illustrates a sample payload with CID 4380.

```json
{
  "schemaName": "test handlebars",
  "version": "1.0.0",
  "recordId": "b4743762-706a-4964-8136-c00003f75142",
  "cid": 4380
}
```

- **schemaName**: Specifies the name of the schema created on the platform.
- **version**: Specifies the version of the schema used to generate the HTML template.
- **recordId**: Specifies the record from which data is fetched and added to the HTML template.
- **cid**: Specifies the case ID for which an HTML template is generated.

Upon successful execution of the JSON payload, the API returns an output containing the details defined in the template. In this example, the response includes case-related information such as the CID, PID, case creation date and time, and other relevant fields. The sample output is illustrated below:

```json
{
    "success": true,
    "message": "Content created for schema = test handlebars, recordId = b4743762-706a-4964-8136-c00003f75142, cid = 4380 successfully.",
    "data": {
        "id": "b4743762-706a-4964-8136-c00003f75142",
        "age": "",
        "info": "<p>## Case Summary</p><p>### Case Details</p><p>- **Case ID (CID):** 4380</p><p>- **Process Instance ID (PIID):** 4571</p><p>- **Case Definition ID (CDID):** 44</p><p>- **Status:** New Case</p><p>- **Process SLA:** -</p><p>- **Case Disabled:** false</p><p>---</p><p>### Source &amp; Description</p><p>- **Source:** -</p><p>- **Description:** -</p><p>---</p><p>### Timestamps</p><p>- **Case Created At:** 2026-01-15T11:55:40.868Z</p><p>- **Last Updated At:** 2026-01-15T11:56:52.903Z</p><p>- **Case Last Updated At:** 2026-01-15T11:56:52.778Z</p><p>---</p><p>### Case Data Information</p><p>- **Case Data ID:** 4380</p><p>- **Case Data Created At:** 2026-01-15T11:55:40.868Z</p><p>- **Case Data Updated At:** 2026-01-15T11:55:40.868Z</p><p></p><p>✅ **This case is active and in progress.**</p><p></p><p></p>",
        "name": "",
        "email": "",
        "details": "2026-01-15T11:55:40.868Z",
        "disabled": false,
        "createdAt": "2026-01-15T18:59:04.096Z",
        "createdBy": "testingserviceaccount@neutrinos.co",
        "updatedAt": "2026-01-15 19:35:49.155788+00"
    }
}
```

Note

: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.

## Generate PDF

To generate the PDF using the data fetched for a specific CID, follow the steps below:

In the Swagger file downloaded from the platform, provide the required details in the JSON payload to generate a PDF using data fetched for a specific CID. The following JSON example illustrates a sample payload with CID 4380.

```json
{
  "schemaName": "test handlebars",
  "version": "1.0.0",
  "recordId": "b4743762-706a-4964-8136-c00003f75142",
  "cid": 4380,
  "pdfTemplateKey": "info"
}
```

- **schemaName**: Specifies the name of the schema created on the platform.
- **version**: Specifies the version of the schema used to generate the HTML template.
- **recordId**: Specifies the record from which data is fetched and added to the HTML template.
- **cid**: Specifies the case ID for which an HTML template is generated.
- **pdfTemplateKey**: Specifies the key in the template from which data is fetched to generate the PDF.

Case details are fetched and passed to the API to generate a PDF based on the markdown defined on the platform. A sample markdown is illustrated below:

```markdown
## Case Summary

### Case Details

- **Case ID (CID):** {{cid}}

- **Process Instance ID (PIID):** {{piid}}

- **Case Definition ID (CDID):** {{cdid}}

- **Status:** {{status}}

- **Process SLA:** {{processSLA}}

- **Case Disabled:** {{caseDisabled}}

---

### Source & Description

- **Source:** {{source}}

- **Description:** {{description}}

---

### Timestamps

- **Case Created At:** {{created_at}}

- **Last Updated At:** {{updated_at}}

- **Case Last Updated At:** {{case_last_updated_at}}

---

### Case Data Information

- **Case Data ID:** {{caseData.cidid}}

- **Case Data Created At:** {{caseData.created_at}}

- **Case Data Updated At:** {{caseData.updated_at}}

{{#if caseDisabled}}

⚠️ **This case is currently disabled.**

{{else}}

✅ **This case is active and in progress.**

{{/if}}
```

**Note**: The values for these fields are retrieved from the case details. Sample case data is illustrated below.

```json
{
  "cid": 4380,
  "piid": 4571,
  "source": "-",
  "description": "-",
  "created_at": "2026-01-15T11:55:40.868Z",
  "updated_at": "2026-01-15T11:56:52.903Z",
  "case_last_updated_at": "2026-01-15T11:56:52.778Z",
  "status": "New Case",
  "cdid": 44,
  "processSLA": "-",
  "caseDisabled": false,
  "caseData": {
    "cidid": 4380,
    "data": {},
    "created_at": "2026-01-15T11:55:40.868Z",
    "updated_at": "2026-01-15T11:55:40.868Z"
  }
}
```

Upon successful execution of the JSON payload, the API returns an output containing the PDF generated from the template. In this example, the PDF includes case-related information such as the CID, PID, case creation date and time, and other relevant fields. The sample output is illustrated below:

Note

: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.

## Handlebars By Data

To create Handlebars templates by passing data, follow these steps:

In the Swagger file downloaded from the platform, provide the required details in the JSON payload to generate a Handlebars template using the data passed in the payload. The following JSON example illustrates a sample request.

```json
{
    "schemaName": "test handlebars",
    "version": "1.0.0",
    "recordId": "4f4d878b-f480-45af-a327-cc6e8aff1ca8",
    "data": {
        "user": {
            "age": 29,
            "fullname": "Neha Sharma",
            "verified": false,
            "joined_date": "2022-08-14",
            "languages": [
                "English",
                "Hindi",
                "Spanish"
            ],
            "address": {
                "street": "221B Baker Street",
                "city": "Mumbai",
                "state": "Maharashtra",
                "country": "India",
                "zip": "400001"
            },
            "contact": {
                "email": "neha.sharma@example.com",
                "phone": "+91-**********"
            },
            "subscriptions": [
                {
                    "plan": "Gold",
                    "status": "Active",
                    "renewal_date": "2024-08-14"
                },
                {
                    "plan": "Premium Support",
                    "status": "Inactive",
                    "renewal_date": "2023-12-01"
                }
            ]
        }
    },
    "templateKey": ["info","name"]
}
```

- **schemaName**: Specifies the name of the schema created on the platform.
- **version**: Specifies the version of the schema used to generate the HTML template.
- **recordId**: Specifies the record from which data is fetched and added to the HTML template.
- **data**: Specifies the required data to be passed to the template defined in the platform markdown.

Note

: The JSON used in this example is based on the markdown specified.

Upon successful execution of the JSON payload, the API returns a response containing the details defined in the template, populated with the data passed in the request. In this example, the response renders the data from the JSON payload into the defined HTML template. The sample output is illustrated below.

```json
{
    "success": true,
    "message": "Content created for schema = test handlebars, recordId = 4f4d878b-f480-45af-a327-cc6e8aff1ca8 successfully.",
    "data": {
        "info": "<h2>Hello Neha Sharma,</h2><p>Welcome to our platform! Here's your account overview:</p><hr><h3>Location</h3><p>221B Baker Street, Mumbai, Maharashtra, India - 400001</p><h3>Contact Info</h3><ul><li><p><strong>Email:</strong> neha.sharma@example.com</p></li><li><p><strong>Phone:</strong> +91-**********</p></li></ul><h3>Languages</h3><ul><li><p></p></li><li><p>English</p></li><li><p></p></li><li><p>Hindi</p></li><li><p></p></li><li><p>Spanish</p></li><li><p></p></li></ul><h3>Subscription Plans</h3><p></p><p>PlanStatusRenewal</p><p></p><p><span style=\"color: red;\">Your account is not yet verified. Please verify to unlock all features.</span></p><p></p><h3>Joined On</h3><p>2022-08-14</p><hr><p>If you have any questions, feel free to contact our support team.</p><p>Thanks,<br><strong>The Support Team</strong></p>",
        "name": "Neha Sharma"
    }
}
```

Note

: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.

## Generate PDF By Data

To generate the PDF using the data passed in the JSON payload, follow the steps below:

In the Swagger file downloaded from the platform, provide the required details in the JSON payload to generate a PDF using the data passed in the payload. The following JSON example illustrates a sample request.

```json
{
    "schemaName": "test handlebars",
    "version": "1.0.0",
    "recordId": "4f4d878b-f480-45af-a327-cc6e8aff1ca8",
    "data": {
        "user": {
            "age": 29,
            "fullname": "Neha Sharma",
            "verified": false,
            "joined_date": "2022-08-14",
            "languages": [
                "English",
                "Hindi",
                "Spanish"
            ],
            "address": {
                "street": "221B Baker Street",
                "city": "Mumbai",
                "state": "Maharashtra",
                "country": "India",
                "zip": "400001"
            },
            "contact": {
                "email": "neha.sharma@example.com",
                "phone": "+91-9876501234"
            },
            "subscriptions": [
                {
                    "plan": "Gold",
                    "status": "Active",
                    "renewal_date": "2024-08-14"
                },
                {
                    "plan": "Premium Support",
                    "status": "Inactive",
                    "renewal_date": "2023-12-01"
                }
            ]
        }
    },
    "pdfTemplateKey": "info"
}
```

- **schemaName**: Specifies the name of the schema created on the platform.
- **version**: Specifies the version of the schema used to generate the HTML template.
- **recordId**: Specifies the record from which data is fetched and added to the HTML template.
- **data**: Specifies the required data to be passed to the template defined in the platform markdown.

**Note**: The information provided in the data field of the JSON payload is integrated into the markdown defined on the platform. In this example, the sample markdown is illustrated below.

```markdown
Hello {{user.fullname}},

Welcome to our platform! Here's your account overview:

Location

{{user.address.street}}, {{user.address.city}}, {{user.address.state}}, {{user.address.country}} - {{user.address.zip}}

Contact Info

Email: {{user.contact.email}}

Phone: {{user.contact.phone}}

Languages

{{#each user.languages}}

{{this}}

{{/each}}

Subscription Plans

{{#each user.subscriptions}}{{/each}}

PlanStatusRenewal{{plan}}{{status}}{{renewal_date}}

{{#if user.verified}}

Your account is verified.

{{else}}

Your account is not yet verified. Please verify to unlock all features.

{{/if}}

Joined On

{{user.joined_date}}

If you have any questions, feel free to contact our support team.

Thanks,The Support Team
```

Upon successful execution of the JSON payload, the API returns an output containing the PDF generated from the template. The sample output is illustrated below:

Note

: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
