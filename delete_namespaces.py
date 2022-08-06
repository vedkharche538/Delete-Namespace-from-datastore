def delete_namespace(project_id, location_id, namespace_id):
    """Deletes a namespace in the given location."""

    client = servicedirectory_v1.RegistrationServiceClient()

    namespace_name = client.namespace_path(
        project_id, location_id, namespace_id)

    client.delete_namespace(name=namespace_name)

    print(f'Deleted namespace {namespace_name}.')


delete_namespace('project_id', 'region', 'namespace')
