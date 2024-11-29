import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    # Busca el registro en la tabla
    response = table.get_item(
        Key={'tenant_id': tenant_id, 'alumno_id': alumno_id}
    )
    alumno = response.get('Item', {})
    
    # Salida (json)
    if not alumno:
        return {
            'statusCode': 404,
            'message': 'Alumno no encontrado'
        }
    
    return {
        'statusCode': 200,
        'alumno': alumno
    }
