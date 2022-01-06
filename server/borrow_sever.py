import grpc
from concurrent import futures

from proto.borrwor_pb2_grpc import BorrowServicer, add_BorrowServicer_to_server, BorrowStub
from proto.borrwor_pb2 import BorrowerResponse, BankReturnCheckRequest, DeferredInstallmentRequest


class BorrowServer(BorrowServicer):
    def request_server2(self, id, n_account):
        with grpc.insecure_channel('localhost:50505') as channel:
            stub = BorrowStub(channel)
            response = stub.RequestCheck(
                BankReturnCheckRequest(Id=id, n_account=n_account)
                )
        return response
    
    def request_server3(self, id, n_account):
        with grpc.insecure_channel('localhost:50506') as channel:
            stub = BorrowStub(channel)
            response = stub.RequestInstallment(
                DeferredInstallmentRequest(Id=id, n_account=n_account)
                )
        return response
   
    def RequestLoan(self, request, context):
        s2 = self.request_server2(request.Id, request.n_account)
        s3 = self.request_server3(request.Id, request.n_account)
        print(f'RequestLoan server2 return check : {s2.message}\nRequestLoan server3 installment: {s3.message}')
        result = bool(s2.message==s3.message==True)
        respones = BorrowerResponse()
        print(result)
        if result:
            respones.message = f'Yes'
            return respones
        else:
            respones.message = f'NO'
            return respones


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BorrowServicer_to_server(BorrowServer(), server)
    server.add_insecure_port('[::]:50551')
    print('server is started')
    server.start()
    server.wait_for_termination()

main()