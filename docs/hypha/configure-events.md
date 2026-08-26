# Object Triggers

<https://documentation.neutrinos.com/articles/#!hypha/configure-events>

To add an event in the platform, follow the steps below:

1. From the selected object, navigate to the left navigation panel and click Events to open the Events page.
    ![hypha-studio-events-page](/resources/Storage/hypha/images/hypha-studio-events-page.png)
2. Events can be configured for an object under four circumstances in the platform:
    For each of these operations, the event can be configured to trigger either before or after the action is executed as illustrated in the image below:
    ![hypha-studio-events-page-event-timing](/resources/Storage/hypha/images/hypha-studio-events-page-event-timing.png)
  - When a record is created
  - When a record is saved
  - When a record is updated
  - When a record is deleted
3. After selecting when the event should be triggered, configure the component to be executed. The following component types are supported:
    ![hypha-studio-events-page-event-type](/resources/Storage/hypha/images/hypha-studio-events-page-event-type.png)
  - API Request
  - Case Service
  - REELS
4. After configuring the event as required, click Save at the bottom of the page to persist the changes.

## Object Triggers

When an event is configured through the UI, the corresponding object triggers are executed automatically. Triggers can be configured in two ways: Immediate triggers and Scheduled triggers. Immediate triggers are executed instantly when the associated event occurs, whereas scheduled triggers are executed according to a defined cron schedule.

### Immediate Trigger

Immediate triggers can be configured in the platform when creating an event. Follow the steps below:

1. In Swagger, specify the required JSON payload to create a trigger. A sample JSON payload is illustrated below.
    Copy CodeJSONcurl --location 'http:****/hook-orchestrator/hooks' \n--header 'Content-Type: application/json' \n--header 'Authorization: Bearer ****' \n--header 'X-Organization-Id: ****' \n--data-raw '{
    "name": "Notify on Product Create (Immediate)",
    "schema_name": "seq_test_1",
    "entity_name": "product",
    "trigger_event": "CREATE",
    "trigger_timing": [
    "ON_SUCCESS"
    ],
    "status": "ACTIVE",
    "awaits_response": false,
    "execution_order": 1,
    "actions": [
    {
    "action_type": "SEND_TEAMS_NOTIFICATION",
    "execution_order": 1,
    "configuration": {
    "webhook_url": "https://****/webhookb2/****",
    "message_template": {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "0076D7",
    "summary": "Lead Updated: {{ after.first_name }}",
    "sections": [
    {
    "activityTitle": "Lead '\''{{ after.first_name }}'\'' was created",
    "activitySubtitle": "Lead ID: {{ after._id }}",
    "facts": [
    {
    "name": "Email",
    "value": "{{ after.email }}"
    }
    ],
    "markdown": true
    }
    ]
    }
    }
    }
    ],
    "schedule": null
   }'
  - **name**: Specifies the unique, human-readable name of the trigger being created. In this example, the value is set to *On Lead Email Update*.
  - **schema_name**: Specifies the logical schema in which the trigger is registered. In this example, the schema name is '*lms'*.
  - **entity_name**: Specifies the entity being observed. In this example, the trigger is activated for events on the ‘*contact*’ entity.
  - **trigger_event**: Defines the entity lifecycle events that activate the trigger, including create, update, and delete events for the ‘*contact*’ entity.
  - **trigger_timing**: Defines when the trigger executes relative to the core operation. The trigger can be configured to execute **BEFORE **the operation, **ON_SUCCESS **after a successful operation, or **ON_FAILURE **when an operation fails.
  - **status**: Enables or disables the triggers. When set to **true**, the trigger is active; otherwise, it is inactive.
  - **awaits_response**: Controls synchronous versus asynchronous execution. When set to **true**, the trigger waits for the action response before continuing. When set to **false**, the trigger executes asynchronously in a fire-and-forget (non-blocking) mode.
  - **execution_order**: Defines the execution priority relative to other triggers for the same event. Triggers with lower numeric values are executed first.
  - **actions**: Defines one or more actions to execute when the trigger is activated.
  - **action_type**: Specifies the supported action types for the trigger. Supported values include **HTTP_REQUEST**, **SEND_TEAMS_NOTIFICATION**, **SEND_SLACK_MESSAGE**, **SEND_EMAIL**, **CALENDAR_ITEM_CREATE**, and **EVALUATE_EXPRESSION**.
  - **Configuration**: Defines the runtime settings for the selected action(s).
    - HTTP Request Configuration: Endpoint and HTTP method for the outbound request.
    - Headers: Custom HTTP headers included in the request.
    - Body: Payload sent to the endpoint. Typically includes dynamic data from the triggering event.
    - Authentication: Defines authentication strategy (e.g., OAuth2, API Key).
  - **Success Conditions**: Defines rules to determine whether the action is considered successful.
  - **Action Execution Order**: Defines the sequencing when multiple actions exist within the same trigger.
  - **Scheduling Configuration**: Defines when the trigger is allowed or scheduled to run.
