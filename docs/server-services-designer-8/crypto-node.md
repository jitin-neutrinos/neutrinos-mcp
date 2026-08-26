# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/crypto-node>

The Crypto node is used to perform encryption and decryption of data using security algorithms.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.5.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Download the Plugin from Neutrinos Store. See [Download from Store](/articles/studio-guide-7/import-plugin).
- In the Nodes Palette, search for the installed node and drag and drop the **Crypto** node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node.**

### Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. To call the flow in which the node is used, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Type of Operation: **The type of operation you want to perform on the data. See [Crypto Operations](/articles/server-services-designer-8/crypto-node/a/h3__1822811531) to learn more.
- **Input Type:** The format in which you want to provide the data. Input type includes:
  - **Text:** Enter the data directly in the **Input **field.
  - **File: **Upload the file containing the data in the **Input **field.
  - **Buffer:** Provide the buffer in the **Input **field.
- **Password:** The secret using which you want to encrypt the data. You should use the same password to view the encrypted data on the receiver's end.
- **Input: **The data to be encrypted or decrypted.
- **Options:** The string encoding to use when the key is of **string** type.If you do not want to provide any options, pass a blank object.
- **Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

---

### Crypto Operations

#### Create HMAC

Encrypts data using the hash function and key that you choose. Note that the encrypted data cannot be decrypted.

HMAC stands for Keyed-Hashing for Message Authentication. It is a message authentication code obtained by running a cryptographic hash function (like MD5, SHA1, and SHA256) over the data (to be authenticated) and a shared secret key.

**HMAC Attributes**

- **Hash: **Select a hash function to encrypt the data.
- **Input Encoding:** Select the type of encoding to be performed on the data.

#### Create Cipher

Creates a ciphertext using the algorithm and password that you choose. After creating the ciphertext, this operation will provide the encrypted data and the initialization vector as the output.

You can decide the length of the initialization vector and provide it in the **Initialization vector length** attribute.

**Cipher attributes**

- **Algorithm:** Select an algorithm to encrypt the data.
- **Input encoding: **The input encoding format in which you want to read the data.
- **Output encoding:** The output encoding format in which you want to send the data.
- **Salt:** The random string of data to be used to modify a password. It is an additional supplement to generate a stronger password to encrypt the data. Neutrinos uses the node.js scrypt() class that takes the password, salt, and keylength to generate a stronger key. See [node.js documentation](https://nodejs.org/api/crypto.html#crypto_crypto_scrypt_password_salt_keylen_options_callback) to learn more. To decrypt, you should use the same salt on the encrypted data.
- **Keylen:** The length of the key. The key length differs based on the algorithm that you choose.
- **Initialization vector length:** The length of the initialization vector. An initialization vector (IV) is an arbitrary number that can be used along with a secret key for data encryption. It is an additional supplement to generate a stronger password to encrypt or decrypt data.

#### Create Decipher

Deciphers the ciphertext using the algorithm and password that you choose. To decipher the data, you should know the initialization vector, password, keylength, and the salt that was provided to encrypt the data.

**Decipher attributes**

- **Algorithm:** Select an algorithm from the list to decrypt the data.
- **Input encoding: **The input encoding format in which you want to read the data.
- **Output encoding:** The output encoding format in which you want to send the data.
- **Salt:** The random string of data that was used to encrypt the data.
- **Keylen:** The length of the key that was used to encrypt the data.
- **Initialization vector:** The initialization vector that was provided by the **Create Cipher** operation.
