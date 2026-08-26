# Points to Remember

<https://documentation.neutrinos.com/articles/#!pulse-publication/onboard-process-and-case-wf-cm>

## Points to Remember

1. Every **Case Instance** must be linked to a corresponding **Process Instance**, identified by its **Process Instance ID (piid)**. This linkage must be updated whenever the version of the associated **Process Definition** changes.
2. To onboard a **Process Definition** into the **Case Manager**, the **BPM Service** is required to provide the relevant deployment details. Similarly, onboarding a **Case Type** into the **Case Manager** requires an explicit association with an existing **Process Definition**.
3. All **Case Instances** in the **Case Manager** are created based on a specific **Case Type** and remain tightly coupled with it throughout their lifecycle.
4. Processes can be versioned. The new version must be mapped to the corresponding Case instance whenever a process version changes. Versioning is performed by navigating to **Space** > **Project** > **General Settings** > **Version**. This setting determines the version used for the build and deployment.
    ![Warning](/resources/Storage/pulse-publication/warning.png)
    Versioning a process before migrating between environments is considered best practice. This ensures that existing processes with active instances continue to function without issues. Failing to do so may result in system disruptions.

The overview of events involved in onboarding a process and case is illustrated by the sequence image below:

![processCaseOnboarding](/resources/Storage/pulse-publication/images/processCaseOnboarding.jpg)

Onboarding a case is a crucial step. Follow the below steps to onboard a process:

## Create Process

1. **Create a BPM Workflow**: Use the **BPM Designer** to create a business workflow tailored to the specific requirements. Ensure all tasks, rules, and decision points are configured to align with the defined needs.
    ![jbpm-process](/resources/Storage/pulse-publication/images/jBPM%20process.png)
2. **Save and Deploy the Workflow**: After designing the workflow, save and deploy the process to make it executable.
    ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
    Navigate to the execution servers to verify that the workflow has been deployed successfully.
    ![execution-server](/resources/Storage/pulse-publication/images/Execution%20servers.png)
