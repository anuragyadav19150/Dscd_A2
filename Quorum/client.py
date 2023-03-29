import grpc 
import registry_pb2
import registry_pb2_grpc
import server_pb2
import server_pb2_grpc
from concurrent import futures
import uuid
from datetime import datetime

def getAllServers():
    # print("Generating uuid for a client")
   

    while True:
        print("1. Write")
        print("2. Read ")
        print("3. Delete")
        print("4. Exit")

        argument=int(input("Choose one of the above options : "))

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


                uid=input("Enter UID : ")
                # updatevalue=int(input("Do you want to update or write , for update press 1 and write press 2 : "))

                # if updatevalue==2:
                #     uid=str(uuid.uuid1())

                filename=input("Enter the name of file : ")
                content=input("Enter content of file : ")

                success_port=[]
                failure_port=[]
                temp_uid=""
                for value in response.serverclient:
                    with grpc.insecure_channel('localhost:'+value.port) as channelServer:
                        serverStub = server_pb2_grpc.Server_serviceStub(channelServer)
                        serverResponse = serverStub.WriteServer(server_pb2.clientResponse(uid=uid,filename=filename,content=content))
                        # print("Status : ",serverResponse.status)
                        # print("UID : ",serverResponse.uid)
                        # print("Version : ",serverResponse.version)

                        print(f"Status: {serverResponse.status}, Uid: {serverResponse.uid}, Version: {serverResponse.version}")
                        

                        if serverResponse.status[0]=='S':
                            success_port.append(value.port)
                            temp_uid=serverResponse.uid
                        else:
                            failure_port.append(value.port)

                if len(success_port)>0:
                    if len(failure_port)>0:
                        print("File was not present in some of the replica so creating the file")
                    for values in failure_port:
                        with grpc.insecure_channel('localhost:'+values) as channelServerf:
                            serverStubf = server_pb2_grpc.Server_serviceStub(channelServerf)
                            serverResponsef = serverStubf.WriteServer(server_pb2.clientResponse(uid=temp_uid,filename=filename,content=content))
                            # print("Status : ",serverResponsef.status)
                            # print("UID : ",serverResponsef.uid)
                            # print("Version : ",serverResponsef.version)
                            print(f"Status: {serverResponsef.status}, Uid: {serverResponsef.uid}, Version: {serverResponsef.version}")


        elif argument==2:
            print("Inside Read server List")
            with grpc.insecure_channel('localhost:50051') as channel:
                print("connect to registry server")
                stub = registry_pb2_grpc.RegisterStub(channel)
                response = stub.GetServerList(registry_pb2.ClientRequest(client='read'))
        
                # print(response.serverclient)
                # print(type(response))

                # data={}

                # for values in response.serverclient:
                #     print(values.ip," hiii")

                print("List of Read Quorums (N_r) : ")
                i=0
                for value in response.serverclient:
                    print(i+1,end=" ")
                    print(". "+value.name + " - "+ value.ip+":"+value.port)
                    i+=1


                uid=input("Enter UID : ")

                latest_data={"Version":"","Status":"","UID":"","Content":""}

                
                for value in response.serverclient:
                    with grpc.insecure_channel('localhost:'+value.port) as channelServerRead:
                        serverStubr = server_pb2_grpc.Server_serviceStub(channelServerRead)
                        serverResponseR = serverStubr.ReadServer(server_pb2.clientResponseRead(uid=uid))
                        # print("Status : ",serverResponseR.status)
                        # print("UID : ",serverResponseR.uid)
                        # print("Version : ",serverResponseR.version)
                        # print("Content : ",serverResponseR.content)
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

                uid=input("Enter UID : ")
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




        else:
            break

   

if __name__ == '__main__':
    getAllServers()
