import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB resource and table
dynamodb = boto3.resource('dsynamodb')
table = dynamodb.Table('StudentRecords')

def lambda_handler(event, context):
    # Log the received event for debugging
    print("Received event:", json.dumps(event, indent=2))
    
    # Check if the event is None or empty
    if not event:
        return {
            'statusCode': 400,
            'body': json.dumps('No event data received')
        }
    
    # Extract the HTTP method from the event
    http_method = event.get('method')
    
    try:
        if http_method == 'POST':
            # Create a new student record
            student = json.loads(event.get('body', '{}'))
            if 'student_id' not in student:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Missing student_id in request body')
                }
            table.put_item(Item=student)
            return {
                'statusCode': 200,
                'body': json.dumps('Student record added successfully')
            }

        elif http_method == 'GET':
            # Fetch student record by student_id
            student_id = event.get('query', {}).get('student_id')
            if not student_id:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Missing student_id query parameter')
                }
            response = table.get_item(Key={'student_id': student_id})
            if 'Item' in response:
                return {
                    'statusCode': 200,
                    'body': json.dumps(response['Item'])
                }
            return {
                'statusCode': 404,
                'body': json.dumps('Student record not found')
            }

        elif http_method == 'PUT':
            # Update an existing student record
            student = json.loads(event.get('body', '{}'))
            if 'student_id' not in student:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Missing student_id in request body')
                }
            table.update_item(
                Key={'student_id': student['student_id']},
                UpdateExpression="set #n = :n, course = :c",
                ExpressionAttributeNames={'#n': 'name'},
                ExpressionAttributeValues={
                    ':n': student['name'],
                    ':c': student['course']
                },
                ReturnValues="UPDATED_NEW"
            )
            return {
                'statusCode': 200,
                'body': json.dumps('Student record updated successfully')
            }

        elif http_method == 'DELETE':
            # Remove a student record by student_id
            student_id = event.get('query', {}).get('student_id')
            if not student_id:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Missing student_id query parameter')
                }
            table.delete_item(Key={'student_id': student_id})
            return {
                'statusCode': 200,
                'body': json.dumps('Student record deleted successfully')
            }

        else:
            return {
                'statusCode': 405,
                'body': json.dumps('Method not allowed')
            }

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Internal Server Error: {e.response["Error"]["Message"]}')
        }
