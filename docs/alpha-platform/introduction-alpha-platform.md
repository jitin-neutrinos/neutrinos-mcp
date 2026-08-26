# Architecture

<https://documentation.neutrinos.com/articles/#!alpha-platform/introduction-alpha-platform>

In evolving landscape of digital transformation, efficiency and adaptability are critical to enterprise success. The **Neutrinos Alpha Platform
 serves as comprehensive ecosystem that empowers organizations to develop scalable solutions, enhancing operational efficiency and driving business growth.
 **

With its advanced hyper-automation deployment capabilities, **Neutrinos Alpha Workflow** redefines Business Process Management (BPM) by enabling organizations to design,
 automate, and optimize business operations with precision and effectiveness.

This documentation provides a comprehensive guide to the powerful features of the Neutrinos Alpha Platform, helping you build, customize, and deploy workflows that adapt to your business needs.

## Architecture

The image below outlines the Architectural design of Neutrinos Alpha Platform.

![Architecture of Alpha](/resources/Storage/alpha-platform/images/alpha_arch.pptx.png)

The Neutrinos Alpha Platform's Architecture can be broadly explained as follows:

- **BPM Designer**: A user interface designed for Business Analysts and BPM Administrators to create, deploy, and manage business processes in BPMN 2.0 standards. This tool integrates with the BPM Engine to deploy process definitions and execute Business Processes.
- **Admin UI**: Designed for Alpha Admin user to manage users, groups, and manage Case Instances.
- **Insights**: Offers analytics and reporting capabilities to monitor and evaluate case and workflow performance across the platform.
- **Alpha Studio**: A configuration tool that enables developers and analysts to configure models, tasks, pages, processes, manage environment settings, and define themes.
- **Workbench**: A Unified Experience for knowledge workers to manage cases, make Informed Decisions, and access dashboards.
- **BPM Service**: Handles the execution and management of business processes defined by Business Analysts in BPM Designer.
- **Admin Service**: The backend service supporting the Admin UI, responsible for managing users and groups and processing requests related to Case Instances.
- **Config Service**: Manage configurations  for Alpha Studio.
- **Request App Service**: Serves as the Backend for Frontend (BFF) for Workbench, routing requests to backend services such as CMS, DMS, BPM, and case management. Additionally, it handles environment-specific configurations deployed from Trinity.
- **Enquiry Service**: Manages the search and retrieval of case instances, including querying, filtering, and accessing all associated tasks and data within each specific case.
- **Case Manager Service**: Enables to interact with case instances, define cases, onboard and link them to process definitions, make decisions, add comments, and execute processes associated with case instances.

### External Adapters

External Adapter components standardize the APIs used by the core components of the Neutrinos Alpha Platform. These components ensure consistent access to information displayed to Workbench users and facilitate integration with other services that interact with or modify data through APIs.

- **CMS Adapter**: Facilitates integration with an external Content Management System (CMS) to handle content management and metadata processing.
- **DMS Adapter**: Enables integration with an external Document Management System (DMS), offering functionality to store, retrieve, and manage documents within the Neutrinos Alpha Platform.

### Users

The top section of the architectural diagram details different User Roles accommodated by the Neutrinos Alpha workflow

![Alpha platform users](/resources/Storage/alpha-platform/images/Users.png)

1. **Business Analyst**: A Business Analyst plays a critical role in evaluating existing ("as-is") business processes and transforming them into streamlined,
    goal-oriented workflows using the Neutrinos Alpha Platform. Their key responsibilities include:
  - **Analyzing Existing Processes**: Evaluate current business workflows to identify inefficiencies, bottlenecks, and areas for improvement.
  - **Translating into BPMN 2.0**: Convert the existing business process into an improved one, represented in BPMN 2.0 standards, for review and approval from both business and technical perspectives.
  - **Defining Business Objects**: Establish and manage Business Objects to accurately represent business requirements, ensuring consistency and alignment across the
      organization.
  - **Planning Process Transitions**: Develop a comprehensive roadmap to transition from the existing state to an optimized desired ("to-be") state, aligned with
      organizational goals.
  - **Monitoring and Feedback**: Continuously monitor deployed business processes, gather data-driven insights, and implement iterative improvements to refine strategies and
      enhance efficiency.
