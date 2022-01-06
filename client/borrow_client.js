const grpc = require('grpc');
const message = require('./borrwor_pb');
const services = require('./borrwor_grpc_pb');

function main() {
    const clinet = new services.BorrowClient(
        'localhost:50551', grpc.credentials.createInsecure()
    );
    
    const BorrowerRequest = new message.BorrowerRequest();
    BorrowerRequest.setId(410669123);
    BorrowerRequest.setNAccount(300869905)
    clinet.requestLoan(BorrowerRequest, function (err, response) {
        if (err) {
            console.log('this thing broke!', err);
        } else {
            console.log('response from python : ', response);
        }
    })

}

main();