3. **Retrieve Deployment Details**:
  1. Access process definitions: In **Neutrinos BPM**, navigate to **Menu** > **Manage** > **Process Definitions** to access and manage process definitions.
      ![menu-process-definition](/resources/Storage/pulse-publication/images/menu-process-definition.png)
  2. Select the required process to invoke when the **Create Case API** is called. This metadata is critical during the process onboarding in the Case Manager.
      ![process-definition-list-page](/resources/Storage/pulse-publication/images/process-definition-list-page.png)
  3. Locate the recently deployed process flow and verify the process definition name:
      ![process-detail-info-page](/resources/Storage/pulse-publication/images/process-detail-info-page.png)
  4. Note the Identifiers - The Definition ID and Deployment details are required to invoke the Case Service:
      ![](/resources/Storage/pulse-publication/images/process-detail-info-page%20-%202.png)
      ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
      Replace the <processDefinitionID> and <containerID> with the specific values. The deployment is represented as containerId, while the process definition is referred to processDefinitionId.
  5. In Swagger, under **Process Definition**, find **Fetch All Process Definition** API. This API retrieves all the processes deployed within a BPM container, identified by the containerId. The Header and Body follow the below format:
      **Headers**:
      **Field**
      **Value**
      Authorization (required)
      <IDS TOKEN>
      Content-Type (required)
      application/json
      accept (required)
      application/json
      **Body**:
      **Field**
      **Type**
      **Description**
      options.pageSize
      Number (required)
      Size of the returned page list.
      options.page
      Number (required)
      Page number to be fetched.
      metadata.containerId
      string (required)
      Container ID of the Process Definition.
      The curl below illustrates a sample section for process definition:
      Copy CodeBash (Unix Shell)curl -X 'POST' \n'https://<ALPHA_DEPLOYMENT_DOMAIN>/bpmservice/process/definition/fetch-all' \
     -H 'accept: application/json' \
     -H 'Authorization: Bearer <IDS_TOKEN>' \n-H 'Content-Type: application/json' \
     -d '{
     "options": {
     "pageSize": 10,
     "page": 0
     },
     "metadata": {
     "containerId": "HNI_1.0.0-SNAPSHOT"
     }
     }'
      On successful execution of the above curl, it returns a response as illustrated below:
      Copy CodeJavaScript{
      "processName": "Registration Review",
      "processVersion": "1.0",
      "processDefinitionId": "create-case.RegistrationReview",
      "metadata": {
      "containerId": "create-case_1.0.0-SNAPSHOT",
      "variables": null,
      "reusableSubProcesses": null,
      "nodes": null,
      "timers": null,
      "tagsByVariable": null,
      "package": "com.myspace.create_case",
      "dynamic": false
      },
      "taskDefinitions": [
      {
      "taskName": "Registration",
      "taskType": "Human Task",
      "metadata": {
      "owner": ["High"]
      }
      }
      ]
     }
  6. Navigate to the Create Process Definition API EndPoint - **POST /caseservice/process/definition/create** to create Process Definitions. The Headers and Body details for the API are described in the below format:
      **Header**:
      **Field**
      **Description**
      Authorization (required)
      The authentication token to authorize the request.
      For example: Bearer < IDS_TOKEN >
      Content-Type (required)
      Specifies the media type of the resource in the request body.
      Value: application/json.
      accept (required)
      Indicates that the client expects JSON data in response.
      Value: application/json.
      **Request Body**:
      **Field**
      **Type**
      **Required**
      **Description**
      processName
      string
      true
      Name for the process definition.
      processVersion
      string
      true
      Version label or number for the process definition.
      processDefinitionId
      string
      true
      Unique ID referencing this specific process definition.
      metadata
      object
      true
      Metadata information of extra context about the process definition.
      process SLA
      string
      optional
      Any SLA or time-bound definition for the process (For example: "2 days").
      mainProcess
      boolean
      true
      Flag to indicate if this definition is the main/primary process.
      taskDefinitions
      array
      true
      An array of task definition object (discussed below).
      Within the **taskDefinitions**, each task object has the following details:
      **Field**
      **Type**
      **Required**
      **Description**
      taskName
      string
      true
      Name/identifier for the task.
      taskType
      string
      true
      Category or type of the task (For example: "Human Task", "automated", etc.,).
      inputSchema
      object
      true
      JSON schema or object representing the input data for the task.
      outputSchema
      object
      true
      JSON schema or object representing the output data for the task.
      displayText
      string
      true
      A human-readable text displayed in UI for the task.
      taskSLA
      string
      optional
      SLA or time-based requirement for this task (For example: "4 hours").
      taskIcon
      string
      optional
      A path or identifier for an icon representing the task visually.
      The curl below illustrates a sample section for process creation.
      Copy CodeBash (Unix Shell)curl --location '<DOMAIN>/caseservice/process/definition/create' \n--header 'accept: application/json' \n--header 'Content-Type: application/json' \n--data '{
      "processName": "string",
      "processVersion": "string",
      "processDefinitionId": "string",
      "metadata": {},
      "processSLA": "string",
      "mainProcess": true,
      "taskDefinitions": [
      {
      "taskName": "string",
      "taskType": "string",
      "inputSchema": {},
      "outputSchema": {},
      "displayText": "string",
      "taskSLA": "string",
      "taskIcon": "string"
      }
      ]
     }'
      On successful execution of the above curl, it returns a Case Instance reference to the onboarded Process Definition ID (pdid). If the pdid corresponds to a main process, use it to establish the link with the Case Definition (case type).
      Additionally, if the designed business workflow includes sub-processes, follow the steps outlined in the previous sections to obtain the PDIDs of each sub-process. Pass these pdid’s to the sub-process array when creating cases for the workflow.
      ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
      A Sub-Process is a smaller process embedded within a larger workflow. It simplifies complex workflows by breaking them into manageable sections, making the design process more efficient and maintainable

## Onboard Case

To onboard a case, follow the steps below:

1. In Swagger, navigate to the API Endpoint - **POST ${DOMAIN}/caseservice/case/definition/create**. Use the below curl. Pass the appropriate values to the fields: caseSchema, pdid, sub-process pdid’s (if workflow contains a sub-process), caseType, and the version to create a case definition:
    Copy CodeBash (Unix Shell)curl -X 'POST' \n '<DOMAIN>/caseservice/case/definition/create' \n -H 'accept: application/json' \n -H 'Content-Type: application/json' \n -d '{
    "caseDefinitionSchema": {
    "caseSchema": {},
    "pdid": 0,
    "subProccess": [
    0
    ],
    "active": true
    },
    "caseType": "string",
    "version": "string"
   }'
    Note: caseSchema is an optional JSON schema model that is stored for the project. Also, multiple projects can be associated with a single case, this schema can serve as a reference.
2. Upon successful execution of the curl request, a cdid (Case Definition ID) is generated, representing the created case definition.
3. To verify the successful creation of a case definition, create cases using the specified caseType in the previous curl request. Use the following API endpoint -** POST ${DOMAIN}/caseservice/case/instance/create**.
    Copy CodeBash (Unix Shell)curl -X 'POST' \n'<DOMAIN>/caseservice/case/instance/create' \n -H 'accept: application/json' \n -H 'Content-Type: application/json' \n -d '{
    "caseType": "string",
    "caseData": {},
    "wfData": {}
   }'
