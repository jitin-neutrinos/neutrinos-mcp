# Liveness Probe

<https://documentation.neutrinos.com/articles/#!trinity-publication/probes>

Probes are used to assess and monitor the health and operational status of a container within a Pod. They help ensure that the container is functioning correctly and responding as expected by periodically checking its state and performance. If a probe detects an issue, it can trigger corrective actions such as restarting the container or marking it as unhealthy, which helps maintain the overall reliability and stability of the application that has been deployed.

There are three types of probes within Trinity:

1. Liveness Probe
2. Readiness Probe
3. Startup Probe

#### Liveness Probe

This determines if a container is running correctly. If the liveness probe fails, Kubernetes restarts the container. This is useful for situations where the application might have entered an inconsistent or hung state.

![](/resources/Storage/trinity-publication/probes/LivenessProbe.jpg)

#### Readiness Probe

This indicates if a container is ready to service requests. If the readiness probe fails, the container is temporarily removed from service endpoints, but it continues to run. This is useful to delay traffic until the container is ready to handle it, preventing requests from being sent to a container that's not yet prepared to process them.

![](/resources/Storage/trinity-publication/probes/Readinessprobe.jpg)

#### Startup Probe

This is used to determine when a container application has started. It complements the liveness probe by allowing Kubernetes to delay considering the container available until it's ready to serve requests. Once the startup probe succeeds once, Kubernetes stops performing the startup probe checks.

![](/resources/Storage/trinity-publication/probes/Startupprobe.png)

Each probe type can be configured with parameters such as the probe type (HTTP, TCP, or Exec), the path or command to execute, and thresholds for success and failure. Probes are defined in the Pod specification and are crucial for maintaining the reliability and responsiveness of applications running in Kubernetes clusters.
