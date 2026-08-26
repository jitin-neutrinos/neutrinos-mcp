# Package Information

<https://documentation.neutrinos.com/articles/#!pulse-publication/case-service-plugins-gcc>

A comprehensive case management service for Alpha UI Base that provides complete workflow and case lifecycle management capabilities, including case definitions, instances, enquiries, and process management.

### Package Information

- Name: alpha-module-case-servcie
- Version: 1.0.1
- Description: Complete case management and workflow service
- Exposed Name: caseService

### Features

- Case Definition Management: Create, read, update case definitions and schemas
- Case Instance Lifecycle: Full case instance management from creation to completion
- Process Definition: Workflow process management and task definitions
- Case Enquiry System: Dynamic case enquiry creation and management
- Audit Trail: Comprehensive case activity tracking and comments
- Signal Management: Case signal handling for workflow coordination
- Multi-tenant Support: User and group-based case access control

### API Reference

#### Main Service: Case Service

The main service that orchestrates all case management operations.

```javascript
class CaseService {
  public caseDef: CaseDefnitionService;        // Case definition operations
  public caseInstance: CaseInstanceService;    // Case instance operations
  public processDef: ProcessService;           // Process definition operations
  public caseEnquiry: CaseEnquiryService;     // Case enquiry operations
}
```

#### Service Components

1. Case Definition Service (caseDef): Manages case definitions, schemas, and configurations
    Key Methods:
  - addCaseDefinition(args: CaseDefSchema): Create new case definition
  - getCaseDefinitionByCaseType(args: GetCaseDefinition): Retrieve case definition
  - updateCaseDefinition(args: CaseDefSchema): Update existing definition
  - getAllCaseDefinition(args?: GetAllCaseDefinition): List all definitions
2. Case Instance Service (caseInstance): Handles individual case instances and their lifecycle.
    Key Methods:
  - createCase(args: CreateCaseInstance): Create new case instance
  - getCase(args: FetchCaseInstance): Retrieve case details
  - getAllCase(args: FetchAllCaseInstances): List cases with filtering
  - updateCaseData(args: UpdateCaseData): Update case information
  - updateCaseStatus(args: UpdateCaseStatus): Change case status
  - abortCase(args: AbortCase): Terminate case execution
  - addCaseComment(args: AddCaseComment): Add comments to case
  - addCaseAudit(args: AddCaseInstanceAudit): Log audit entries
3. Process Service (processDef): Manages workflow process definitions and task configurations.
    Key Methods:
  - createProcessDefinition(args: ProcessDefinition): Create workflow process
  - getProcessDefinition(args: GetProcessDefinition): Retrieve process details
  - updateProcessDefinition(args: UpdateProcessDefinition): Update process configuration
4. Case Enquiry Service (caseEnquiry): Handles dynamic case enquiry creation and management.
    Key Methods:
  - createCaseEnquiry(args: CreateCaseEnquiry): Create new enquiry
  - getCaseEnquiry(args: GetCaseEnquiry): Retrieve enquiry details
  - updateCaseEnquiry(args: UpdateCaseEnquiry): Update enquiry
  - searchCaseEnquiry(args: SearchCaseEnquiry): Search enquiries

### Data Models

#### Case Definition Schema

```javascript
interface CaseDefSchema {
  caseDefinitionSchema: {
    caseSchema: Record<string, any>;
    pdid: number;
    subProccess?: number[];
    active: true;
  };
  caseType: string;
  version: string;
}
```

#### Case Instance Creation

```javascript
interface CreateCaseInstance {
  caseType: string;
  caseData: Record<string, any>;
  wfData?: Record<string, any>;
}
```

#### Process Definition

```javascript
interface ProcessDefinition {
  processName: string;
  processVersion: string;
  processDefinitionId: string;
  metadata: Record<string, any>;
  processSLA: string;
  mainProcess?: boolean;
  taskDefinition: {
    taskName: string;
    taskType: string;
    inputSchema?: Record<string, any>;
    outputSchema?: Record<string, any>;
    displayText?: string;
    taskSLA?: string;
    taskIcon?: string;
  }[];
}
```

