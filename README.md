## Solis Client 

### Preparations
1. Create cache directories. 
```
> mkdir cache
> mkdir masterdata
```

2. Create a `client_cache.json` in this folder, which has the following schema: 
```
{
    "masterVersion": "abcd",
    "octoCacheRevision": 0,
    "refreshToken": "abcd",
    "idToken": "abcd",
    "firebaseAuthToken": "abcd"
}
```
You can set all string values to empty because they will be automatically updating during the program running except `refreshToken`, which MUST be given at the first running. 

### How to use
```
> python main.py
```
That's all. 

### Updating
If API has been updated, take the following steps to keep the client proto schema up-to-date with server. 

0. Back up your files to avoid unexpected overrides. 

1. Move `dump.cs` generated by il2cppdumper to `cache/` folder. 

2. Run `proto_analyzer_meta.py` to generate .proto files. 

3. Add `service`s to `ProtoApi.proto`. Currently, required services are listed as follows. 
```
service System {
  rpc Check(SystemCheckRequest) returns (SystemCheckResponse);
}
service Auth {
  rpc Login(AuthLoginRequest) returns (AuthLoginResponse);
}
service Master {
  rpc Get(google.protobuf.Empty) returns (MasterGetResponse);
}
service User {
  rpc Get(google.protobuf.Empty) returns (UserGetResponse);
}
service Home {
  rpc Login(HomeLoginRequest) returns (HomeLoginResponse);
  rpc Enter(HomeEnterRequest) returns (HomeEnterResponse);
}
service Dokan {
  rpc List(google.protobuf.Empty) returns (DokanListResponse);
}
service Notice {
  rpc List(google.protobuf.Empty) returns (NoticeListResponse);
}
```

4. Run `gen_proto.bat` to generate python code, or run the following commands in orde. 
```
> python -m grpc_tools.protoc --proto_path=. ./ProtoEnum.proto ./ProtoMaster.proto ./ProtoTransaction.proto --python_out=.
> python -m grpc_tools.protoc --proto_path=. ./ProtoApi.proto --python_out=. --grpc_python_out=.
> python gen_grpc_aftermath.py
```
