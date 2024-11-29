import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    alumno_datos = event['body']['alumno_datos']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    # Actualiza el registro en DynamoDB
    update_expression = "SET " + ", ".join(f"{k} = :{k}" for k in alumno_datos.keys())
    expression_attribute_values = {f":{k}": v for k, v in alumno_datos.items()}
    
    response = table.update_item(
        Key={'tenant_id': tenant_id, 'alumno_id': alumno_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="UPDATED_NEW"
    )
    
    # Salida (json)
    return {
        'statusCode': 200,
        'updated_attributes': response['Attributes']
    }
