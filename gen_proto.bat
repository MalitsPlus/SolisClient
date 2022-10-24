python proto_analyzer_meta.py
python proto_analyzer_ts.py
protoc -I=D:/GitHub/SolisClient/cache --python_out=D:/GitHub/SolisClient/cache ProtoEnum.proto ProtoMaster.proto ProtoTransaction.proto
:: add services
protoc -I=D:/GitHub/SolisClient/cache --python_out=D:/GitHub/SolisClient/cache ProtoApi.proto 
python -m grpc_tools.protoc --proto_path=./cache ./cache/ProtoApi.proto --grpc_python_out=./cache
python gen_grpc_aftermath.py
pause