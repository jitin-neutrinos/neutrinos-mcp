# Model Types

<https://documentation.neutrinos.com/articles/#!ai-hub/architecture>

This topic outlines the architecture of the AI Hub platform, detailing the end-to-end flow, from data ingestion to consumer integration. The modular and scalable architecture covers key stages: Model Types, Training, Deployment, Inferencing, Monitoring, Data Management, and Consumption.

The diagram below illustrates the platform architecture:




 ![ai-hub-architecture](/resources/Storage/ai-hub/images/AI_HUB_ARCH%202.png)

## Model Types

The platform supports various AI/ML model categories:

- **LLM**: Large Language Models.
- **SML**: Small Language Models.
- **Prediction**: Traditional models for regression and/or classification.
- **Extraction**: Named Entity Recognition

Model types are modular and can be tailored based on use cases.

## Training Pipeline

Training is a core capability in the platform and includes the following stages:

- **Data Ingestion**: Source data is pulled into the system.
- **Annotation**: Labeling and tagging for supervised learning.
- **Evaluation**: Model performance metrics are calculated before progressing.
- **Enrich/Tuning**: Data is preprocessed, and model parameters are fine-tuned.
- **Training**: Final model training happens in a containerized or distributed setup.

## Deployment

Once training is complete, models are deployed across controlled environments:

- **Sandbox**: For testing and staging.
- **Production**: For live usage with real-time inference capabilities.

## Inferencing

Models once deployed can be consumed through multiple inferencing modes:

- **Sync/Single**: Real-time predictions via synchronous API calls.
- **Async/Batch**: This is used to process large documents asynchronously.
- **Version Management**: Enables tracking and managing different model versions.
- **Review Hub**: Supports human-in-the-loop validation workflows.

## Monitoring

The platform provides observability and traceability of AI system behavior:

- **Audit**: Captures user activity, model changes, and system events.
- **Insights**: Displays performance metrics, usage direction, and usage statistics.

## Data Infrastructure

AI Hub utilizes various storage structures to efficiently manage processed data and ensure seamless access during data consumption workflows:

- **File Buckets**: Serve as repositories for storing processed files such as CSVs, Excel documents, PDFs, and other supported formats.
- **Meta Info**: Acts as a metadata layer, capturing field-level information and contextual data about models.
- **Image Repository**: Stores and manages the Docker files.
- **Caching**: Temporarily holds frequently accessed data to improve response times and reduce redundant processing during repeated access.
- **Async Events**: Facilitates the handling of event-driven operations by storing processed event data, enabling actions such as triggering retraining processes or batch validations.

## Consumers

Final model outputs and capabilities are consumed via multiple touchpoints:

- **Workbench**: Developer or analyst interface for testing and exploration.
- **SSD**: Server Side Designer modules.
- **Reels**: Integrate the Neutrinos Reels Engine.
- **External**: Integration points for third-party systems and APIs.

The AI Hub architecture offers a comprehensive and flexible pipeline for managing AI models throughout their lifecycle—from ingestion and training to inference and monitoring—while ensuring integration with underlying consumer applications.
