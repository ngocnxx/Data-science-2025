from diagrams import Diagram
from diagrams.programming.framework import React
from diagrams.aws.compute import Fargate, ApplicationAutoScaling, Lambda
from diagrams.aws.database import Aurora
from diagrams.aws.network import ELB, CloudFront
from diagrams.aws.security import WAF, Cognito
from diagrams.aws.mobile import APIGateway


with Diagram(
    'GraphQL Handler',
    direction='LR',
    show=False,
    filename='../content/assets/graphql-lambda',
):
    APIGateway('DataHub API ') >> Lambda('Authorizer') >> Lambda('API Handler')
