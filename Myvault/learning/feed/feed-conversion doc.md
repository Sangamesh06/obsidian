
both feed and indexed are on unbxd sdk platform
**Feature field mapping** involves the assignment of specific attributes or properties in a customer feed to predefined features within the Unbxd platform. This ensures that the data is correctly interpreted and utilized by the system.

### Advanced Functionality of the Unbxd SDK: Field Mapping Explained

The Unbxd SDK provides advanced functionality for mapping fields in customer feeds, making the process efficient and precise. Here, we'll break down the concepts of feature field mapping and schema field mapping, and provide an example to illustrate their application.

#### Feature Field Mapping

**Feature field mapping** involves the assignment of specific attributes or properties in a customer feed to predefined features within the Unbxd platform. This ensures that the data is correctly interpreted and utilized by the system.

For example, let's say you have a product feed with the following fields:

- `product_name`
- `product_price`
- `product_color`
- `product_size`

In feature field mapping, you might map these fields to Unbxd's predefined features like:

- `product_name` → `title`
- `product_price` → `price`
- `product_color` → `color`
- `product_size` → `size`

**Schema field mapping** involves defining the structure (schema) of the data in a way that ensures all necessary fields are included and correctly formatted. This is crucial for the accurate generation of the schema for a customer’s feed.

onsider a customer feed that includes both required and optional fields. Required fields might be:

- `title`
- `price`

Optional fields might be:

- `color`
- `size`

feature_mapping = {
    "productName": "title",
    "cost": "price",
    "shade": "color",
    "dimensions": "size"
}


schema = {
    "title": {"type": "string", "required": True},
    "price": {"type": "number", "required": True},
    "color": {"type": "string", "required": False},
    "size": {"type": "string", "required": False}
}





The Unbxd SDK provides several advanced functionalities designed to significantly enhance the customer experience on e-commerce websites. These functionalities include optimized efficiency, performance enhancement, and enhanced schema generation. Here's how each functionality contributes to improving the customer experience:

#### 1. Optimized Efficiency

The Unbxd SDK optimizes the process of uploading customer feeds by utilizing a database for storing customer data and integrating a multipart upload feature. This approach offers several benefits:

- **Reduced Upload Time**: By breaking down large files into smaller parts and uploading them simultaneously, the SDK minimizes the time needed to upload customer feeds to the Unbxd platform.
- **Smooth Customer Onboarding**: Faster upload times lead to quicker onboarding of customer feeds, allowing businesses to get their products online faster.

**Example**: If a large retail store wants to upload its entire product catalog, the multipart upload feature ensures that the upload is efficient and completed in a shorter time, enabling customers to see the latest products without delay.

#### 2. Performance Enhancement

The SDK ensures rapid data transfer and efficient indexing of customer feeds, which boosts the overall performance of the e-commerce website. Key aspects include:

- **Fast Data Processing**: The streamlined feed uploading process enables quick data transfer, which translates to faster updates on the website.
- **Efficient Indexing**: Efficient indexing means that the search and browse functionalities on the website are quicker and more accurate.

**Example**: A customer searching for "running shoes" on an e-commerce site will get accurate and relevant results quickly, enhancing their shopping experience.

#### 3. Enhanced Schema Generation

The SDK offers advanced functionality for field mapping, ensuring precise schema generation. This involves:

- **Feature Field Mapping**: Assigning specific attributes in a customer feed to predefined features within the Unbxd platform, ensuring correct data interpretation.
- **Schema Field Mapping**: Defining the structure of the data to include all necessary fields in the correct format.

**Example**: When a new product is added to the catalog, the SDK ensures that all necessary attributes (e.g., product name, price, color) are correctly mapped and displayed on the website. This ensures customers have all the information they need to make an informed purchase.

### Conclusion

The Unbxd SDK functionalities enhance the customer experience by:

- **Improving Efficiency**: Faster upload and processing times mean that customers see the most up-to-date products without delays.
- **Enhancing Performance**: Quick and accurate search results improve the shopping experience.
- **Ensuring Data Accuracy**: Proper schema generation ensures that product information is complete and correctly displayed, helping customers make informed decisions.

When we say that data or a feed is "routed" to a specific geographical region, we are referring to the process of directing the data to a designated location or server based on certain criteria, such as the location of the end user or the optimal server for processing that data. Routing is essentially the process of determining the path that data will take from its source to its destination.

### What Does "Routed" Mean in Different Contexts?

1. **Internet and Networking**:
    
    - **Routing** is the process of selecting paths in a network along which to send network traffic. Routers are devices that determine the best path for forwarding packets towards their destination. Routing decisions are made based on various algorithms and protocols.
## region
When we say that data or a feed is "routed" to a specific geographical region, we are referring to the process of directing the data to a designated location or server based on certain criteria, such as the location of the end user or the optimal server for processing that data.
## feed domain
The domain URL to which the feed data should be routed (set based on ‘region’ if None)
Let's consider an e-commerce platform that needs to upload product feeds to different servers based on the geographical region:

1. **Region-Specific URLs**:
    
    - **Europe**: `europe.example.com/feed`
    - **North America**: `na.example.com/feed`
    - **Asia**: `asia.example.com/feed`
2. **Routing Logic**:
    
    - If the data is from a European supplier, the system routes the feed to `europe.example.com/feed`.
## unbxd_is_incremental

An incremental feed flag is a setting that indicates whether the data being uploaded in the feed is an incremental update or a full dataset.

**Incremental Feed**:
To update only the changed or new records since the last data upload.

**Full Feed**:
**Purpose**: To upload the complete dataset, regardless of changes.


