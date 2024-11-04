import boto3
import base64

def lambda_handler(event, context):
    # Entrada
    bucket = event['body']['bucket']
    nombre_archivo = event['body']['nombre_archivo']
    contenido_archivo = base64.b64decode(event['body']['contenido_archivo'])

    # Proceso
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=nombre_archivo, Body=contenido_archivo)

    # Salida
    return {
        'statusCode': 200,
        'message': f'Archivo {nombre_archivo} subido exitosamente al bucket {bucket}'
    }
