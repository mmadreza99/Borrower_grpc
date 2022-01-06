import grpc
import concurrent
from concurrent import futures

from proto.borrwor_pb2_grpc import BorrowServicer, add_BorrowServicer_to_server, BorrowStub
from proto.borrwor_pb2 import  BankReturnCheckResponse

# BankReturnCheckRequest(Id=id, n_account=n_account)

class BorrowServer(BorrowServicer):

    def RequestCheck(self, request, context):
        print(f'in server to we got something. {request.Id} , {request.n_account}')
        respones = BankReturnCheckResponse()
        respones.message = 'True'
        return respones

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BorrowServicer_to_server(BorrowServer(), server)
    server.add_insecure_port('[::]:50505')
    print('server2 is started on prot 50505')
    server.start()
    server.wait_for_termination()

main()