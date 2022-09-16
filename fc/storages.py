from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = "cww-"
    location = "static"
    querystring_auth = False

    def _normalize_name(self, name):
        """
        Get rid of this crap: http://stackoverflow.com/questions/12535123/django-storages-and-amazon-s3-suspiciousoperation
        """
        if name[:1] == "/":
            name = name[1:]
        # name = name[1:]
        return name