## process_inmemory
An in-memory processing flag is a setting that indicates whether the feed data should be processed entirely in memory.

**Key Points:**

1. **In-Memory Processing**:
    
    - **Purpose**: To perform data processing operations directly in the system's RAM (Random Access Memory) rather than using disk-based storage.
**Disk-Based Processing**:

- **Purpose**: To perform data processing operations by reading from and writing to disk storage.
-Consider an application that processes large customer feeds containing product data for an e-commerce platform. The data includes product details, prices, and stock levels. Here’s how the two types of processing might be used:

1. **In-Memory Processing**:
    
    - **Scenario**: Processing a moderate-sized feed of product data.
   **Disk-Based Processing**:

- **Scenario**: Processing a large feed of product data that cannot fit into memory.

## end points and domains
**Endpoints**:

- An endpoint is a specific URL path where an API or web service can be accessed.
- It is the address where requests are sent to interact with the service, retrieve data, submit data, or perform other operations.
**Domains**:

- A domain is the main address of a website or web service. It represents the network location of the service.
- It usually contains multiple endpoints that perform different functions under the same domain.
**Routing**: When you send a data feed to `http://feed.unbxd.io/`, the data is routed to the servers and services that handle feed processing in the US-East region.


When a customer wants to upload a feed, they would choose the appropriate endpoint based on their geographical region. For example, a customer in the UK would use `http://feed-uk.unbxd.io/` to ensure their data is processed efficiently within their region.

### Role of Each Concept in the Example:

- **Routing:** Ensures that the customer's data is directed efficiently from their location to Unbxd's servers, optimizing for speed and reliability.
    
- **Domain:** Provides a recognizable name (`unbxd.io`) for accessing Unbxd's services over the internet.
    
- **Endpoint:** Specifies the exact location (`http://feed-uk.unbxd.io/`) where the customer should send their data, ensuring it is processed within the UK region for compliance and performance reasons.
    
- **Geographical Region:** Determines the location-specific endpoint (`feed-uk.unbxd.io`), ensuring data compliance with local regulations and minimizing latency by processing data closer to where it is generated or needed.
    
- **Feed Upload by Customer:** Represents the action of the customer preparing and sending their product data to Unbxd for processing and integration.
    
- **Unbxd Services and Servers:** Handle the processing, validation, indexing, and integration of the customer's product data into their e-commerce platform.
    
- **Processing and Reflecting on Website:** Completes the cycle where the customer's newly uploaded product data becomes searchable and purchasable on their e-commerce website, facilitated by Unbxd's services.


### What is an API Key?

An API Key is a unique identifier assigned to a user, application, or service that grants access to an API (Application Programming Interface). It serves as a form of authentication to ensure that only authorized entities can interact with the API and its associated services.

### Role of the Unbxd API Key:

1. **Authentication:**
    
    - The primary purpose of the Unbxd API Key is to authenticate requests made to Unbxd's APIs. When a client (such as an e-commerce platform or application) wants to send requests to Unbxd for tasks like uploading product data, querying search results, or managing configurations, they must include their API Key in the request headers or parameters.
2. **Authorization:**
    
    - In addition to authentication, the API Key also plays a role in authorization. It determines the level of access and permissions granted to the client. For example, some API Keys may have read-only access, allowing clients to fetch data but not modify it, while others may have full access for managing data and configurations within Unbxd services.


### How the Unbxd API Key is Used:

- **Integration:** Clients integrate the Unbxd API Key into their application’s code or configuration files. This key is included with each API request as a header or parameter.
    
- **Secure Communication:** When a client sends a request to Unbxd’s API endpoints (e.g., for uploading product data or retrieving search results), the API Key serves as proof of identity and authorization. Unbxd verifies the API Key associated with each request to ensure it matches an authorized client and that the requested operation is permitted.
    
- **Access Control:** Through the API Key, Unbxd can enforce access control policies, restricting or allowing specific actions based on the privileges associated with each key. This ensures that clients only perform actions they are permitted to, based on their API Key’s permissions.


## unbxd site key

The Unbxd Site Key is a parameter used to uniquely identify the configuration and settings of a specific website or application within Unbxd's ecosystem. Here’s a detailed explanation of its role and significance:

### What is the Unbxd Site Key?

1. **Unique Identifier:**
    
    - The Unbxd Site Key serves as a unique identifier for a particular instance or configuration of Unbxd services associated with a website or application. It distinguishes one site's configuration from another within Unbxd’s platform.
2. **Configuration and Settings:**
    
    - Each Unbxd Site Key is linked to a specific set of configurations and settings that define how Unbxd’s services behave for that particular site. This includes settings related to search behavior, product catalog synchronization, merchandising rules, relevance settings, and more.
-
### How the Unbxd Secret Key is Used:

- **Secure Authentication:** When a client makes an API request to Unbxd, they typically include both the API Key and Secret Key in the request headers or parameters. Unbxd uses these keys to authenticate the request and determine the level of access granted to the client.




The term "partition_size" in the context of processing feed files likely refers to the batch size or the number of product records processed simultaneously. Here’s a detailed explanation:
**Definition:**

- **Partition Size** refers to the number of product records that are processed together in a single batch or chunk during feed processing.
- Let’s say you have a feed file containing 10,000 products to be processed. If the `partition_size` is set to 1,000, the processing will be divided into 10 batches, each containing 1,000 products.

- **Batch 1:** Process products 1 to 1,000
### The Field to Check for Multiple Files

1. **Definition:**
    - **Field to Check for Multiple Files** refers to a specific attribute or property within the feed files that the system uses to identify, differentiate, and manage the files during processing.
    - 