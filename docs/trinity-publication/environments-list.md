# Environment Dashboard

<https://documentation.neutrinos.com/articles/#!trinity-publication/environments-list>

The Environment List page, provides an overview of the created environment, the projects associated with it, performance and resource details.

![](/resources/Storage/trinity-publication/environments-list/Allenvirons.jpg)

#### Environment Dashboard

The Environment dashboard provides information specific to the selected environment. This information relates to the system resource level and includes pod status, which pods have restarted recently, the amount of CPU and memory the pods are consuming. It reveals that the resources being utilized, and workloads that are actively running at the moment.

To view the dashboard:

1. Navigate to All environments screen.
2. Select an environment by clicking on it.
3. Click on Live Dashboard to view the details.
   ![](/resources/Storage/trinity-publication/environments-list/dashboard.png)

The Live Dashboard screen is divided in to 3 sections:

- [Environments](/articles/trinity-publication/environments-list/a/envs)
- [Projects](/articles/trinity-publication/environments-list/a/Projs)
- [Applications](/articles/trinity-publication/environments-list/a/appl)

Each section is described in detail.

#### Environments

![](/resources/Storage/trinity-publication/environments-list/perma1.png)

![](/resources/Storage/trinity-publication/environments-list/cpusage.png)

![](/resources/Storage/trinity-publication/environments-list/report.png)

##### CPU Usage Graph

The CPU usage graph provides a detailed visualization of CPU metrics over time, including:

- CPU %: Percentage of CPU capacity being utilized.
- CPU Usage: Absolute CPU usage in terms of core count.
- Idle: Percentage of CPU time spent idle.
- IO Wait: Percentage of CPU time spent waiting for I/O operations.
- User: Percentage of CPU time spent on user processes.

The graph shows a timeline (x-axis) against the CPU usage percentages (y-axis), giving users insight into the CPU performance trends and helping identify periods of high or low activity.

##### Nodes

The Nodes sub-section provides detailed information about each node in the cloud environment. Each node entry includes:

- IP Address: The unique address of the node.
- Uptime: The duration for which the node has been running without interruption (e.g., 2 months).
- Data Transfer: The amount of data transferred by the node, along with the current data transfer rate (e.g., 46.68 KB/s).
- Cores: The number of CPU cores allocated to the node (e.g., 8 cores).
- Memory: The amount of memory available to the node (e.g., 15 GB).
- CPU Used: The percentage of CPU currently being utilized by the node (e.g., 1.7%).
- Memory Used: The percentage of memory currently being utilized by the node (e.g., 28.04%).

#### Projects

##### CPU Usage

![](/resources/Storage/trinity-publication/environments-list/use.png)

The CPU usage graph displays usage over time for several different processes or environments. These processes are represented by different colors:

- Dynamic (Orange)

- Test-sync-secret (Green)

- India (Purple)

- regression-final (Blue)

The time range is shown on the x-axis. The y-axis represents the CPU usage percentage.

##### Memory Usage

![](/resources/Storage/trinity-publication/environments-list/memusage.jpg)

The memory usage graph tracks memory consumption over time for the same set of processes. The x-axis spans from a specific time range, and the y-axis measures memory usage in megabytes (Mb).

This analysis helps in identifying which processes are resource-intensive and may need optimization or monitoring to ensure system performance remains optimal.

#### Applications

The memory usage screen offers a comprehensive visualization of the application's memory consumption over time, enabling a deeper understanding of the application's performance patterns and potential issues.

![](/resources/Storage/trinity-publication/environments-list/perform.png)

**Promql details**

To view and edit Promql details, follow these steps:

1. Navigate to All environments screen.
2. Select an environment by clicking on it.
3. Click on the ellipse icon corresponding to Add New Environment > Environment Configurations.
   ![](/resources/Storage/trinity-publication/my-profile/promql.png)
   The Environment configuration pop-up window is displayed.
   ![](/resources/Storage/trinity-publication/my-profile/envconf.png)
4. Add/edit the Promql details.
