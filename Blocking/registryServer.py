import grpc
import registry_pb2
import registry_pb2_grpc
import server_pb2
import server_pb2_grpc
from concurrent import futures

class RegisterServer(registry_pb2_grpc.RegisterServicer):

    def registerReplica(self, request, context):
        ip=request.address.ip
        port=request.address.port
        print('JOIN REQUEST FROM ',request.address.ip,":",request.address.port)

        for i in range(len(registry_server.replicas)):
            if ip==registry_server.replicas[i].ip and port==registry_server.replicas[i].port:
                return registry_pb2.registerReplicaResponse(status='Fail! Replica with same address already exist!')

        rep_address=registry_server.replicas.add()
        rep_address.ip=request.address.ip
        rep_address.port=request.address.port

        # print('check0')
        if registry_server.HasField('p_address')==True:
            # print('check1')
            with grpc.insecure_channel('localhost:'+registry_server.p_address.port) as channelServer:
                serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
                # print('check2')
                Response = serverStub.newReplica(server_pb2.newReplicaRequest(address=request.address))
                # print(Response)


        # print('check3')
        if registry_server.HasField('p_address')==False:
            print('Assigning replica with address ',ip,':',port,"as primary")
            registry_server.p_address.ip=ip
            registry_server.p_address.port=port
            return registry_pb2.registerReplicaResponse(status='Success')

        else:
            return registry_pb2.registerReplicaResponse(status='Success',paddress=registry_server.p_address)
        

        

        

    def GetReplicaList(self, request, context):
        print('SERVER LIST REQUEST FROM ',request.uuid)

        response=registry_pb2.ClientResponse()

        for i in range(len(registry_server.replicas)):
            rep=response.addresses.add()
            rep.ip=registry_server.replicas[i].ip
            rep.port=registry_server.replicas[i].port
        
        response.status='True'

        return response

        



def serve():
    port='50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    registry_pb2_grpc.add_RegisterServicer_to_server(RegisterServer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()



if __name__ == '__main__':
    registry_server=registry_pb2.RegistryServer()
    serve()
