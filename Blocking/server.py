import grpc 
import registry_pb2
import registry_pb2_grpc
import server_pb2
import server_pb2_grpc
from concurrent import futures
import time
import os
from datetime import datetime
def callback(future):
    response=future.result()
    print(response)


def Write_helper(request,temp):
    print()
    flag=0
    flag1=0
    ind=-1
    for i in range(len(replica.data_store)):
        if request.uuid==replica.data_store[i].uuid:
            ind=i
            flag=1
            if request.name==replica.data_store[i].filename:
                flag1=1
            break
        elif request.name==replica.data_store[i].filename:
            return {'status':"Fail",'message':"File with same name exist"}
    
    timestamp=''

    if flag==0:
        file_path = os.path.join(replica.directory,request.name)
        with open(file_path, 'w') as f:
            f.write(request.content)
            f.close()
        obj=replica.data_store.add()
        obj.uuid=request.uuid
        obj.filename=request.name
        if temp:
            obj.timestamp=request.timestamp
        else:
            obj.timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        timestamp=obj.timestamp

    
    else:
        if flag1:
            file_path = os.path.join(replica.directory,request.name)
            with open(file_path, 'w') as f:
                f.write(request.content)
                f.close()
            if temp:
                replica.data_store[i].timestamp=request.timestamp
            else:
                replica.data_store[i].timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            timestamp=replica.data_store[i].timestamp
        else:
            return {'status':"Fail",'message':"Deleted file cannot be updated"}
    
    return {'status':"Success",'timestamp':timestamp}


def Delete_Helper(request,isPrimary):
    for i in range(len(replica.data_store)):
        if request.uuid==replica.data_store[i].uuid:
            if len(replica.data_store[i].filename)!=0:
                os.remove(os.path.join(replica.directory,replica.data_store[i].filename))
                replica.data_store[i].filename=''
                if not isPrimary:
                    replica.data_store[i].timestamp=request.timestamp
                else:
                    replica.data_store[i].timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                return {'status':'Success','timestamp':replica.data_store[i].timestamp}

                

            else:
                return {'status':'Fail','message': 'File already deleted'}
    
    return {'status':'Fail','message': 'File does not Exist'}
        



