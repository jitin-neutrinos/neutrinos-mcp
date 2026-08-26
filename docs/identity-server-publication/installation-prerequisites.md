# IDS Domain with SSL Certificate

<https://documentation.neutrinos.com/articles/#!identity-server-publication/installation-prerequisites>

Before you install Identity server, be sure you have met the installation prerequisites, and then follow the installation instructions. This section will provide you with the installation prerequisites for identity server.

##### IDS Domain with SSL Certificate

- IDS requires a DNS name and SSL Certificate to be able to install successfully.
- Certificate Formats: PEM, Private Key used for CSR.

##### Database

Ensure that the following components related to the database are available:

- DB Host:
- DB Port:
- DB Name:
- DB Password:
- DB Schema:
- DB User Name:
- Docker Image URL:
- Uuid-ossp extension(has to be installed in PostgreSQL

##### Tools required

The following tools are required:

- Kubectl
- Helm

##### Kubernetes Environment

- Kubernetes cluster(with at least one node 1 vCPU, 1 GB RAM)
- Nginx ingress controller
