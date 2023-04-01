import grpc 
import registry_pb2
import registry_pb2_grpc
import server_pb2
import server_pb2_grpc
from concurrent import futures
import uuid
from datetime import datetime
import sys 
import os

def getAllServers():
    # print("Generating uuid for a client")
    index=1

    while True:
        print()
        print("1. Write")
        print("2. Read ")
        print("3. Delete")
        print("4. All Replica")
        print("5. Exit")

        print()
        print("Choose one of the above options : ",end="")
        argument=int(sys.argv[index])
        index+=1
        print(argument)

        if argument==1:
            print("Inside write server List")
            with grpc.insecure_channel('localhost:50051') as channel:
                print("connect to registry server")
                stub = registry_pb2_grpc.RegisterStub(channel)
                response = stub.GetServerList(registry_pb2.ClientRequest(client='write'))
        
                # print(response)
               

                print("List of write quorum (N_w) : ")
                i=0
                for value in response.serverclient:
                    print(i+1,end=" ")
                    print(". "+value.name + " - "+ value.ip+":"+value.port)
                    i+=1

                print("Enter UID : ",end="")

                uid=sys.argv[index]
                index+=1
                print(uid)
                # updatevalue=int(input("Do you want to update or write , for update press 1 and write press 2 : "))

                # if updatevalue==2:
                #     uid=str(uuid.uuid1())

                print("Enter the name of file : ",end="")

                filename=sys.argv[index]
                index+=1
                print(filename)

                print("Enter content of file : ",end="")

                content=sys.argv[index]
                index+=1
                print(content)


                success_port=[]
                failure_port=[]
                temp_uid=""
                temp_uid_fail_update=""
                temp_uid_fail_filename=""
                temp_uid_fail_fileupd=""
                for value in response.serverclient:
                    with grpc.insecure_channel('localhost:'+value.port) as channelServer:
                        serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
                        serverResponse = serverStub.WriteServer(server_pb2.clientResponse(uid=uid,filename=filename,content=content))
                        # print("Status : ",serverResponse.status)
                        # print("UID : ",serverResponse.uid)
                        # print("Version : ",serverResponse.version)

                        print(f"Status: {serverResponse.status}, Uid: {serverResponse.uid}, Version: {serverResponse.version}")
                        

                        if serverResponse.status[0]=='S':
                            success_port.append([serverResponse.uid,value.port])
                            temp_uid=serverResponse.uid
                        elif serverResponse.status=='FAILURE: DELETED FILE CANNOT BE UPDATED':
                            temp_uid_fail_update=serverResponse.uid
                            print(temp_uid_fail_update)
                            failure_port.append(value.port)
                        elif serverResponse.status=='FAILED : FILE WITH THE SAME NAME ALREADY EXISTS':
                            temp_uid_fail_filename=uid
                            failure_port.append(value.port)
                        elif serverResponse.status=='FAILED: FILENAME IS WRONG':
                            temp_uid_fail_fileupd=uid
                            failure_port.append(value.port)

                if len(failure_port)>0:
                    if len(temp_uid_fail_update)>0:
                        if len(success_port)>0:
                            print(f"File was already Deleted in some Replica so can not update in any")
                        for values in success_port:
                            with grpc.insecure_channel('localhost:'+values[1]) as channelServerf:
                                serverStubf = server_pb2_grpc.Server_serviceStub(channelServerf)
                                serverResponsef = serverStubf.WriteServerUpdate(server_pb2.clientResponseupd(uid=values[0],type="update"))
                                print(f"Status: {serverResponsef.status}, Uid: {serverResponsef.uid}, Version: {serverResponsef.version}")

                    if len(temp_uid_fail_filename)>0:
                        if len(success_port)>0:
                            print(f"File with same name already present in some Replicas so deleting the successfull entries")
                        for values in success_port:
                            with grpc.insecure_channel('localhost:'+values[1]) as channelServerf:
                                serverStubf = server_pb2_grpc.Server_serviceStub(channelServerf)
                                serverResponsef = serverStubf.WriteServerUpdate(server_pb2.clientResponseupd(uid=values[0],type="filename"))
                                print(f"Status: {serverResponsef.status}, Uid: {serverResponsef.uid}, Version: {serverResponsef.version}")

                    if len(temp_uid_fail_fileupd)>0:
                        if len(success_port)>0:
                            print(f"File with same UID already present in some Replicas so deleting the successfull entries")
                        for values in success_port:
                            with grpc.insecure_channel('localhost:'+values[1]) as channelServerf:
                                serverStubf = server_pb2_grpc.Server_serviceStub(channelServerf)
                                serverResponsef = serverStubf.WriteServerUpdate(server_pb2.clientResponseupd(uid=values[0],type="fileupd"))
                                print(f"Status: {serverResponsef.status}, Uid: {serverResponsef.uid}, Version: {serverResponsef.version}")


             


        elif argument==2:
            print("Inside Read server List")
            with grpc.insecure_channel('localhost:50051') as channel:
                print("connect to registry server")
                stub = registry_pb2_grpc.RegisterStub(channel)
                response = stub.GetServerList(registry_pb2.ClientRequest(client='read'))
        
             

                print("List of Read Quorums (N_r) : ")
                i=0
                for value in response.serverclient:
                    print(i+1,end=" ")
                    print(". "+value.name + " - "+ value.ip+":"+value.port)
                    i+=1


                print("Enter UID : ",end="")

                uid=sys.argv[index]
                index+=1
                print(uid)

                # uid=input("Enter UID : ")

                latest_data={"Version":"","Status":"","UID":"","Content":""}

                
                for value in response.serverclient:
                    with grpc.insecure_channel('localhost:'+value.port) as channelServerRead:
                        serverStubr = server_pb2_grpc.Server_serviceStub(channelServerRead)
                        serverResponseR = serverStubr.ReadServer(server_pb2.clientResponseRead(uid=uid))
                       
                        if len(latest_data['Version'])==0:
                            latest_data['Version']=serverResponseR.version
                            latest_data['Status']=serverResponseR.status
                            latest_data['UID']=serverResponseR.uid
                            latest_data['Content']=serverResponseR.content
                        elif latest_data['Version']<serverResponseR.version:
                            latest_data['Version']=serverResponseR.version
                            latest_data['Status']=serverResponseR.status
                            latest_data['UID']=serverResponseR.uid
                            latest_data['Content']=serverResponseR.content

                print("Final Data From Read : ")
                print("---------------------------------------------------------")
                print()
                print("Status : ",latest_data['Status'])
                print("UID : ",latest_data['UID'])
                print("Content : ",latest_data['Content'])
                print("Version : ",latest_data["Version"])

                        
        elif argument==3:
            print("Inside Delete server List")
            with grpc.insecure_channel('localhost:50051') as channel:
                print("connect to registry server")
                stub = registry_pb2_grpc.RegisterStub(channel)
                response = stub.GetServerList(registry_pb2.ClientRequest(client='delete'))
        
                # print(response)
               
                print("List of write quorum (N_w) : ")
                i=0
                for value in response.serverclient:
                    print(i+1,end=" ")
                    print(". "+value.name + " - "+ value.ip+":"+value.port)
                    i+=1

                print("Enter UID : ",end="")

                uid=sys.argv[index]
                index+=1
                print(uid)
                success_port=[]
                failure_port=[]
                status=""
                for value in response.serverclient:
                    with grpc.insecure_channel('localhost:'+value.port) as channelServerDelete:
                        serverStubd = server_pb2_grpc.Server_serviceStub(channelServerDelete)
                        serverResponseD = serverStubd.DeleteServer(server_pb2.clientResponseDelete(uid=uid,work="first"))
                        status=serverResponseD.status

                        if status == "FAILED: FILE DOES NOT EXIST":
                            failure_port.append(value.port)
                        elif status == 'SUCCESS':
                            
                            success_port.append(value.port)

                        print(f"UID : {uid} file delete status : {status}")

                if len(success_port)>0:
                    if len(failure_port)>0:
                        print("File was not present in Some of the replica so creating in memory entry")

                        for values in failure_port:
                            with grpc.insecure_channel('localhost:'+value.port) as channelServerDeletes:
                                serverStubds = server_pb2_grpc.Server_serviceStub(channelServerDeletes)
                                serverResponseDs = serverStubds.DeleteServer(server_pb2.clientResponseDelete(uid=uid,work="second"))
                                status=serverResponseDs.status

                                print(f"UID : {uid} file delete status : {status}")


        elif argument==4:
            print("Inside All server List")
            with grpc.insecure_channel('localhost:50051') as channel:
                print("connect to registry server")
                stub = registry_pb2_grpc.RegisterStub(channel)
                response = stub.GetServerList(registry_pb2.ClientRequest(client='all'))
        
                # print(response)
               
                print("List of All Replicas (N) : ")
                i=0
                for value in response.serverclient:
                    print(i+1,end=" ")
                    print(". "+value.name + " - "+ value.ip+":"+value.port)
                    i+=1

        else:
            break

   

if __name__ == '__main__':
    getAllServers()
