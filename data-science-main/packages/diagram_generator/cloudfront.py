from diagrams import Diagram
from diagrams.programming.framework import React
from diagrams.onprem.client import Client
from diagrams.aws.compute import Fargate, ApplicationAutoScaling
from diagrams.aws.storage import S3
from diagrams.aws.database import Aurora
from diagrams.aws.network import ELB, CloudFront
from diagrams.aws.mobile import APIGateway


with Diagram('Frontend', show=False, filename='../content/assets/cloudfront'):
    distro = CloudFront('DataHub')
    content = S3('Static')
    client = Client('Browser')
    app = React('UI')
    client >> distro
    distro >> content
    app >> client
