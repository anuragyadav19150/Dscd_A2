import grpc 
import registry_pb2
import registry_pb2_grpc
import client_pb2
import client_pb2_grpc
import server_pb2
import server_pb2_grpc
from concurrent import futures
import uuid
import time
import sys

args = sys.argv[1:]
print(args)
def Interact():
    cnt=0
    while(True):
        print()

        print("1. Write")
        print("2. Read ")
        print("3. Delete")
        print("4. Exit")

        # arg=int(input("Choose one of the above options : "))
        arg=int(args[cnt])
        cnt+=1
        if arg==1:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = registry_pb2_grpc.RegisterStub(channel)
                response = stub.GetReplicaList(registry_pb2.ClientRequest(uuid=client.uuid))
                print("List of all available replicas : ")
                i=0
                for value in response.addresses:
                    print(i+1,end=" ")
                    print(". "+value.ip+":"+value.port)
                    i+=1
                
                # serverJoin=int(input("Enter index to connect or press 0 to exit: "))
                serverJoin=int(args[cnt])
                cnt+=1

                with grpc.insecure_channel('localhost:'+response.addresses[serverJoin-1].port) as channelServer:

                    serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
                    # filename=input("Enter the name of file : ")
                    # content=input("Enter content of file : ")
                    # uuid=input("Enter uuid: ")
                    filename=args[cnt]
                    cnt+=1
                    content=args[cnt]
                    cnt+=1
                    uuid=args[cnt]
                    cnt+=1

                    Response = serverStub.Write(server_pb2.WriteRequest(name=filename,content=content,uuid=uuid))

                    print()
                    print('--------------------------------------')
                    print("Write Result: ")
                    print('Status: ',Response.status)
                    print('UUID:',Response.uuid)
                    print('Version:',Response.timestamp)
                    print('--------------------------------------')
        
        elif arg==2:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = registry_pb2_grpc.RegisterStub(channel)
                response = stub.GetReplicaList(registry_pb2.ClientRequest(uuid=client.uuid))
                print("List of all available replicas : ")
                i=0
                for value in response.addresses:
                    print(i+1,end=" ")
                    print(". "+value.ip+":"+value.port)
                    i+=1
                
                # serverJoin=int(input("Enter index to connect or press 0 to exit: "))
                serverJoin=int(args[cnt])
                cnt+=1

                with grpc.insecure_channel('localhost:'+response.addresses[serverJoin-1].port) as channelServer:

                    serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
    
                    # uuid=input("Enter uuid: ")
                    uuid=args[cnt]
                    cnt+=1

                    Response = serverStub.Read(server_pb2.ReadRequest(uuid=uuid))

                    print()
                    print('--------------------------------------')
                    print("Read Result: ")
                    print('Status: ',Response.status)
                    print('Name:',Response.name)
                    print('Content:',Response.content)
                    print('Version:',Response.timestamp)
                    print('--------------------------------------')
        
        elif arg==3:
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = registry_pb2_grpc.RegisterStub(channel)
                response = stub.GetReplicaList(registry_pb2.ClientRequest(uuid=client.uuid))
                print("List of all available replicas : ")
                i=0
                for value in response.addresses:
                    print(i+1,end=" ")
                    print(". "+value.ip+":"+value.port)
                    i+=1
                
                # serverJoin=int(input("Enter index to connect or press 0 to exit: "))
                serverJoin=int(args[cnt])
                cnt+=1

                with grpc.insecure_channel('localhost:'+response.addresses[serverJoin-1].port) as channelServer:

                    serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
    
                    # uuid=input("Enter uuid: ")
                    uuid=args[cnt]
                    cnt+=1

                    Response = serverStub.Delete(server_pb2.DeleteRequest(uuid=uuid))

                    print()
                    print('--------------------------------------')
                    print("Delete Result: ")
                    print('Status: ',Response.status)
                    print('--------------------------------------')
        
        else:
            break

        

if __name__ == '__main__':
    client=client_pb2.Client()
    client.uuid=str(uuid.uuid1())
    print('Client uuid:',client.uuid)
    Interact()