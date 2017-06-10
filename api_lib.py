# -*- coding: utf-8 -*-

import boto3


def instance_create(region_name, image_id, min_count, max_count, key_name, instance_type):
    ec2 = boto3.resource('ec2', region_name=region_name)

    instances = ec2.create_instances(
        ImageId=image_id,
        MinCount=int(min_count),
        MaxCount=int(max_count),
        KeyName=key_name,
        InstanceType=instance_type
    )

    return instances


def instance_info(region_name):
    ec2 = boto3.resource('ec2', region_name=region_name)
    dados = []
    for instances in ec2.instances.all():
        dados.append({'id': instances.id, 'state': instances.state['Name']})

    return dados


def instance_terminate(region_name, instance_id):
    ec2 = boto3.resource('ec2', region_name=region_name)
    instance = ec2.Instance(instance_id)
    response = instance.terminate()

    return response

