import grpc
import concurrent
from concurrent import futures

from borrwor_pb2_grpc import BorrowServicer, add_BorrowServicer_to_server
from borrwor_pb2 import BorrowerResponse
 

class BorrowServer(BorrowServicer):
    
    def RequestLoan(self, request, context):
        print(f'we got something. {request.Id}')
        respones = BorrowerResponse()
        respones.message = f'this customer not loan'
        return respones

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BorrowServicer_to_server(BorrowServer(), server)
    server.add_insecure_port('[::]:50551')
    print('server is started')
    server.start()
    server.wait_for_termination()

main()