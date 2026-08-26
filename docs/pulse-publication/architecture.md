# Core Architectural Principles

<https://documentation.neutrinos.com/articles/#!pulse-publication/architecture>

Process Management has a distributed, event-driven workflow orchestration designed to execute long-running, asynchronous business processes. The architecture follows a microservices plus message queue pattern, enabling scalability, fault tolerance, and clear separation of concerns.




 ![pulse-architecture](/resources/Storage/pulse-publication/images/Pulse%20Architecture.jpg)

## Core Architectural Principles

- **Event-driven orchestration**: Workflow progression is driven by events (task completed, timer triggered, user action).
- **Asynchronous execution**: Services communicate through messages instead of direct calls.
- **Horizontal scalability**: Stateless or minimally stateful services backed by shared infrastructure (DB, cache, queue).

## Components

1. **Thor Process Engine (Workflow Orchestrator)**: Controls workflow state and decision-making.
    **Responsibility**:
    **Behavior**:
    **Purpose**:
  - Brain of the workflow system.
  - Maintains workflow definitions, execution state, and transitions.
  - Determines the next step to execute based on process logic.
  - Publishes `process.step.execute` or `task.execute` messages to the Message Queue.
  - Waits for completion or resolution events before advancing the workflow.
  - Handles gateways (conditional branching, parallel paths).
  - Separates process logic from execution logic.
  - Enables deterministic workflow progression even in the face of failures.
2. **Core Service Task Executor (Automated Task Execution)**: Execution, scheduling, human interaction, and auditing are handled by specialized services.
    **Responsibility**:
    **Behaviors**:
  - Executes system-level tasks, such as:
    - API calls
    - Script execution
    - Timers
    - Gateway evaluations
  - Subscribes to execution messages from the queue
  - Performs the assigned step
  - Publish outcome events:
    - `task.completed`
    - `task.failed`
    - `gateway.resolved`
  - Uses cache for transient execution data.
  - Reports only outcomes, not decisions (decisions remain with Thor).
3. **Scheduler Service (Time-based Triggers)**:
    **Responsibility**:
    **Behaviors**:
  - Manages time-driven workflow events
  - Supports:
    - One-time triggers
    - Recurring schedules
  - Tracks timers and schedules
  - When a timer expires, throws a `process.trigger` event
  - Enables delayed or recurring workflow continuation
4. **Hulk Task Service (Human Task Management)**:
    **Responsibility**:
    **Behaviors**:
  - Manages human-in-the-loop interactions
  - Handles:
    - Task assignment
    - User actions (approve, reject, complete)
    - Outcome submission back to the workflow
  - Consumes `usertask.create` events
  - Throws `usertask.update` events upon user action
  - Integrates with UI or external identity systems
  - Clean separation between automated execution and human workflows
  - Supports SLA tracking and task reassignment independently
5. **Audit Services (Observability & Compliance)**:
    **Responsibility**:
    **Captured Data**:
    **Behaviors**:
  - Provides immutable audit trails for workflow execution
  - Who performed an action
  - What action was performed
  - When it occurred
  - Snapshot of relevant state
  - Subscribes to audit-related events from the queue
  - Persists searchable audit logs in Pulse DB
  - Ensures auditing does not impact execution latency
  - Guarantees audit completeness even under partial failures
6. **Message Queue (Integration Backbone)**:
    **Responsibility**:
    **Purpose**:
    **Events**:
  - Serves as the central communication layer between all services
  - Decouples producers and consumers
  - Enables retry, buffering, and fault isolation
  - Allows services to scale independently
  - Execution requests
  - Completion/failure notifications
  - User task events
  - Timer triggers
  - Audit events
7. **Design Studio**:
    **Responsibility**:
    **Characteristics**:
  - Designing workflows
  - Starting process instances
  - Visualizing execution state
  - Interacts with backend services via APIs
  - Relies on backend persistence and audit logs for visualization
8. **Data & State Management**:
  - **Pulse DB**:
    - Used by each service for its own persistence needs
    - Avoids shared mutable state across services
  - **Cache**: Used for performance optimization and transient execution data

## Summary

To summarize, Process Management is an event-driven, microservices-based workflow orchestration designed to execute long-running and asynchronous business processes. The Thor Process Engine acts as the central orchestrator, controlling workflow state, sequencing, and decision-making, while specialized services handle automated task execution, time-based triggers, human tasks, and auditing. All inter-service communication occurs asynchronously through a message queue, enabling loose coupling, fault tolerance, and independent scaling. Each service persists its own state in Pulse DB and uses caching where required, while the Design Studio provides a stateless front-end for designing, starting, and visualizing workflow executions.
