# Session

<https://documentation.neutrinos.com/articles/#!concepts-publication/session>

### Session

Server-side information that is desired to persist throughout the user's interaction with the website. **Session management** is a term for the secure implementation of sessions. It is the rule that is set for interactions between a web-based application and users.

### How Sessions Work

For a single user application, like a desktop application, there is only one user, so there is also one session, it is not difficult for the application to make the connection between the user and their session data.

However, for a web application, a server has multiple clients. It identifies its clients through the session ID. A session ID is a unique identifier that a website's server assigns to a specific user for the duration of that user's visit.

You as the client, give the server your session id, and in return the server grants you access to your session data if it finds your session id stored in its session data store.

After the client acquires a client session, it can send read requests to the server. The server session responds to these requests as follows:

- If the object or data is in the session cache, then the server session returns the information back to the client.

- If the object or data is not in the cache, then the server session reads the information from the database or memory and stores the object in the session cache. The objects are then available for retrieval from the cache.
