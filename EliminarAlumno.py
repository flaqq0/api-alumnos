import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    # Elimina el registro de la tabla
    response = table.delete_item(
        Key={'tenant_id': tenant_id, 'alumno_id': alumno_id}
    )
    
    # Salida (json)
    return {
        'statusCode': 200,
        'message': 'Alumno eliminado correctamente'
    }
