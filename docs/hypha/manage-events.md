# Purpose

<https://documentation.neutrinos.com/articles/#!hypha/manage-events>

Events are system-triggered notifications that occur when a defined action is performed or when a state change occurs within an object. They enable the system to automatically execute configured logic when specified conditions are met.

Events can be configured to trigger actions under various circumstances, such as when a record is created, a field value is updated, or a record is deleted. These events can then be used to perform actions such as sending email notifications to recipients, creating calendar events, or generating reminders.

## Purpose

- Enable event-driven automation across workflows.
- Integrate with external applications and services.
- Enforce validation, or notification logic.
- Reduce manual intervention by triggering actions automatically.

## Working

Actions associated with an event are triggered when the configured event occurs. Common trigger events include:

- Creating a record
- Updating a record
- Deleting a record

Configuration

Events are typically defined and managed at the object level and include:

- Trigger action that initiates the event.
- Defines the action to be executed when an event occurs. The execution of the action depends on the timing at which it is triggered. The supported timing sequences are BEFORE, ON_SUCCESS (AFTER), and ON_FAILURE.

## Example Scenario

Consider an insurance organization that uses Hypha to manage claim data. Multiple downstream systems—such as fraud detection, policy administration, and payment systems—must be notified when a claim reaches specific milestones.

### Example: Claim Status Update

#### Event: Claim Status Changed

Trigger Condition: When claim status transitions from “Under Review” to “Approved”.

#### Execution Flow

1. A **Claims Adjuster** updates the claim status to Approved.
2. This update made by the **Claims Adjuster** triggers the Update event.
3. The configured event is evaluated, and conditions are met.
4. The event invokes the Payment Processing Service via respective API calls.
5. The payment system initiates disbursement.
6. Execution details (success/failure, response time) are logged in the audit trail.
