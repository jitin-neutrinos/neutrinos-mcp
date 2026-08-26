# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/email-out-node>

An **Email Out node** is used to send emails. Emails can be sent with attachments of images, files, HTML templates. You can also send calendar events.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available for you to use from Neutrinos Studio release 7.1.0. |
| --- | --- |

### How to use

- Open the Services editor window.
- Click the plus icon to add a new service or open an existing service from the service list.
- In the Nodes Palette, drag and drop an **Email Out **node to the workspace. Double click the node and configure its properties according to your need.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.

### Prerequisites

Depending on the mail provider you are using, you have to enable the Security and IMAP settings.

For example, if you are using the Google mail provider, perform the following steps:

1. Login to your Gmail account. Click the **Gear** icon on the right to change the mail settings and select** Settings**.
    ![Gmail Settings](/resources/Storage/server-services-designer-8/gmail_settings.png)
2. In the Settings editor, select **Forwarding and POP/IMAP** settings.
    ![email settings](/resources/Storage/server-services-designer-8/emailsettings.png)
3. Enable **POP **and** IMAP **settings. Save the changes.
    ![imap and pop settings](/resources/Storage/server-services-designer-8/IMAPandPOP.png)
4. Navigate to the **Account Settings** and select **Security**.
    ![account settings 1](/resources/Storage/server-services-designer-8/accountsettings1.png) ![account settings 2](/resources/Storage/server-services-designer-8/accountsettings2.png)
5. Scroll down and enable the **Less secure app access**.
    ![account settings 3](/resources/Storage/server-services-designer-8/AS3.png)

![Information](/resources/Storage/server-services-designer-8/info.png)


 Make sure you enable the Security and IMAP settings for the mail provider that you will be configuring in the Email node.

### Associated attributes

- **Name**: Display name of the node. This name will appear on the services editor when you save the node.
- **Mail Configuration**: Select a mail configuration that already exists from the drop-down list or click the **Edit **icon to add a new mail configuration. Configure the following** Server options** and **Email options** to add a Mail Configuration.
  - **Name**: Name of the new configuration.

#### Server Options

- **Host**: The hostname or the IP address of the mail provider. For example, the hostname for Gmail is **smtp.gmail.com **and for outlook is** smtp-mail.outlook.com. ![email out attributes](/resources/Storage/server-services-designer-8/Emailout1.png)**
  - To enter the query, choose string and enter the hostname directly.
  - You can choose the env type and enter the environment property that holds the port number. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.
- **Port**: The port that is used to connect to the host. Port values depend on which mail provider you select. For example, if you choose **Google**, the default port is **587** if **Secure** is set to false and port value is **465** if **Secure** is set to true. If you choose **Outlook**, the default port value is **587**.
  - To enter the port number, choose number and enter the port number.
  - You can choose the env type and enter the environment property that holds the port number. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.
- **Secure**: If set to true, the connection will use TLS when connecting to the server. If set to false, then TLS is used if the server supports the STARTTLS extension. By default, this property is set to** false**.
- **TLS**: Transport Layer Security (TLS), is a way to encrypt your email traffic from a server to another server. If TLS is set to true and secure is set to false, then nodemailer uses the STARTTLS command even if the server does not support it. If the connection cannot be encrypted, the message is not sent.

#### Email Options

- **UserID**: The UserID or the Username of your email account that you are using to send emails.
- **Password**: The password associated with the UserID.

#### Basic

- **From**: The email address of the sender.
  - If you are using the Outlook or Hotmail as your email provider, you need not enter any address in this field as it takes the email address from the Mail configuration. If you still want to enter any value make sure you enter the same email address used in the Mail configuration.
  - If you are using the mail providers other than Outlook or Hotmail, you can enter any other email address in this field. By default, it takes the email address from the Mail configuration.
     ![email basic fields](/resources/Storage/server-services-designer-8/emailbasic.png)
- **To**: An array or comma-separated list of receivers' email addresses.
- **CC**: An array or comma-separated list of receivers' email addresses.
- **Bcc**: An array or comma-separated list of receivers' email addresses.
- **Subject**: The subject of the email.
- **Body**: The plaintext version of the message. It can be a Unicode string, Buffer, Stream or an attachment.
- **Htm**l: The HTML version of the message. It can be a Unicode String, Buffer, Stream, or an attachment like object. For example, select bh.input and enter mailHtml where mailHtml is the object name defined in the script node which contains the Html version of the message.

You can map these fields to a property type, choose bh. , bh.input, or bh.local property from the drop-down list and enter the variable name which contains the values for these fields or choose string and enter the values directly.

- **Attachments**: An array of attachment objects which can include files, images, etc. Click the map icon and enter the object name which contains the options for attaching a file. Refer [Attachments options](https://nodemailer.com/message/attachments/) to learn more about the various options that you can include for attachments. Map the attachments to a property type by:
  - Choosing bh. , bh.input, or bh.local property from the drop-down list and entering the variable name defined in the script node which contains the attachment options.
  - Choosing as is or string and entering the attachment options directly.

You can also click the plus ![](/resources/Storage/server-services-designer-8/designing-data-models-2019-05-31.png)icon and enter the following fields to add an attachment:

- **Filename**: The name of the file that you want to attach the email. Make sure you specify the Extension of the file. ![attachment options for email out](/resources/Storage/server-services-designer-8/attchmentiptions.png)For example, if the file is an image of the jpeg format, then the extension should be **img****.jpeg**.
- **Content**: The content of the file. It can be Buffer or Stream contents for the attachment. For example, select bh.local and enter fileincontent where fileincontent is the object name defined in the script node that includes the content of the file.
- **File path**: The path of the file. For example, /home/neutrinos/Downloads/download.jpeg.
- **Encoding**: **Encoding** standards tell the **email** application how to interpret the text characters in your HTML or the body of the **email.** Example values used to set encoding are **base64**, **hex**, **binary**, etc. By default, it is set to **utf8**.

You can map all the above fields to a property type. Choose bh. , bh.input, or bh.local property from the drop-down list and enter the variable name or choose as is or string and enter the values directly.

#### Advanced Fields

- **iCal Object**: An object to define a calendar event.
  1. Create an object in a [Script node](/articles/server-services-designer-8/script-node) and assign the calendar event options to that object. See [Calendar event options](https://nodemailer.com/message/calendar-events/) to learn more about the options that you can provide for creating a calendar event. For example,
  2. Enter the name of the object that you have defined in the **iCal Object **field. For example,

You can use any opensource calendar event generator to generate a calendar event. For example, you can use this [ical generator](https://ical.marudot.com/).

- **Routing Options**: Define additional options for Routing an email in an object inside a script node and mention the object name in this field. Refer [Routing options](https://nodemailer.com/message/#routing-options) to learn more about the options that you can provide.
- **Content Options**: Define additional options for the email content in an object inside a script node and mention the object name in this field. Refer [Content options](https://nodemailer.com/message/#content-options) to learn more about the options that you can provide.
- **Header Options**: Define additional options for headers of an email in an object inside a script node and mention the object name in this field. Refer [Header options](https://nodemailer.com/message/#header-options) to learn more about the options that you can provide.
- **Security Options**: Define additional options for security of an email in an object inside a script node and mention the object name in this field. Refer [Security options](https://nodemailer.com/message/#security-options) to learn more about the options that you can provide for content options.

You can map all the Advanced options to a property type. Choose bh. , bh.input, or bh.local property from the drop-down list and enter the variable name defined in the script node which contains the options for the respective fields.

**Result Mapping**: You can map the retrieved data to bh. , bh.local or bh.input properties. Select the parameter type and enter the variable that should hold the output.
