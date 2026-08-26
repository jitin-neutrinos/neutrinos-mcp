# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/active-directory-node>

An **Active Directory** (**AD**) is a Microsoft product that consists of several services that run on a Windows Server to manage permissions of the users and their access to the networked resources. It also serves as a centralized data storage for quick access to all users and their controlled access based on the security policies set in place.

The** Active Directory**** n****ode **is used to perform the operations related to the active directory such as authentication, findUser, etc.

### How to use

- Open the Server Services editor window.
- Click the plus icon to add a new server service or open an existing service from the service list.
- In the Nodes palette list, drag and drop the **Active directory** node to the workspace. Double click the node and configure the properties of the node.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node or an HTTP In node.**

### Associated attributes

1. **Name: **Unique name given for the node. This name will display on the canvas when you save the node.
2. **Active Directory config**: The **Active Directory** **Configuration **of your organization. Click the **Map icon** and configure your organization details. The fields that you need to configure to add a new Active Directory to the list are:  After entering the details click the done ![](/resources/Storage/server-services-designer-8/correct.png) icon and the new Active Directory configuration gets added to the list. Select the Active Directory config from the drop-down list.
  - **Name**: The name of the Active Directory.
  - **Active Directory URL**: Map this field to str or env property type and enter the **Active Directory URL** (LDAP URL) to configure the connection to the directory server. It is the URL where your Active Directory is hosted. If you choose env, enter the environment property which contains the value. Make sure that the environment property is added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before calling this property here.
  - **Base DN**: Map this field to str or env property type and enter the **Base DN**. Base DN is the section of the directory where the application will commence searching for users and groups. For example, if the domain name is **domain.neutrinos.org**, then the base DN can be **dc=domain,dc=neutrinos,dc=org**.
  - **Username Postfix**: Map this field to str or env property type and enter the **Username Prefix** to be prepended to the username before the Active Directory bind is attempted. Usually, the prefix is the domain of your organization. For example, if **@test.neutrinos.io** is the [User Principal Name(UPN)](https://www.codetwo.com/kb/upn/#:~:targetText=In%20Windows%20Active%20Directory%2C%20a,domain%20name%20(UPN%20suffix).), then **@test** is the prefix.
  - **Username Prefix**: Map this field to str or env property type and enter the **Username Postfix **to be appended to the username before the Active Directory bind is attempted. For example, if **@test.neutrinos.io** is the UPN, then** .io** is the postfix.
  - **Admin Username**: Map this field to str or env property type and enter the username of the Admin who is managing the Active Directory.
  - **Admin Password**: Map this field to str or env property type and enter the password of the Admin who is managing the Active Directory.
3. **Operation Type**: The type of operation the node should perform. By default, **Authentication** is the type of operation the node will perform.
  - **Authenticate**: Authenticates the username and password by doing a simple bind operation with the specified credentials.
    - **username: **The username that is to be authenticated.
    - **password: **The password associated with the username.
    - **sAMAccountName:** The **sA****M****AccountName** to authenticate. The logon name used to support clients and servers from the previous version of Windows, such as Windows NT 4.0, Windows 95, Windows 98, LAN Manager, etc.
  - **isUserMemberOf**: Checks whether the user is a member of the specified group or not.
    - **username: **The username to be checked against the membership in the group.
    - **groupName: **The group name against which the username has to be checked.
  - **findUser**: Finds a user by their **sAMAccountName**. If found, the returned object contains all of the requested attributes.
    - **sAMAccountName:** The **s****AMAccountName** to find the user.
  - **getGroupMembershipForUser: **For the specified username, retrieve all of the groups that a user belongs to.
    - **sAMAccountName:** Specify the **sAMAccountName** to retrieve the groups in which the user belongs.
  - **findGroup**: Finds a group within the Active Directory based on the group name specified.
    - **GroupName: **The unique group name from which the information is to be retrieved.
  - **groupExists**: Checks if the specified group exists or not.
    - **GroupName: **The name of the group to be checked.
  - **getGroupMembershipForGroup**: For the specified group, this retrieves all the groups the group is a member of.
    - **GroupName: **Specify the group name to retrieve the group membership.
  - **getUsersForGroup**: For the specified group, this retrieves all the users that belong to the group.
    - **GroupName:** Specify the name of the group to check for the membership of the user.
  - **findUsers**: Used to search users that match the specified filter.
    - **Query:** The query to obtain the desired data about the users.
  - **findGroups**: Used to search groups that match the specified filter.
    - **Query: **The query to obtain the desired data about the groups.
  - **userExists**: Checks if the specified user exists or not.
    - **username: **The username to be checked.
  - **findDeletedObjects**: Retrieves items from the recycle bin.
    - **Options:** Provides optional parameters to extend the search functionality. See [Optional Parameters](https://www.npmjs.com/package/activedirectory#opts).
4. **Result Mapping**: You can map the retrieved data to bh.local or bh.input properties. For example, if you specify bh.input.result in this field, then that input parameter will hold the content of the file in the selected output format. See[properties](/articles/server-services-designer-8/properties-in-server-services) to know more.
