from os import read
import grpc
from concurrent import futures

from proto.borrwor_pb2_grpc import BorrowServicer, add_BorrowServicer_to_server
from proto.borrwor_pb2 import  BankReturnCheckResponse


def read_file(id, account):
    with open('server2/list_return_check.txt', 'r') as f:
        for i in f.readlines():
            split = i.split(' ')
            if int(split[0]) == id and int(split[1]) == account:
                return split[2]
        return 'NO'


class BorrowServer(BorrowServicer):

    def RequestCheck(self, request, context):
        respones = BankReturnCheckResponse()
        result = read_file(request.Id, request.n_account)
        print(f'in server to we got something. {request.Id}, {request.n_account}\
            the result : {result}')
        if result== 'YES':
            respones.message = False  
        elif result == 'NO':
            respones.message = True
        return respones


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BorrowServicer_to_server(BorrowServer(), server)
    server.add_insecure_port('[::]:50505')
    print('server2 is started on prot 50505')
    server.start()
    server.wait_for_termination()

main()
