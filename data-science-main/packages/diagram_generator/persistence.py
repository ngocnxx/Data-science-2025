from diagrams import Diagram
from diagrams.programming.framework import React
from diagrams.aws.compute import Fargate, ApplicationAutoScaling, Lambda
from diagrams.aws.database import Aurora
from diagrams.aws.network import ELB, CloudFront
from diagrams.aws.mobile import APIGateway


with Diagram('Persistence', show=False, direction='LR', filename='../content/assets/db'):
    [Lambda('GraphQL'), Lambda('Async Task Runner')] >> Aurora('Shared State ')
