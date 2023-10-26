def implicit():
    from google.cloud import storage
    torage_client = storage.Client.from_service_account_json('mykey.json')
    

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    project = 'data-rainfall-396303'
    storage_client = storage.Client(project=project)

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)
implicit()

