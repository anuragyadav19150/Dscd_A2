import grpc 
import registry_pb2
import registry_pb2_grpc
import random
from concurrent import futures
import os
import sys

class RegisterServer(registry_pb2_grpc.RegisterServicer):

    def registerServer(self,request,context):
        print('JOIN REQUEST FROM ',request.server.ip,":",request.server.port)
       
        ip=request.server.ip
        port=request.server.port
        name=request.server.name

        if len(registry_server.servers)==N:
            return registry_pb2.registerServerResponse(response='Failure: Only N Replica allowed')

               


        for i in range(len(registry_server.servers)):
            if name==registry_server.servers[i].name:
                return registry_pb2.registerServerResponse(response='Failure: Name already taken')
        


        for i in range(len(registry_server.servers)):
            if port==registry_server.servers[i].port:
                return registry_pb2.registerServerResponse(response='Failure: One Replica is already running on this port')

        server=registry_server.servers.add()
        server.name=request.server.name
        server.ip=request.server.ip
        server.port=request.server.port

        folder_name='replica_'+request.server.port
        path='./'+folder_name
        
        if os.path.exists(folder_name):
            # print("hiii")
            for root, dirs, files in os.walk(path):
                # print("hii1")
                for file in files:
                    fpath = os.path.join(path, file)
                    os.remove(fpath)
            # os.rmdir(folder_name)
            # print(f"Deleted folder '{folder_name}'")
        else:
            os.mkdir(path) 


        

        return registry_pb2.registerServerResponse(response='Success')




    def GetServerList(self,request,context):
        
        if request.client=='read':
            print('Server List Request for Read Quorum (N_R server list)')
            listServer=[]
            for i in range(len(registry_server.servers)):
                listServer.append(i)
                

            listServer.sort()
            finalList = random.sample(listServer, registry_server.N_r)
            finalList.sort()
            listIndex=0
            client_server=registry_pb2.ClientResponse()
            for i in range(len(registry_server.servers)):
                if i==finalList[listIndex]:
                    listIndex+=1
                    serverList=client_server.serverclient.add()
                    serverList.name=registry_server.servers[i].name
                    serverList.ip=registry_server.servers[i].ip
                    serverList.port=registry_server.servers[i].port

                    print(f"name {serverList.name} , ip {serverList.ip} , port {serverList.port}")

                if listIndex>=len(finalList):
                    break
            # print(client_server.serverclient)
            return registry_pb2.ClientResponse(serverclient=client_server.serverclient)

        elif request.client=='write':
            print('Server List Request for Write Quorum (N_W server list)')
            listServer=[]
            for i in range(len(registry_server.servers)):
                listServer.append(i)
                

            listServer.sort()
            finalList = random.sample(listServer, registry_server.N_w)
            finalList.sort()
            # print(finalList,"final list for N_W ",registry_server.N_w)

            listIndex=0
            client_server=registry_pb2.ClientResponse()
            for i in range(len(registry_server.servers)):
                if i==finalList[listIndex]:
                    listIndex+=1
                    serverList=client_server.serverclient.add()
                    serverList.name=registry_server.servers[i].name
                    serverList.ip=registry_server.servers[i].ip
                    serverList.port=registry_server.servers[i].port

                    print(f"name {serverList.name} , ip {serverList.ip} , port {serverList.port}")

                if listIndex>=len(finalList):
                    break
            # print(client_server.serverclient)
            return registry_pb2.ClientResponse(serverclient=client_server.serverclient)

                    

        elif request.client=='delete':
            print('Server List Request for Write Quorum (N_W server list)')
            listServer=[]
            for i in range(len(registry_server.servers)):
                listServer.append(i)
                

            listServer.sort()
            finalList = random.sample(listServer, registry_server.N_w)
            finalList.sort()
            listIndex=0
            client_server=registry_pb2.ClientResponse()
            for i in range(len(registry_server.servers)):
                if i==finalList[listIndex]:
                    listIndex+=1
                    serverList=client_server.serverclient.add()
                    serverList.name=registry_server.servers[i].name
                    serverList.ip=registry_server.servers[i].ip
                    serverList.port=registry_server.servers[i].port

                    print(f"name {serverList.name} , ip {serverList.ip} , port {serverList.port}")
                if listIndex>=len(finalList):
                    break

            # print(client_server.serverclient)
            return registry_pb2.ClientResponse(serverclient=client_server.serverclient)

        elif request.client=='all':
            print('All Server List Request (N server list)')
            client_server=registry_pb2.ClientResponse()
            for i in range(len(registry_server.servers)):
                serverList=client_server.serverclient.add()
                serverList.name=registry_server.servers[i].name
                serverList.ip=registry_server.servers[i].ip
                serverList.port=registry_server.servers[i].port
                print(f"name {serverList.name} , ip {serverList.ip} , add {serverList.port}")

        



            return registry_pb2.ClientResponse(serverclient=client_server.serverclient)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    registry_pb2_grpc.add_RegisterServicer_to_server(RegisterServer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':

    registry_server=registry_pb2.RegistryServer()
    Nr=0
    Nw=0
    N=0
    check=True
    index=1
    # choice = int(sys.argv[arg_index])
        # arg_index+=1
    print(sys.argv[1:])
    while check:
        print("No. of Replicas :- ",end="")
        N = int(sys.argv[index])
        index+=1
        print(N)
        print("No. of Read Quorum :- ",end="")
        Nr = int(sys.argv[index])
        index+=1
        print(Nr)
        print("No. of Write Quorum :- ",end="")
        Nw = int(sys.argv[index])
        index+=1
        print(Nw)

        if Nw > N/2 and Nr > (N-Nw) :
            check=False

        if check:
            print("Given Input for Nr , Nw and N does not satisfy the condition please give Valid input ")
        
            
    registry_server.N_r=Nr
    registry_server.N_w=Nw
    registry_server.N=N

    serve()



