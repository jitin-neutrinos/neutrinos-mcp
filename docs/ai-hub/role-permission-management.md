# Interface

<https://documentation.neutrinos.com/articles/#!ai-hub/role-permission-management>

Role-Based Access Control (RBAC) is a security and authorization model that regulates system access based on predefined user roles. It defines how users are categorized and how access to system resources is granted through role assignments.

Instead of assigning permissions directly to individual users, RBAC introduces roles as an intermediary layer. Each role represents a defined set of responsibilities and includes a collection of permissions that determine the actions a user can perform within the platform.

When a user is onboarded, administrators assign one or more roles to the user. These role assignments automatically grant the user the corresponding access privileges.

| ![Note](/resources/Storage/ai-hub/project-trailproject/note.png) | Note: During the initial configuration, an owner is provisioned for each Organization. The owner is responsible for establishing access control policies and managing user roles and permissions within the respective Organization. |
| --- | --- |

## Interface

![ai-hub-users-landing-page](/resources/Storage/ai-hub/images/ai-hub-users-landing-page.png)

To access the **Role and Permission Management** section in the AI Hub platform, Navigate to **Users** from the AI Hub landing page using the left navigation panel. The Users page lists all users registered on the platform and provides details such as email address, assigned roles, and last recorded activity.

1. **User**: Displays the registered user’s name.
2. **Email**: Displays the email address of the registered user.
3. **Roles**: Displays all roles assigned to the registered user on the platform. The assigned roles define the permissions and access levels available to the user. **Note**: Permissions can also be modified by the owner at an individual permission level for a specific user.
4. **Last Activity**: Displays the timestamp of the user’s most recent activity on the platform.
5. **Actions**: The kebab icon in this column provides options to edit the user profile, manage access permissions, or remove the user from the platform.
    ![ai-hub-users-landing-page-action-button](/resources/Storage/ai-hub/images/ai-hub-users-landing-page-action-button.png)

## Roles

1. **Creator**: A Creator is a user with permissions to build and manage the end-to-end lifecycle of models, typically spanning model configuration, training orchestration, validation, and versioning.
  - Model Creation: Creators can create, train, retrain, and delete AI models within the platform. This includes configuring model parameters, associating datasets, initiating training jobs, and validating model outcomes.
  - Knowledge Article: Knowledge articles that augment or contextualize AI models.
  - API Configuration: API definitions and integrations that expose models.
  - Dataset: Browse and inspect datasets available on the platform
  - Access Audit Log: Creators have read-only access to audit logs, allowing them to track model-related activities, including creation, training runs, updates, and deletions.
2. **Deployer**: A Deployer is a platform role responsible for operationalizing AI models by promoting approved models into runtime environments and ensuring they are securely accessible for consumption. Deployers can view available and approved AI models and deploy them to designated environments such as development, staging, or production.
  - Deployment Management: Deployers handle the end-to-end deployment lifecycle, including redeployments, rollbacks, and updates to existing deployments.
  - Token Generation: Deployers can generate and manage access tokens used to authenticate and authorize consumers of deployed models.
  - Dataset and Marketplace Access: Deployers have read-only access to datasets and the marketplace to understand data dependencies and verify compatibility with deployed models.
  - Audit Log Access: Deployers can view audit logs related to deployments, token activities, and model access.
3. **Finance**: The Finance role provides visibility into platform usage, cost drivers, and consumption patterns to support financial reporting, budgeting, and operational analytics.
  - Dashboards: Finance users can view usage dashboards that present aggregated and detailed insights into platform consumption.
  - Audit Log Access: Finance users have read-only access to audit logs to track usage-related activities and validate consumption against billing or internal chargeback models.
  - Dataset Visibility: Finance users can browse available datasets to understand data usage patterns and dependencies that influence storage and processing costs.
  - Marketplace Access: Finance users can access the marketplace to review available models, datasets, and reusable assets from a cost and utilization perspective.
4. **Owner**: The Owner is the highest-privileged role within the AI platform and holds full administrative and operational control over all platform resources.
  - Full Resource Access: Owners have unrestricted access to all platform resources, including AI models, datasets, deployments, APIs, tokens, knowledge assets, marketplace items, dashboards, and audit logs. They can create, modify, delete, deploy, and govern resources across all environments without functional limitations.
  - User and Membership Management: Owners can add, remove, and manage members and assign or modify roles across the platform. A key responsibility of this role is the ability to transfer ownership to another member.
  - Additionally, Owners oversee the complete lifecycle of models - from creation and deployment through model purging. With full visibility into audit logs and activity trails, Owners ensure accountability for all actions performed within the platform.
5. **Reviewer**: A Reviewer is responsible for evaluating model behavior and inference outcomes to ensure accuracy and reliability.
  - Model Visibility: Reviewers can view available AI models and execute inference runs using approved inputs or datasets.
  - Inference Review: Reviewers can review, validate, and manage inference records, including outputs, confidence scores, timestamps, and associated metadata.
  - Dataset and Marketplace Access: Reviewers have read-only access to datasets to understand the input data context used during inference and evaluation.
  - Audit Log Access: Reviewers can view audit logs related to inference activity, model access, and review actions.

## Login

Users can log in to the platform using one of the following authentication methods:

1. **Platform-Based Authentication (RBAC Method)**: User accounts can be created directly within the platform. Access permissions are assigned using the Role-Based Access Control (RBAC) model. Once the user account is created and appropriate roles are configured, the user can log in using their registered credentials.
2. **Microsoft Azure Authentication**: Users can also log in using their Microsoft Azure credentials. If a user has valid Microsoft credentials, they can authenticate using the same. Additionally, users with an email address under the neutrinos.com domain are automatically routed to the projects assigned to them upon successful login.
    The following image illustrates the available login options using either IDS credentials or Microsoft Azure credentials.
    ![ai-hub-rbac-login-with-azure](/resources/Storage/ai-hub/images/ai-hub-rbac-login-with-azure.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: Even if a user logs in using Microsoft credentials, the user must be added to the platform and assigned the appropriate roles to obtain the required permissions.