2. **Alpha Admin**: The Alpha Admin plays a pivotal role in overseeing the operational and organizational framework of the Neutrinos Alpha Platform. Their responsibilities ensure
    that user and process configurations align with organizational and project needs, enabling seamless execution of workflows and tasks. Alpha Admin’s key responsibilities
    can be listed as follows:
  - **Group and Role Management**:
    - Create and manage groups based on organizational or project-specific requirements.
    - Define groups based on the logical hierarchy provided by the business requirements or as determined by the task distribution logic.
  - **User Metadata Management**: Configure and maintain user metadata to optimize task allocation and team structure:
    - **Task Distribution**: Define task allocation strategies to balance workloads.
    - **Skills Management**: Tag users with relevant skills to match task requirements.
    - **Group Assignments**: Assign users to appropriate groups for streamlined operations.
  - **Case Management**
    - Monitor and interact with case instances throughout their lifecycle.
    - Perform case-based actions to ensure smooth processing and resolution:
  - **System Configuration**:
    - Configure and manage system-level settings to support efficient business processes execution.
    - Ensure compliance with organizational policies through robust system configuration.
3. **Studio Developer**: The Studio Developer plays a crucial role in translating business requirements into technical solutions on the Neutrinos Alpha Platform.
    They are accountable for ensuring end-to-end (E2E) project functionality and delivering scalable, efficient, and reusable solutions. By bridging business objectives
    with technical execution, the Studio Developer is integral to the success of Alpha projects. Their key responsibilities include:
  - **Requirement Analysis and Technical Design**:
    - Develop detailed technical designs that align with business goals and leverage platform capabilities.
  - **Business Object Design**:
    - Create well-structured, efficient, and searchable Business Objects to support workflows and data management.
  - **API Integration**:
    - Solution Design and Implementation of Integration Layer using Server Side Designer (SSD).
    - Use the business processes to invoke relevant Integration Layer APIs.
  - **Reusable UI Components**:
    - Design and develop reusable Alpha UI Components tailored to project-specific needs.
    - Publish these components to the marketplace, promoting standardization and efficiency across the platform.
  - **Solution Architecture Design**:
    - Architect solutions that are scalable, secure, and maintainable while aligning with organizational objectives.
    - Collaborate with stakeholders to validate and refine architectural decisions.
  - **Version Control and Change Management**:
    - Commit configuration versions and manage changes systematically to maintain platform integrity.
    - Document all changes thoroughly to support future updates and maintenance efforts.
  - **End-to-End Functionality Implementation**:
    - Oversee the full lifecycle of Alpha projects, including development, configuration, deployment, and testing.
    - Ensure workflows, integrations, and components function cohesively to deliver seamless solutions.
4. **Workbench User/Manager**: They are end-users of the Workbench application. They handle tasks, manage cases, and access dashboards.

### Cross-Functional Services

These systems enable Neutrinos Alpha's workflow to deliver flawless performance.

| **Component** | **Description** |
| --- | --- |
| Identity Server | The Identity Server manages user authentication and authorization and provides identity services for Alpha Platform. It integrates with external providers and maintains an OpenID user store for seamless access management. |
| Trinity | The deployment engine is responsible for configuring and deploying applications across different environments. Trinity provides the necessary environment variables to the Request App, allowing it to operate with correct context-specific settings. |
| Reels | The rules engine applies rule-based logic to processes and cases within the platform, either in the BPM Designer or directly through the Workbench, based on business requirements |

[Go to Top](/articles/alpha-platform/introduction-alpha-platform/a/Top)