#### Case Enquiry

```javascript
interface CreateCaseEnquiry {
  caseType: string;
  fieldName: 'field1' | 'field2' | 'field3' | 'field4';
  displayName: string;
  mapping: string;
}
```

### Usage Examples

#### Basic Case Management

```javascript
// Create a new case
const newCase = await ap.caseService.caseInstance.createCase({
  caseType: 'customer-support',
  caseData: {
    customerId: '12345',
    issue: 'Technical problem',
    priority: 'high'
  }
});

// Get case details
const caseDetails = await ap.caseService.caseInstance.getCase({
  cid: newCase.cid
});
```

#### Case Definition Management

```javascript
// Create case definition
const caseDef = await ap.caseService.caseDef.addCaseDefinition({
  caseDefinitionSchema: {
    caseSchema: {
      customerId: { type: 'string', required: true },
      issue: { type: 'string', required: true },
      priority: { type: 'string', enum: ['low', 'medium', 'high'] }
    },
    pdid: 1,
    active: true
  },
  caseType: 'customer-support',
  version: '1.0.0'
});
```

#### Process Management

```javascript
// Create process definition
const process = await ap.caseService.processDef.createProcessDefinition({
  processName: 'Customer Support Process',
  processVersion: '1.0.0',
  processDefinitionId: 'cust-support-v1',
  metadata: { category: 'support' },
  processSLA: '24h',
  mainProcess: true,
  taskDefinition: [
    {
      taskName: 'Initial Review',
      taskType: 'human',
      inputSchema: { reviewNotes: 'string' },
      displayText: 'Review customer issue',
      taskSLA: '2h'
    }
  ]
});
```

#### Case Enquiry System

```javascript
// Create case enquiry
const enquiry = await ap.caseService.caseEnquiry.createCaseEnquiry({
  caseType: 'customer-support',
  fieldName: 'field1',
  displayName: 'Customer ID',
  mapping: 'customer.customerId'
});

// Search enquiries
const searchResults = await ap.caseService.caseEnquiry.searchCaseEnquiry({
  caseType: 'customer-support',
  query: 'technical',
  pageSize: 10,
  pageNumber: 1
});
```

### Case Lifecycle

#### Case Statuses

The system supports the following case statuses:

- CREATED: Case has been created
- READY: Case is ready for processing
- RESERVED: Case is assigned to a user
- INPROGRESS: Case is being worked on
- SUSPENDED: Case is temporarily suspended
- COMPLETED: Case has been completed
- FAILED: Case processing failed
- ERROR: Error occurred during processing
- EXITED: Case has exited the workflow
- OBSOLETE: Case is no longer relevant

#### Workflow Integration

```javascript
// Get workflow data
const wfData = await ap.caseService.caseInstance.getCaseWfData({
  cid: caseId
});

// Set workflow data
await ap.caseService.caseInstance.setCaseWfData({
  cid: caseId,
  variables: {
    currentStep: 'review',
    assignedTo: 'user123',
    dueDate: '2024-01-15'
  }
});
```

### Case Analytics

#### Dashboard and Reporting

```javascript
// Get case dashboard data
const dashboard = await ap.caseService.caseInstance.getCaseDashBoard({
  caseType: 'customer-support'
});

// Get case count with filters
const count = await ap.caseService.caseInstance.getCaseCount({
  userName: 'user123',
  groups: ['support-team'],
  caseType: 'customer-support',
  status: ['READY', 'INPROGRESS']
});
```

### Access Control

#### User and Group Management

```javascript
// Check in case (assign to user)
await ap.caseService.caseInstance.caseCheckIn({
  cid: caseId,
  tiid: taskId,
  userName: 'user123'
});

// Delegate case to another user
await ap.caseService.caseInstance.delegateCaseToUser({
  cid: caseId,
  tiid: taskId,
  userName: 'user456'
});
```
