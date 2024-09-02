
When you see "SFTP - Pull catalog from files on an FTP server," it generally refers to using Secure File Transfer Protocol (SFTP) to download or retrieve a list of files or data (the catalog) from a server that hosts files using the File Transfer Protocol (FTP).

sftp username@ftp.server.com
sftp> get catalog_file.txt
sftp> mget *.txt


When you see "API - Pull catalog from API exposed," it generally means using an Application Programming Interface (API) to retrieve or download a list of items, data, or resources (the catalog) that the API makes available (exposes).


using request library
response = requests.get(url)
url = "https://api.example.com/catalog"

using curl request
curl -X GET "https://api.example.com/catalog"

In the context of Magento, a "plugin feed" typically refers to a method for integrating external data feeds (such as product catalogs, inventory updates, or other content) into a Magento store using plugins or extensions. These plugins are designed to import, manage, and synchronize data from various external sources with the Magento eCommerce platform.

- **Magento**:
    
    - Magento is a popular open-source eCommerce platform that provides a flexible shopping cart system and control over the look, content, and functionality of an online store.
- **Plugin**:
    
    - A plugin (or extension) in Magento is a piece of software that can be installed to add specific features or functionality to a Magento store.
- **Feed**:
    
    - A feed is a data file that contains structured information, usually in formats like XML, CSV, or JSON. Feeds can include product information, prices, inventory levels, etc.
Here's a high-level overview of how you might use a plugin to import a product feed into Magento:

1. **Choose a Plugin**:
    
    - There are various plugins available for Magento that facilitate data feed imports, such as "Data Feed Manager" or "Improved Import & Export" by Firebear Studio.
2. **Install the Plugin**:
    
    - Install the chosen plugin through Magento's admin interface or via Composer.
3. **Configure the Plugin**:
    
    - Access the plugin's settings in the Magento admin panel.
    - Configure the source of the feed (e.g., an FTP server, a URL, or a local file).
    - Map the fields in the feed to the corresponding fields in Magento (e.g., product name, SKU, price, inventory level).
4. **Schedule the Import**:
    
    - Set up a schedule for the feed import (e.g., hourly, daily).
    - The plugin will automatically fetch and import the feed data according to the schedule.
5. **Monitor and Manage**:
    
    - Monitor the import process through logs and reports provided by the plugin.
    - Handle any errors or conflicts that arise during the import
- - **Configure Feed Source**:
    
    - Navigate to the plugin configuration page.
    - Select the feed source type (e.g., FTP, URL).
    - Enter the necessary credentials or URL.
- **Field Mapping**:
    
    - Map the fields from the feed to Magento product attributes.
    - Example: Map the `product_name` field in the feed to the `name` attribute in Magento.
- **Schedule**:
    
    - Set up a cron job to automate the import process.
    - Define how frequently the feed should be imported.
- **Run Import**:
    
    - Manually run the import to test the configuration.
    - Ensure that the data is correctly imported and mapped.

  When you see the instruction "limit maximum number of documents allowed for a single file upload, batch upload will apply limit on each file separately," it means setting a restriction on the number of documents that can be included in a single file during an upload process. Additionally, when multiple files are uploaded in a batch, this limit will be applied to each file independently.

### Key Points:

1. **Maximum Number of Documents per File**:
    
    - Each file can only contain a certain number of documents. If a file exceeds this limit, the upload should be rejected or the extra documents should be ignored.
2. **Batch Upload**:
    
    - A batch upload involves uploading multiple files at once. The limit on the number of documents will be enforced separately for each file in the batch.

When you see the instruction "limit maximum number of documents allowed for a single file upload, batch upload will apply limit on each file separately," it means setting a restriction on the number of documents that can be included in a single file during an upload process. Additionally, when multiple files are uploaded in a batch, this limit will be applied to each file independently.


When you see "total size of a document allowed in MB," it means that there is a restriction on the maximum file size that can be uploaded, measured in megabytes (MB). If a file exceeds this size limit, the upload will be rejected.


Total Number of Fields Allowed in a Document:

**Definition:**

- The "total number of fields allowed in a document" refers to the maximum number of individual data fields that a single document (feed item) can contain. If a document exceeds this number, the upload will be rejected.


"number of variants in a doc for search type variants" refers to the number of different versions or configurations of a single product that can be included in a single document. Variants typically represent different options for a product, such as size, color, or material.