2. Upon successful execution of the above JSON payload, a trigger is created based on the configuration criteria specified in the payload. The sample response is illustrated below:
    Copy CodeJSON{
    "status": "ACTIVE",
    "name": "Notify on Product Create (Immediate)",
    "tenant_id": "****",
    "schema_name": "seq_test_1",
    "schema_id": "****",
    "entity_name": "product",
    "entity_id": "****",
    "trigger_event": "CREATE",
    "trigger_timing": [
    "ON_SUCCESS"
    ],
    "execution_order": 1,
    "awaits_response": false,
    "schedule": null,
    "actions": [
    {
    "action_type": "SEND_TEAMS_NOTIFICATION",
    "configuration": {
    "webhook_url": "https://****/webhookb2/****",
    "message_template": {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "0076D7",
    "summary": "Lead Updated: {{ after.first_name }}",
    "sections": [
    {
    "activityTitle": "Lead '{{ after.first_name }}' was created",
    "activitySubtitle": "Lead ID: {{ after._id }}",
    "facts": [
    {
    "name": "Email",
    "value": "{{ after.email }}"
    }
    ],
    "markdown": true
    }
    ]
    }
    },
    "execution_order": 1,
    "_id": "****",
    "created_at": "2026-01-21T14:39:09.025Z",
    "updated_at": "2026-01-21T14:39:09.025Z"
    }
    ],
    "createdBy": null,
    "updatedBy": null,
    "_id": "****",
    "createdAt": "2026-01-21T14:39:09.025Z",
    "updatedAt": "2026-01-21T14:39:09.025Z"
   }

### Create a Trigger with CRON

To create a trigger with a cron schedule, follow the steps outlined below.

1. In Swagger, specify the required JSON payload to create a trigger. A sample JSON payload is illustrated below.
    Copy CodeJSONcurl --location 'http://****/hook-orchestrator/hooks' \n--header 'Content-Type: application/json' \n--header 'Authorization: Bearer ****' \n--header 'X-Organization-Id: ****' \n--data-raw '{
    "name": "Notify on Product Create (Cron)",
    "schema_name": "seq_test_1",
    "entity_name": "product",
    "trigger_event": "CREATE",
    "trigger_timing": [
    "ON_SUCCESS"
    ],
    "status": "ACTIVE",
    "awaits_response": false,
    "execution_order": 1,
    "actions": [
    {
    "action_type": "SEND_TEAMS_NOTIFICATION",
    "execution_order": 1,
    "configuration": {
    "webhook_url": "https://****/webhookb2/****",
    "message_template": {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "0076D7",
    "summary": "Lead Updated: {{ after.first_name }}",
    "sections": [
    {
    "activityTitle": "Lead '\''{{ after.first_name }}'\'' was created",
    "activitySubtitle": "Lead ID: {{ after._id }}",
    "facts": [
    {
    "name": "Email",
    "value": "{{ after.email }}"
    }
    ],
    "markdown": true
    }
    ]
    }
    }
    }
    ],
    "schedule": {
    "type": "cron",
    "expression": "*/15 * * * * *"
    }
   }'
    **Note**: The JSON attributes and their corresponding values remain consistent with those used for creating an immediate trigger. The key distinction lies in the scheduling configuration: the trigger is defined with the schedule type set to **cron**, along with a specified cron expression that determines its execution schedule.
2. Upon successful execution of the JSON payload, a trigger is created according to the configuration criteria specified in the payload and the defined cron expression. A sample response is illustrated below.
    Copy CodeJSON{
    "status": "ACTIVE",
    "name": "Notify on Product Create (Cron)",
    "tenant_id": "****",
    "schema_name": "seq_test_1",
    "schema_id": "****",
    "entity_name": "product",
    "entity_id": "****",
    "trigger_event": "CREATE",
    "trigger_timing": [
    "ON_SUCCESS"
    ],
    "execution_order": 1,
    "awaits_response": false,
    "schedule": {
    "type": "cron",
    "expression": "*/15 * * * * *"
    },
    "actions": [
    {
    "action_type": "SEND_TEAMS_NOTIFICATION",
    "configuration": {
    "webhook_url": "https://****/webhookb2/****",
    "message_template": {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "0076D7",
    "summary": "Lead Updated: {{ after.first_name }}",
    "sections": [
    {
    "activityTitle": "Lead '{{ after.first_name }}' was created",
    "activitySubtitle": "Lead ID: {{ after._id }}",
    "facts": [
    {
    "name": "Email",
    "value": "{{ after.email }}"
    }
    ],
    "markdown": true
    }
    ]
    }
    },
    "execution_order": 1,
    "_id": "****",
    "created_at": "2026-01-21T14:41:29.660Z",
    "updated_at": "2026-01-21T14:41:29.660Z"
    }
    ],
    "createdBy": null,
    "updatedBy": null,
    "_id": "****",
    "createdAt": "2026-01-21T14:41:29.660Z",
    "updatedAt": "2026-01-21T14:41:29.660Z"
   }

The table below further summarizes the triggers that can be created for each scheduling type.

