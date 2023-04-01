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

def Interact():

    while(True):
        print("1. Write")
        print("2. Read ")
        print("3. Delete")
        print("4. Exit")

        arg=int(input("Choose one of the above options : "))

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
                
                serverJoin=int(input("Enter index to connect or press 0 to exit: "))

                with grpc.insecure_channel('localhost:'+response.addresses[serverJoin-1].port) as channelServer:

                    serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
                    filename=input("Enter the name of file : ")
                    content=input("Enter content of file : ")
                    uuid=input("Enter uuid: ")

                    Response = serverStub.Write(server_pb2.WriteRequest(name=filename,content=content,uuid=uuid))

                    print()
                    print("Result: ")
                    print('Status: ',Response.status)
                    print('UUID:',Response.uuid)
                    print('Version:',Response.timestamp)
        
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
                
                serverJoin=int(input("Enter index to connect or press 0 to exit: "))

                with grpc.insecure_channel('localhost:'+response.addresses[serverJoin-1].port) as channelServer:

                    serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
    
                    uuid=input("Enter uuid: ")

                    Response = serverStub.Read(server_pb2.ReadRequest(uuid=uuid))

                    print()
                    print("Result: ")
                    print('Status: ',Response.status)
                    print('Name:',Response.name)
                    print('Content:',Response.content)
                    print('Version:',Response.timestamp)
        
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
                
                serverJoin=int(input("Enter index to connect or press 0 to exit: "))

                with grpc.insecure_channel('localhost:'+response.addresses[serverJoin-1].port) as channelServer:

                    serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
    
                    uuid=input("Enter uuid: ")

                    Response = serverStub.Delete(server_pb2.DeleteRequest(uuid=uuid))

                    print()
                    print("Result: ")
                    print('Status: ',Response.status)
        
        else:
            break




    # print('Getting all the replicas from registry server: ')
    # print()

    # with grpc.insecure_channel('localhost:50051') as channel:
    #     stub = registry_pb2_grpc.RegisterStub(channel)
    #     response = stub.GetReplicaList(registry_pb2.ClientRequest(uuid=client.uuid))
    #     print("List of all available replicas : ")
    #     i=0
    #     for value in response.addresses:
    #         print(i+1,end=" ")
    #         print(". "+value.ip+":"+value.port)
    #         i+=1
        
    #     serverJoin=int(input("Enter index to connect or press 0 to exit: "))

    #     with grpc.insecure_channel('localhost:'+response.addresses[serverJoin-1].port) as channelServer:
    #         serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
    #         Response = serverStub.Write(server_pb2.WriteRequest(name='Test',content='This is my first write111',uuid='uuid'))
    #         print("Results for your activity : ")
    #         print(Response)
    #         time.sleep(10)
    #         print('Now deleteing file: ')
            
    #         Response=serverStub.Delete(server_pb2.DeleteRequest(uuid='uuid'))
    #         print(Response)
        




if __name__ == '__main__':
    client=client_pb2.Client()
    client.uuid=str(uuid.uuid1())
    print('Client uuid:',client.uuid)
    Interact()