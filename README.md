CMPE272 Assignment 2
=======
# Assignment 2 : Building Serverless Application
## Author : Pratikkumar Dalsukhbhai Korat
### SJSU ID : 017512508

* This project utilizes the Amazon Web Services to build serverless application which perform the CRUD operations on DynamoDB

## Technologies Used in this Application
> 1. Amazon Web Services
> 2. Python (for Lambda Function)
> 3. AWS Dynamodb

## Steps

### Step 1 : Setting up Dynamo Database
> 1. Go to AWS management console and open Dynamodb and Create a table named "StudentRecords".
> 2. Mention the primary key as "student_id" and it should be string.
> ![img.png](images/dynamodb.png)

### Step 2 : Setting up IAM role
> 1. Go to Identity Access Management and Create a user role which has full access to DynamoDB
> ![img.png](images/IAM_Lamdba.png)
> ![img.png](images/IAM_Lambda2.png)

### Step 3 : Setting up Lambda Function
> 1. Go to AWS Lambda console and create a new function and give a name StudentRecordHandler
> 2. Chose appropriate runtime, in this project, I am going to utilize Python 3.9 Runtime
> ![img.png](images/lambda1.png)
> 3. Attach the appropriate user role to allow read and write of DynamoDB.
> ![img.png](images/lambda2.png)
>
> 4. Copy and Paste code written in lambda.py to lambda function
> 5. Click on Deploy
> 6. Configure the Test Event for basic testing
>    1. test_post event
>       * Paste the following JSON to test configuration window
>         * ```{"method": "POST", "body": "{\"student_id\": \"11\", \"name\": \"Pratik Korat\", \"course\": \"Computer Science\"}"}```
>       * Result
>       ![img.png](images/test_post.png)
>    2. test_get event
>       * Paste the following JSON to test configuration window
>         *  ``` { "method": "GET", "query": { "student_id": "1"}} ```
>       * Result
>       ![img.png](images/test_get.png)
>    3. test_delete event
>       * Paste the following JSON to test configuration window
>         *  ``` {"method": "DELETE", "query": {"student_id": "11"}} ```
>       * Result
>       ![img.png](images/test_delete.png)
>    4. test_update event
>       * Paste the following JSON to test configuration window
>         *  ``` {"method": "PUT", "body": "{\"student_id\": \"1\", \"name\": \"Pratik Updated\", \"course\": \"Data Science\"}"} ```
>       * Result
>       ![img.png](images/test_update.png)


### Step 4: Create an API Gateway
> 1. Go to AWS API Gateway control and click on Build for REST API.
>   ![img.png](images/api_gateway.png)
> 2. Create resource and name it "students"
> 3. Under resource student, Create a GET method
>    ![img.png](images/get_method.png)
>    1. Once GET method is created, then go to integration request, then go to mapping template, then click on edit and paste the content of "integration_template", then click on save.
>    ![img.png](images/integration_template.png)
>    2. Make sure it should look like this as shown in above picture.
> 4. Under resource student, Create a POST method
>    ![img.png](images/post_method.png)
>    1. Once POST method is created, then go to integration template, then go to mapping template, then click on edit and paste the content of "integration_template", then click on save.
>    ![img_1.png](images/integration_template.png)
>    2. Make sure it should look like this as shown in above picture.
> 5. Click on deploy API, chose appropriate deploy version


### Results
> 1. GET request
>    * POSTMAN
>      ![img.png](images/get_request_postman.png)
>    * AWS DynamoDB
>      ![img.png](images/dynamodb_get.png)
>

> 2. POST request
>    * POSTMAN
>       ![img.png](images/post_request_postman.png)
>    * AWS DynamoDB
>       ![img.png](dynamodb_post.png)


* Currently, this application supports both READ and WRITE operations on DynamoDB via a Lambda function through a REST API.

## Issues Faced
* During the development of this project, I encountered an issue with integrating a REST API with a Lambda function, specifically in parsing the request body in the Lambda function. To resolve this, I created a custom mapping template capable of handling both GET and POST requests.