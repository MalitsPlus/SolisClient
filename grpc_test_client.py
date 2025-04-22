from concurrent import futures

import grpc

import papi_pb2 as apip
import papi_grpc as apig
import ptransaction_pb2 as transp
import google.protobuf.empty_pb2 as empty


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = apig.MasterStub(channel)
        response = stub.Get(empty.Empty())
        # response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.masterTag.version)


if __name__ == "__main__":
    run()