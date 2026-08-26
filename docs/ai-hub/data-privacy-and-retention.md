# Data Retention

<https://documentation.neutrinos.com/articles/#!ai-hub/data-privacy-and-retention>

In a data-driven landscape, safeguarding sensitive information is paramount—not only to maintain user trust but also to comply with stringent regulatory requirements. Data privacy refers to the principles and practices that govern how personal or sensitive data is collected, processed, and stored. It ensures that data is handled responsibly, transparently, and in alignment with legal obligations

Equally important is data retention, which defines how long data is preserved before being securely deleted or anonymized. Retention policies help organizations balance operational needs with privacy concerns, ensuring that data is not held longer than necessary.

While the platform leverages Large Language Models (LLMs), Optical Character Recognition (OCR), and generative AI (such as the Assistant chatbot) for extraction, it also incorporates robust data privacy controls. A key feature is PII Masking, which ensures that personal, organizational, and sensitive information is masked before being transmitted to LLMs. This prevents unintended data exposure during model inference, ensuring that any sensitive content—whether extracted from documents or entered as user input—is protected throughout the model execution lifecycle.

To ensure data privacy and security, all input data used for training is stored in dedicated containers (also known as tenants) in the Neutrinos servers. Each tenant is assigned to a specific business or business unit, keeping their data logically and physically separated from others. This ensures:

- Data Isolation: Each business unit’s data is kept separate to prevent cross-access or accidental sharing.
- Privacy Protection: Sensitive information—whether extracted from documents or entered directly by users—is protected at every stage of the model lifecycle
- Secure Execution: The model training and execution process is designed to comply with enterprise-grade security standards, ensuring data is secure from ingestion through to inference.

In summary, the training process ensures that AI models are both accurate and reliable, while upholding the highest standards of data privacy and confidentiality. With built-in safeguards and secure data handling practices, AI Hub enables organizations to confidently apply AI to business-critical use cases, knowing that their information remains protected throughout the entire model development and deployment lifecycle

## Data Retention

In AI Hub, although organizational data is hosted on Neutrinos servers, it is securely containerized within dedicated tenant spaces. This architecture ensures data isolation, enhances security, and supports compliance with industry and regulatory requirements.

The data retention on the platform happens through 3 broad categories:

- Training data associated with specific prediction (classification), extraction models, or even the Assistant (chatbot – generative model) is retained only as long as the corresponding models exist on the platform. Once a model is deleted, all related data and artifacts are purged. Neutrinos ensures that no residual or derivative data remains in any shared systems, maintaining strict data privacy and integrity standards.
- Inference data is governed by configurable retention rules at individual model level. These rules can be defined under the Retention and Others section at the time of training. Based on these configurations, inference data can be automatically purged, offering organizations control over data lifecycle management.
- Additionally, audit log data—which includes information such as consumption details, timestamps, and model-related metadata used solely for billing purposes (excluding any organization-specific information) - is retained even after the associated models are deleted or the subscription is terminated.

| ![Note](/resources/Storage/ai-hub/project-trailproject/note.png) | To adhere to industry standards and ensure compliance, all data is automatically deleted from the servers within a maximum retention period of 30 days. |
| --- | --- |
