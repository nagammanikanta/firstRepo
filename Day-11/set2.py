server_config = {
    'server1':{'ip':'192.168.1.0', 'port':'8080', 'status':'active'},
    'server2':{'ip':'192.168.1.1', 'port':'8081', 'status':'inactive'},
    'server3':{'ip':'192.168.1.3', 'port':'9000', 'status':'active'}
    
}
print(server_config)

def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'server not found')

server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
