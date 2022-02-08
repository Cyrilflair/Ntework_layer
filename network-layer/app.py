#!/usr/bin/env python3

from aws_cdk import App

from cdk_vpc.cdk_vpc_stack import CdkVpcStack

app = App()

vpc_stack = CdkVpcStack(app, "cdk-vpc")

app.synth()
