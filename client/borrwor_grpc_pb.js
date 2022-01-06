// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var borrwor_pb = require('./borrwor_pb.js');

function serialize_BorrowerRequest(arg) {
  if (!(arg instanceof borrwor_pb.BorrowerRequest)) {
    throw new Error('Expected argument of type BorrowerRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_BorrowerRequest(buffer_arg) {
  return borrwor_pb.BorrowerRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_BorrowerResponse(arg) {
  if (!(arg instanceof borrwor_pb.BorrowerResponse)) {
    throw new Error('Expected argument of type BorrowerResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_BorrowerResponse(buffer_arg) {
  return borrwor_pb.BorrowerResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var BorrowService = exports.BorrowService = {
  requestLoan: {
    path: '/Borrow/RequestLoan',
    requestStream: false,
    responseStream: false,
    requestType: borrwor_pb.BorrowerRequest,
    responseType: borrwor_pb.BorrowerResponse,
    requestSerialize: serialize_BorrowerRequest,
    requestDeserialize: deserialize_BorrowerRequest,
    responseSerialize: serialize_BorrowerResponse,
    responseDeserialize: deserialize_BorrowerResponse,
  },
};

exports.BorrowClient = grpc.makeGenericClientConstructor(BorrowService);
