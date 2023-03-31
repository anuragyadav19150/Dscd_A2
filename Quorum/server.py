import grpc 
import registry_pb2
import registry_pb2_grpc
import server_pb2
import server_pb2_grpc
from concurrent import futures
import datetime
import os

data_dict={}




class Server(server_pb2_grpc.Server_serviceServicer):
         


    def WriteServer(self,request,context):
        for ke,va in data_dict.items():
            print(f"Uid: {ke}, Filename: {va[0]}, Version: {va[1]}")
        uid=request.uid
        filename=request.filename
        content=request.content
        curTime= (datetime.datetime.now())
        curTime = datetime.datetime.strftime(curTime, "%Y-%m-%d %H:%M:%S")
        uidCheck=False
        for k,v in data_dict.items():
            if k==uid:
                uidCheck=True
                break



        if uidCheck:
            print("Update file checking")
            check=False

            if data_dict[uid][0]==filename:
                check=True
            # for k,v in data_dict.items():
            #     if v[0]==filename:
            #         check=True
            #         uid=k
            #         break
            if not check and len(data_dict[uid][0])>0:
                return server_pb2.serverResponse(status='FAILED: FILENAME IS WRONG',version="",uid="")
            
            else:
                filename=data_dict[uid][0]
                
                file_path = os.path.join('./replica_'+portNo+'/', filename)
                # if os.path.exists(file_path):
                if len(filename)>0:
                    path='./'+'replica_'+portNo+'/'+filename
                    os.remove(path)
                    
                    with open(file_path, 'w') as f:
                        f.write(content)
                        print(f"Updated file '{filename}' and wrote message '{content}' to it")
                    data_dict[uid]=[filename,curTime]
                    print(f"UID : {uid} Filename : {data_dict[uid][0]} Version : {data_dict[uid][1]}")
                    return server_pb2.serverResponse(status='SUCCESS',version=curTime,uid=uid)
                
                else:
                    return server_pb2.serverResponse(status='FAILURE: DELETED FILE CANNOT BE UPDATED',version=curTime,uid=uid)

            
        else:
            filecheck=False
            for k,v in data_dict.items():
                if v[0]==filename:
                    filecheck=True
                    break

            if filecheck:
                return server_pb2.serverResponse(status='FAILED : FILE WITH THE SAME NAME ALREADY EXISTS',version="",uid="")
            
            else:
                file_path = os.path.join('./replica_'+portNo+'/', filename)
                with open(file_path, 'w') as f:
                    f.write(content)
                    print(f"Created file '{filename}' and wrote message '{content}' to it")
                data_dict[uid]=[filename,curTime]
                print(f"UID : {uid} Filename : {data_dict[uid][0]} Version : {data_dict[uid][1]}")
                return server_pb2.serverResponse(status='SUCCESS',version=curTime,uid=uid)
            

    def WriteServerUpdate(self,request,context):
        curTime= (datetime.datetime.now())
        curTime = datetime.datetime.strftime(curTime, "%Y-%m-%d %H:%M:%S")
        uid=request.uid
        type=request.type
        filename=data_dict[uid][0]
        if type=='update':
            if len(filename)>0:
                file_path = os.path.join('./replica_'+portNo+'/', filename)
                os.remove(file_path)
            data_dict[uid]=["",curTime]
            return server_pb2.serverResponseupd(status='FAILURE: DELETED FILE CANNOT BE UPDATED',version=curTime,uid=uid)
        else:
            if len(filename)>0:
                file_path = os.path.join('./replica_'+portNo+'/', filename)
                os.remove(file_path)

            if uid in data_dict:
                del data_dict[uid]

            return server_pb2.serverResponseupd(status='FAILED : FILE WITH THE SAME NAME ALREADY EXISTS',version=curTime,uid=uid)



    def ReadServer(self,request,context):
        for ke,va in data_dict.items():
            print(f"Uid: {ke}, Filename: {va[0]}, Version: {va[1]}")
        uid=request.uid
        filename=""
        version=""
        content=""

        check=False
        for k,v in data_dict.items():
            if k==uid:
                check=True
                filename=v[0]
                version=v[1]
                break
        if not check:
            return server_pb2.serverResponseRead(status='FAILED: FILE DOES NOT EXIST',version="",uid="",content="")
        
        else:
            file_path = os.path.join('./replica_'+portNo+'/', filename)
            if len(filename)>0:
                with open(file_path, 'r') as file:
                    file_contents = file.read()
                    content=file_contents

                return server_pb2.serverResponseRead(status='SUCCESS',version=version,uid=uid,content=content)
            
            else:
                return server_pb2.serverResponseRead(status='FAILED: FILE ALREADY DELETED',version="",uid="",content="")
            
    def DeleteServer(self,request,context):
        for ke,va in data_dict.items():
            print(f"Uid: {ke}, Filename: {va[0]}, Version: {va[1]}")
        uid=request.uid
        work=request.work
        filename=""
        curTime= (datetime.datetime.now())
        curTime = datetime.datetime.strftime(curTime, "%Y-%m-%d %H:%M:%S")
        # print(data_dict)
        # print(f"{uid} {work}")

        if work=="first":

            check=False
            # print(data_dict)
            for k,v in data_dict.items():
                if k==uid:
                    check=True
                    filename=v[0]
                    break
            # print(check)
            if not check:
                return server_pb2.serverResponseDelete(status='FAILED: FILE DOES NOT EXIST')
            
            else:
                # print(filename)
                
                file_path = os.path.join('./replica_'+portNo+'/', filename)
                # print(file_path)
                # print(f"len of filename {len(filename)}")
                if len(filename)>0:
                    os.remove(file_path)
                    data_dict[uid]=["",curTime]

                    print(f"UID : {uid} Filename : {data_dict[uid][0]} Version : {data_dict[uid][1]}")
                    return server_pb2.serverResponseDelete(status='SUCCESS')
                
                else:
                    # print(f"len of filename {len(filename)}")
                    return server_pb2.serverResponseDelete(status='FAILED: FILE ALREADY DELETED')
                
        else:
            
            data_dict[uid]=["",curTime]
            print(f"UID : {uid} Filename : {data_dict[uid][0]} Version : {data_dict[uid][1]}")
            return server_pb2.serverResponseDelete(status='SUCCESS: UID ADDED IN MEMORY MAP')



      

        



def regiterToRegistryServer():
    print('Registering to registry server...')
    channel = grpc.insecure_channel('localhost:50051')
    stub = registry_pb2_grpc.RegisterStub(channel)

    
    response = stub.registerServer(registry_pb2.registerServerRequest(server=serverr))
    print("Response from regitry server: " + response.response)
    

    if response.response=='Success':
        # print('inside successssssssssssssss')
        
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        # server_pb2_grpc.add_RegisterServicer_to_server(Server(), server)
        server_pb2_grpc.add_Server_serviceServicer_to_server(Server(),server)
        server.add_insecure_port('[::]:' + portNo)
        server.start()
        print("Server started, listening on " + portNo)
        server.wait_for_termination()

        

if __name__ == '__main__':
    name =input("Enter name of the server : ")
    portNo = input("Enter Port no : ")
    
    serverr = server_pb2.Server()
    # name=portNo
    serverr.name=name
    serverr.ip='127:0:0:1'
    serverr.port=portNo
    
    regiterToRegistryServer()

