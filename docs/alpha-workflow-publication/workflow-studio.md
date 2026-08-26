# Workflow Studio

<https://documentation.neutrinos.com/articles/#!alpha-workflow-publication/workflow-studio>

## Workflow Studio

The Alpha Workflow Studio lets you automate the enterprise at scale. It breaks down barriers between processes and systems, letting you easily create workflows across the enterprise. Alpha Workflow is a platform capability that lets you automate business processes in a single drag-and-drop design environment.

Alpha Workflow Studio gives you rich capabilities for automating processes to reduce repetitive tasks, allowing you to focus on high value work. Empower business users to automate approvals, tasks and notifications. Alpha Workflow studio has the following components:

- Empowers you to design a robust data model for business workflows, ensuring efficient operations and seamless scalability to meet growing business demands.
- Configure the user experience by setting rules for each task and decision, such as assigning roles and setting deadlines.
- Track the real-time progress of workflows, analyze performance, and identify any bottlenecks.

The first thing you see when you log in to Workflow studio is the Projects page. It provides a centralized location for managing projects, such as creating new ones, searching and deleting projects. This page enables easy access to organizational resources, enabling team members to collaborate and work together seamlessly.

You can also get links to various resources to help you build apps using workflow studio.

![](https://lh7-us.googleusercontent.com/Dv2dQcE9LLELomlWYtS3JMQJ2aRuxnJrIKfuNia53xoe89X8bdkt_RtKLSlY0JhDP7URdII-EJtPMM9SkQgKtm4ICDXeoJuB0sMy6L6mj48xR-nU1vDTGba6n3jxgU0k1o3ALUCzij0rk5MaExQ0eWw)

### Projects

This section displays the projects you have created. You can easily navigate to any of them from here. The capabilities within the projects screen is provided in the below table.

| **Feature** | **Description** |
| --- | --- |
| **Search** | Search for a project using this feature. |
| **Filter** | Use the filter option to view your projects based on Draft and Submitted mode. |
| **Sort** | Use this to arrange projects in a specific order, typically based on criteria such as project name, last updated and status. It allows you to organize data in a structured manner, making it easier to find, analyze, and understand information. |
| **Pagination** | Allows you to navigate through the content in manageable chunks, typically displaying the selected number of items per page. It enhances usability by making large datasets more accessible and improving load times by loading only the selected portion of the content at once. |
| **Show by** | Allows you sort data by rows. Each row typically contains related data or elements, making it easier for users enhancing readability and comprehension. |

### Creating a New Project

You can create a new project. If you choose to create a project from scratch, you can choose from a blank app or upload an existing app to get started.

Refer to the video link provided below to create a new project.

**[Create a New Project](/resources/Storage/alpha-workflow-publication/alpha-workflow-studio%2024.6.0.0.120%20-%20Google%20Chrome%202024-06-06%2017-51-03.mp4)**

### Visual Editor

The Workflow Studio allows you to create and manage schemas in an interactive visual canvas called the Visual Editor. This tutorial covers how to create a schema using the Visual Editor. Use the Visual Editor, to view, design, and manage schemas and related files stored in projects.

#### Schema Definition

A schema refers to a structured format or template used to organize and define the data associated with a case. This schema serves as a blueprint for managing and processing workflows efficiently, ensuring that all necessary information is captured and structured consistently. It helps standardize data collection, storage, and retrieval processes within case management systems.

JSON Schemas provide the following benefits:

- Promote a data-first development approach.
- Before starting to build your application, they specify the structure for your data.
- Enforce consistent data validation from a central location.

How it Works:

The process involves identifying relevant data attributes, and organizing them into a coherent schema to generate objects in your app.

- **Identify Relevant Data Elements**: Determine the data elements that your application utilizes. This could include information like application name, version, description, author, and any other relevant attributes.
- **Validation**: Ensure your schema markup is correctly implemented and follows json schema guidelines. This step helps identify any errors or issues that need to be corrected.

You can utilize it to define the requirements for storing and validating data in an application. The Schemas Viewer displays the JSON schemas added to a workspace, allowing you to manage and publish them.

A sample schema is provided below

```json
{      "$schema": "https://json-schema.org/draft/2020-12/schema",      "title": "Case Definition",      "type": "object",      "properties": {            "documents_list": {                  "type": "array",                  "items": {},                  "default": null            },            "dob": {                  "type": "string"            },            "first_name": {                  "type": "string"            },            "expiry_date": {                  "type": "string"            },            "second_name": {                  "type": "string"            },            "sum_insured": {                  "type": "number"            },            "product_name": {                  "type": "string"            },            "claim_claimId": {                  "type": "string"            },            "policy_number": {                  "type": "string"            },            "policy_status": {                  "type": "string"            },            "inception_date": {                  "type": "string"            },            "claim_claimType": {                  "type": "string"            },            "claim_totalCost": {                  "type": "number"            },            "claim_claimStatus": {                  "type": "string"            },            "claim_patient_name": {                  "type": "string"            },            "claimHistory_status": {                  "type": "string"            },            "claim_provider_name": {                  "type": "string"            },            "claim_services_cost": {                  "type": "number"            },            "claim_services_date": {                  "type": "string"            },            "claimHistory_dateFiled": {                  "type": "string"            },            "claim_patient_patientId": {                  "type": "string"            },            "claim_product_productId": {                  "type": "string"            },            "claimHistory_paymentMode": {                  "type": "string"            },            "claim_services_serviceId": {                  "type": "string"            },            "claim_policy_coverageType": {                  "type": "string"            },            "claim_policy_policyNumber": {                  "type": "string"            },            "claim_provider_providerId": {                  "type": "string"            },            "claimHistory_paymentStatus": {                  "type": "string"            },            "claimHistory_pendingAmount": {                  "type": "number"            },            "claim_policy_policyEndDate": {                  "type": "string"            },            "claim_services_description": {                  "type": "string"            },            "claimHistory_previousClaimId": {                  "type": "string"            },            "claim_policy_policyStartDate": {                  "type": "string"            },            "claim_provider_serviceAddress": {                  "type": "string"            },            "customerInfo_idDetails_idType": {                  "type": "string"            },            "claim_paymentDetails_paidAmount": {                  "type": "number"            },            "customerInfo_idDetails_idNumber": {                  "type": "integer"            },            "claim_paymentDetails_paymentDate": {                  "type": "string"            },            "claim_paymentDetails_paymentMode": {                  "type": "string"            },            "claim_product_productDescription": {                  "type": "string"            },            "claim_paymentDetails_paymentStatus": {                  "type": "string"            },            "claim_paymentDetails_pendingAmount": {                  "type": "number"            },            "claimHistory_policyInfo_policyNumber": {                  "type": "string"            },            "claimHistory_policyInfo_policyStartDate": {                  "type": "string"            },            "customerInfo_contactDetails_phoneNumber": {                  "type": "string"            },            "claimHistory_policyInfo_policyExpiryDate": {                  "type": "string"            },            "claim_amount": {                  "type": "string"            },            "email": {                  "type": "string"            },            "decision": {                  "type": "string"            },            "coveredBenefits": {                  "type": "array",                  "items": {},                  "default": null            },            "notCoveredBenefits": {                  "type": "array",                  "items": {},                  "default": null            },            "disease": {                  "type": "string"            },            "transaction_id": {                  "type": "string"            },            "policy_documents": {                  "type": "object",                  "properties": {}            },            "claim_documents": {                  "type": "object",                  "properties": {}            },            "reason": {                  "type": "string"            },            "claim_provider_contact_number": {                  "type": "string"            },            "claim_provider_tax_identifier": {                  "type": "string"            },            "illness_identified": {                  "type": "string"            },            "icd_code": {                  "type": "string"            },            "pc_code": {                  "type": "string"            },            "treatment_date": {                  "type": "string"            },            "input_text": {                  "type": "object",                  "properties": {}            },            "icd_response": {                  "type": "object",                  "properties": {}            },            "sla": {                  "type": "string"            },            "priority": {                  "type": "string"            },            "gender": {                  "type": "string"            },            "procedure": {                  "type": "string"            },            "identify_submitter": {                  "type": "string"            },            "identify_lob": {                  "type": "string"            },            "hospitalized_90": {                  "type": "string"            },            "hospitalisation_start_date": {                  "type": "string"            },            "hospitalisation_end_date": {                  "type": "string"            }      }}
```

Watch this video to understand more about [Creating a Schema](/resources/Storage/alpha-workflow-publication/VisualStudio.mp4)

Once this is completed, Initialize the project>Process link and create a bpm flow.

![](/resources/Storage/alpha-workflow-publication/workflow-studio/Initialize.png)

The steps are explained within the [Process Chapter](/articles/alpha-workflow-publication/process).
