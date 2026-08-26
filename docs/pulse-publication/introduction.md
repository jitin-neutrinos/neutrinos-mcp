# Architecture

<https://documentation.neutrinos.com/articles/#!pulse-publication/introduction>

The platform supports end-to-end digital transformation by providing capabilities such as workflow automation, dynamic case handling, role-based access control (RBAC), object modeling, business rules management, branching and decision orchestration, master data management, content and media management, and enterprise data integration.

## Architecture

The image below outlines the architectural design of the platform:




 ![architecture-unified-hq](/resources/Storage/pulse-publication/images/architecture-unified-hq.png)

The architecture follows a modular and service-oriented approach, enabling scalability, extensibility, centralized governance, and reusable business services across modules and processes.

## Architectural Layers

### UX Layer (Fusion)

At the top of the architecture is the UX Layer (Fusion), which serves as the presentation and interaction layer of the platform. This layer is responsible for:

- Delivering user-facing interfaces and dashboards
- Providing unified user experiences across modules
- Enabling interaction between end users and backend orchestration services

The UX Layer abstracts underlying orchestration and AI services, allowing users to interact with workflows, cases, agents, and business processes through a centralized interface.

### ORB (Config Orchestrator)

The ORB (Config Orchestrator) layer acts as the configuration and orchestration management layer for platform agents and services. This layer provides centralized orchestration and configuration management for specialized agents operating within the ecosystem.

#### Components within ORB

- **Hypha Agent**: Responsible for interacting with business objects and enterprise data models managed within the Hypha data layer.
- **Decision Agent**: Handles business rule execution, decision orchestration, and rule-driven automation.
- **Workflow Agent**: Manages workflow execution logic, process orchestration, and task routing.
- **HIL Agent**: Supports Human-in-the-Loop interactions, enabling manual intervention, approvals, escalations, and assisted decision-making within automated processes.
- **MS Agent**: Represents microservice orchestration and integration capabilities, enabling external or internal services to participate in workflows.
- **UX Agent**: Coordinates user experience configurations and frontend interaction orchestration.

#### Responsibilities of ORB

The ORB layer enables:

- Centralized configuration management
- Agent orchestration and coordination
- Runtime execution configuration
- Service abstraction and modular extensibility
- Reusable orchestration patterns

This layer acts as the bridge between AI-powered orchestration and operational business execution.

### AI Hub (Powered by Cortex)

The AI Hub, powered by Cortex, provides the artificial intelligence and cognitive capabilities of the platform. This layer enables AI-driven functionalities that enhance automation, intelligence, and decision-making across workflows and business processes. For more information about AI Hub and its capabilities, refer to the [AI Hub](/smart/project-ai-hub/overview) documentation.

### Pulse (Agent Orchestrator)

The Pulse layer functions as the primary runtime orchestration engine responsible for executing business operations and coordinating platform services. This layer acts as the operational backbone of the architecture.

#### Core Modules

- **Decisioning Module**: The Decisioning module is responsible for executing business rules, conditional logic, policy validations, and decision automation during runtime. This module enables processes to dynamically determine execution paths based on business conditions, data values, AI outputs, or external inputs.
    **Responsibilities**
    **Capabilities**: The Decisioning module can:
    **Example Use Cases**
    **Interaction with Other Modules**: The Decisioning module interacts closely with:
  - Rule execution
  - Policy validation
  - Conditional branching
  - Decision table execution
  - Dynamic process routing
  - Eligibility and compliance checks
  - SLA-based decision handling
  - Evaluate business conditions in real time
  - Trigger different execution paths based on outcomes
  - Execute rule groups and decision trees
  - Integrate AI-driven recommendations into decisions
  - Support configurable business logic without code changes
  - Loan approval eligibility checks
  - Insurance claim validation
  - Fraud detection routing
  - SLA escalation decisions
  - Workflow module for conditional routing
  - AI Hub for predictive decisions
  - Case module for exception handling
  - Agents for intelligent automation execution
