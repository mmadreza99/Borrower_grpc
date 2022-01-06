import grpc
import concurrent
from concurrent import futures

from proto.borrwor_pb2_grpc import BorrowServicer, add_BorrowServicer_to_server, BorrowStub
from proto.borrwor_pb2 import  DeferredInstallmentResponse


class BorrowServer(BorrowServicer):

    def RequestInstallment(self, request, context):
        print(f'in server3 to we got something. {request.Id} , {request.n_account}')
        respones = DeferredInstallmentResponse()
        respones.message = 'True'
        return respones

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BorrowServicer_to_server(BorrowServer(), server)
    server.add_insecure_port('[::]:50506')
    print('server3 is started on prot 50506')
    server.start()
    server.wait_for_termination()

main()