class Server(server_pb2_grpc.Server_serviceServicer):

    def newReplica(self, request, context):
        print('New replica added with address ',request.address.ip,':',request.address.port)
        rep=replica.backup_replicas.add()
        rep.ip=request.address.ip
        rep.port=request.address.port
        return server_pb2.newReplicaResponse(status='True')
    
    def WriteRequestToBackup(self, request, context):
        print('Received write req from primary replica: ')
        time.sleep(5)
        response=Write_helper(request,1)

        return server_pb2.WriteAcknowledgement(status=response['status'])

    

    def WriteRequestToPrimary(self, request, context):
        print('Received write req from backup replica: ')

        
        res=Write_helper(request,0)
        

        if res['status']=='Fail':
            return server_pb2.WriteResponse(status=res['status']+'! '+res['message'])

        for i in range(len(replica.backup_replicas)):
                channel = grpc.insecure_channel('localhost:'+replica.backup_replicas[i].port)
                stub = server_pb2_grpc.Server_serviceStub(channel)
                response=stub.WriteRequestToBackup(server_pb2.BackupWriteRequest(name=request.name,uuid=request.uuid,content=request.content,timestamp=res['timestamp']))
                print(response)


        print('Write done in all the backup replicas')

        return server_pb2.WriteResponse(status='Success',timestamp=res['timestamp'],uuid=request.uuid)

    
    def Write(self, request, context):
        print('Received write req from client: ')
        if not replica.HasField('p_address'):
            flag=0
            flag1=0
            ind=-1
            for i in range(len(replica.data_store)):
                if request.uuid==replica.data_store[i].uuid:
                    ind=i
                    flag=1
                    if request.name==replica.data_store[i].filename:
                        flag1=1
                    break
                elif request.name==replica.data_store[i].filename:
                    return server_pb2.WriteResponse(status='Fail! File with same name exist')
            
            timestamp=''

            if flag==0:
                file_path = os.path.join(replica.directory,request.name)
                with open(file_path, 'w') as f:
                    f.write(request.content)
                    f.close()
                obj=replica.data_store.add()
                obj.uuid=request.uuid
                obj.filename=request.name
                obj.timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                timestamp=obj.timestamp

            
            else:
                if flag1:
                    file_path = os.path.join(replica.directory,request.name)
                    with open(file_path, 'w') as f:
                        f.write(request.content)
                        f.close()
                    replica.data_store[i].timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    timestamp=replica.data_store[i].timestamp
                else:
                    return server_pb2.WriteResponse(status='Fail! Deleted file cannot be updated')

        
            for i in range(len(replica.backup_replicas)):
                channel = grpc.insecure_channel('localhost:'+replica.backup_replicas[i].port)
                stub = server_pb2_grpc.Server_serviceStub(channel)
                response=stub.WriteRequestToBackup(server_pb2.BackupWriteRequest(name=request.name,uuid=request.uuid,content=request.content,timestamp=timestamp))
                print(response)



            return server_pb2.WriteResponse(status='Success',timestamp=timestamp,uuid=request.uuid)


        else:
            channel = grpc.insecure_channel('localhost:'+replica.p_address.port)
            stub = server_pb2_grpc.Server_serviceStub(channel)
            response=stub.WriteRequestToPrimary(request)
            return response

    

    def Read(self, request, context):
        print('Received read req from client: ')

        for i in range(len(replica.data_store)):
            if request.uuid==replica.data_store[i].uuid:
                if len(replica.data_store[i].filename)!=0:
                    f=open(os.path.join(replica.directory,replica.data_store[i].filename),'r')
                    content=f.read()
                    f.close()
                    return server_pb2.ReadResponse(status='Success',name=replica.data_store[i].filename,content=content,timestamp=replica.data_store[i].timestamp)
                else:
                    return server_pb2.ReadResponse(status='File Already Deleted',name='NULL',content='NULL',timestamp=replica.data_store[i].timestamp)
            


        return server_pb2.ReadResponse(status='File Does not exist',name='NULL',content='NULL',timestamp='NULL')



    def Delete(self, request, context):
        print('Received delete req from client: ')

        if not replica.HasField('p_address'):
            result=Delete_Helper(request,1)
    
            if result['status']=='Fail':
                return server_pb2.DeleteResponse(status=result['status']+'! '+result['message'])

            for i in range(len(replica.backup_replicas)):
                channel = grpc.insecure_channel('localhost:'+replica.backup_replicas[i].port)
                stub = server_pb2_grpc.Server_serviceStub(channel)
                response=stub.DeleteRequestToBackup(server_pb2.BackupDeleteRequest(uuid=request.uuid,timestamp=result['timestamp']))
                print(response)
            

            return server_pb2.DeleteResponse(status='Success')
        
        else:
            channel = grpc.insecure_channel('localhost:'+replica.p_address.port)
            stub = server_pb2_grpc.Server_serviceStub(channel)
            response=stub.DeleteRequestToPrimary(request)
            print('Response from primary: ')
            print(response)
            return response

    
    def DeleteRequestToPrimary(self, request, context):
        print('Received delete req from backup replica: ')

        
        result=Delete_Helper(request,1)

        if result['status']=='Fail':
            return server_pb2.DeleteResponse(status=result['status']+'! '+result['message'])

        for i in range(len(replica.backup_replicas)):
            channel = grpc.insecure_channel('localhost:'+replica.backup_replicas[i].port)
            stub = server_pb2_grpc.Server_serviceStub(channel)
            response=stub.DeleteRequestToBackup(server_pb2.BackupDeleteRequest(uuid=request.uuid,timestamp=result['timestamp']))
            print(response)

        return server_pb2.DeleteResponse(status='Success')


    def DeleteRequestToBackup(self, request, context):
        print('Received delete req from primary replica: ')

        response=Delete_Helper(request,0)

        print('Delete done in Backup')

        return server_pb2.DeleteAcknowledgement(status=response['status'])



        

        

def regiterToRegistryServer():
    print('Registering to registry server...')
    channel = grpc.insecure_channel('localhost:50051')
    stub = registry_pb2_grpc.RegisterStub(channel)
    response = stub.registerReplica(registry_pb2.registerReplicaRequest(address=replica.address))
    print("Response from regitry server:",response.status)
    if response.status=='Success':
        if response.HasField('paddress')==True:
            replica.p_address.ip=response.paddress.ip
            replica.p_address.port=response.paddress.port

        return True
    
    return False
    

if __name__ == '__main__':
    name = input("Enter Name of server : ")
    portNo = input("Enter Port no : ")
    replica=server_pb2.Replica()
    replica.name=name
    replica.address.ip='127:0:0:1'
    replica.address.port=portNo

    if regiterToRegistryServer():

        try:
            current_dir = os.getcwd()
            replica.directory=current_dir+'/files/replica_'+str(portNo)+'/'
            new_dir_path = os.path.join(current_dir, 'files/replica_'+str(portNo)+'/')
            os.makedirs(new_dir_path)
        
        except:
            print()
        
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        server_pb2_grpc.add_Server_serviceServicer_to_server(Server(),server)
        server.add_insecure_port('[::]:' + portNo)
        server.start() 
        print("Server started, listening on " + portNo)
        server.wait_for_termination()