| **Type** | **JSON Snippet** |
| --- | --- |
| Immediate | "schedule": null |
| Cron | "schedule": {      "type": "cron",      "expression": "*/15 * * * * *"      } |
| Relative Schedule | "schedule": {      "type": "relative",      "sourceField": "expiry_date",      "offsets": [      {      "unit": "seconds",      "value": 15      }      ]      } |
| Relative and Repeatetive Schedule | "schedule": {      "type": "relative",      "sourceField": "expiry_date",      "offsets": [      {      "unit": "seconds",      "value": 15,      "repeatUnit": "seconds",      "repeatInterval": 15      }      ]      } |

### Update Triggers

To update triggers, follow the steps:

1. In the swagger, specify the required JSON payload to create a trigger. A sample JSON payload is illustrated below.
   Copy CodeJSONcurl --location 'http:****/hook-orchestrator/hooks' \n--header 'Content-Type: application/json' \n--header 'Authorization: Bearer ****' \n--header 'X-Organization-Id: ****' \n--data-raw '{
    "name": "Notify on Product Create (Immediate)",
    "schema_name": "seq_test_1",
    "entity_name": "product",
    "trigger_event": "CREATE",
    "trigger_timing": [
    "ON_SUCCESS"
    ],
    "status": "ACTIVE",
    "awaits_response": false,
    "execution_order": 1,
    "actions": [
    {
    "action_type": "SEND_TEAMS_NOTIFICATION",
    "execution_order": 1,
    "configuration": {
    "webhook_url": "https://****/webhookb2/****",
    "message_template": {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "0076D7",
    "summary": "Lead Updated: {{ after.first_name }}",
    "sections": [
    {
    "activityTitle": "Lead '\''{{ after.first_name }}'\'' was created",
    "activitySubtitle": "Lead ID: {{ after._id }}",
    "facts": [
    {
    "name": "Email",
    "value": "{{ after.email }}"
    }
    ],
    "markdown": true
    }
    ]
    }
    }
    }
    ],
    "schedule": null
   }'
  - **name**: Specifies the unique, human-readable name of the trigger being updated. In this example, the value is set to ‘*On Lead Email Update*’
  - **schema_name**: Specifies the logical schema in which the trigger is registered. In this example, the schema name is ‘*lms*’
  - **entity_name**: Defines the entity being observed. In this example, the trigger is activated when events occur on the ‘*contact*’ entity.
  - **property_id**: Indicates the specific field being monitored within the entity. In this example, the trigger is scoped to changes in the ‘*email*’ field of the ‘*contact*’ entity.
  - **trigger_event**: Specifies the entity lifecycle events that activate the trigger. The trigger is activated when a *‘contact’* is created, updated, or deleted.
  - **trigger_timing**: Defines when the hook executes relative to the core operation. The triggers can be configured to execute **BEFORE** the operation, **ON_SUCCESS** after a successful operation, or **ON_FAILURE** when an operation fails.
  - **is_active**: Enables or disables the trigger. When set to **true**, the trigger is active; otherwise, it remains inactive.
  - **awaits_response**: Controls whether the trigger executes synchronously or asynchronously. When set to **true**, the trigger waits for the action response before continuing. When set to **false**, it executes asynchronously in a fire-and-forget (non-blocking) mode.”
  - **execution_order**: Specifies the execution priority among triggers for the same event. Lower numeric values indicate higher priority and are executed first.
  - **actions**: Defines one or more actions to execute when the trigger is activated.
  - **action_type**: Specifies the supported action types for the trigger. Supported values include **HTTP_REQUEST**, **SEND_TEAMS_NOTIFICATION**, **SEND_SLACK_MESSAGE**, **SEND_EMAIL**, **CALENDAR_ITEM_CREATE**, and **EVALUATE_EXPRESSION**.
    - HTTP Request Configuration: Endpoint and HTTP method for the outbound request.
    - Headers: Custom HTTP headers included in the request.
    - Body: Payload sent to the endpoint. Typically includes dynamic data from the triggering event.
    - Authentication: Defines authentication strategy (e.g., OAuth2, API Key).
  - **Success Conditions**: Defines rules to determine whether the action is considered successful.
  - **Action Execution Order**: Defines the sequencing when multiple actions exist within the same hook.
  - **Scheduling Configuration**: Defines when the hook is allowed to run or scheduled.
2. Upon successful execution of the **Update Trigger** API, the specified trigger is updated with the values provided in the request payload.

### Delete Triggers

Triggers that are no longer required can be removed from the platform. Follow the steps below to delete a trigger.

1. In Swagger, specify the required parameters to delete triggers that are available or have been created on the platform. The sample fields for which values must be provided are listed below.
   ![data-fabric-hooks-delete-hook](/resources/Storage/hypha/images/data-fabric-hooks-delete-hook.png)
  - **x-organization-id**: Specifies the id of the Organization.
  - **id**: Specifies the UUID of the hook. The trigger matching this ID is deleted based on the value provided in Swagger.
2. Upon successful execution of the API, the trigger matching the specified UUID is deleted from the platform. A sample response for a successful deletion is shown below.
   Copy CodeJSONresponse: NA
   Status 204
