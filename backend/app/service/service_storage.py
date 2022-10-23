import boto3
from fastapi import UploadFile

from core.settings import s3_settings, security_settings


class ServiceStorage:
    def __init__(self):
        _session = boto3.session.Session(
            aws_access_key_id=security_settings.yc_access_key,
            aws_secret_access_key=security_settings.yc_secret_key,
        )
        self._s3_client = _session.client(
            service_name="s3", endpoint_url=s3_settings.endpoint
        )

    def safe_weights_file(self, file: UploadFile):
        self._s3_client.put_object(
            Body=file.file, Key=file.filename, Bucket=s3_settings.bucket_name
        )