- **Workflow Module**: The Workflow module is responsible for orchestrating end-to-end business processes and managing the lifecycle of workflow execution. This module controls how tasks, approvals, integrations, and automation activities move across process stages.
    **Responsibilities**
    **Capabilities**: The Workflow module supports:
    **Workflow Lifecycle Stages**: Typical workflow lifecycle stages include:
    **Example Use Cases**
  - Process orchestration
  - Task sequencing
  - State transition management
  - Workflow lifecycle execution
  - Parallel and sequential execution handling
  - Event-triggered workflow execution
  - SLA tracking and escalation
  - Structured workflow automation
  - Dynamic task assignment
  - Multi-stage approval flows
  - Workflow versioning and execution tracking
  - Process initiation
  - Task creation
  - Decision evaluation
  - Agent or service execution
  - Human intervention if required
  - Status tracking
  - Completion or escalation
  - Employee onboarding
  - Procurement approval workflows
  - Incident management processes
  - Customer service request handling
  - Claims processing
- **Agents Module**: The Agents module manages autonomous and semi-autonomous agents that play a vital role in business process execution. Agents represent intelligent operational entities capable of performing tasks, making decisions, invoking services, or coordinating workflow activities.
    **Responsibilities**
    **Capabilities**: The Agents module enables:
    **Example Use Cases**
  - Agent lifecycle management
  - Task delegation
  - Agent communication orchestration
  - Context sharing between agents
  - AI-assisted execution management
  - Autonomous task execution
  - Multi-agent collaboration
  - Intelligent process participation
  - Dynamic orchestration between agents
  - Distributed operational execution
  - AI agent processing customer requests
  - Automated document processing agents
  - Workflow optimization agents
- **HIL (Human-in-the-Loop) Module**: The Human-in-the-Loop (HIL) module enables human participation within automated business operations. This module ensures that processes requiring human judgment, approvals, reviews, or interventions can seamlessly coexist with automated workflows and AI-driven orchestration.
    **Responsibilities**
    **Capabilities**: The HIL module supports:
    **Example Use Cases**
  - Manual approval management
  - Human task assignment
  - Exception handling
  - Escalation management
  - Human review and validation
  - Assisted decision-making
  - User task queues
  - Approval workflows
  - AI-assisted recommendations for users
  - Role-based human interactions
  - Compliance approvals
  - Manual fraud investigations
  - Document verification
  - Exception resolution workflows
- **Case Module**: The Case module provides case management capabilities for handling long-running, stateful, and event-driven business operations. Unlike structured workflows, cases are dynamic and evolve based on events, interactions, and changing business contexts.
    **Responsibilities**
    **Capabilities**: The Case module supports:
    **Example Use Cases**
  - Case lifecycle management
  - Stateful process tracking
  - Event-driven orchestration
  - Multi-activity coordination
  - Case history management
  - Dynamic case progression
  - Ad hoc task creation
  - Multi-channel event handling
  - Persistent contextual data management
  - SLA and milestone tracking
  - Collaborative case resolution
  - Insurance claims
  - Customer dispute management
  - Legal case handling
  - Incident response management
- **MS (Microservices) Module**: The MS module provides microservice orchestration and enterprise integration capabilities. This module enables Pulse to interact with internal services, external systems, APIs, enterprise applications, and distributed service architectures.
    **Responsibilities**
    **Capabilities**
  - Service orchestration
  - API invocation
  - Integration management
  - External system communication
  - Event publishing and consumption
  - Service coordination
  - API integrations
  - Asynchronous messaging
  - Event-driven communication
  - Enterprise system connectivity
  - Distributed execution coordination

### Hypha - Data Layer

At the foundation of the architecture is the Hypha Data Layer, which manages enterprise business objects and shared data models. This layer acts as the centralized data abstraction and persistence layer for the entire platform.

Responsibilities

- Business object management
- Enterprise data modeling
- Centralized data access
- Data persistence and retrieval
- Shared object reuse across workflows and cases
- Data consistency and governance
- Integration with enterprise systems

The Hypha layer ensures that workflows, agents, decisions, and cases operate on a unified and reusable business data model.

[Next Topic](/articles/pulse-publication/navigating-interface)

[Previous](/articles/pulse-publication/overview)
