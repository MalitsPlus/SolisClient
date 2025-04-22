@echo off

python proto_analyzer_meta.py
python proto_analyzer_ts.py
protoc -I=D:/GitHub/SolisClient/cache --python_out=D:/GitHub/SolisClient/cache penum.proto pmaster.proto ptransaction.proto
protoc -I=D:/GitHub/SolisClient/cache --python_out=D:/GitHub/SolisClient/cache papi.proto 

protoc -I=D:/GitHub/SolisClient/cache --python_out=D:/GitHub/SolisClient/cache papi.proto 
python -m grpc_tools.protoc --proto_path=./cache ./cache/papi.proto --grpc_python_out=./cache
python gen_grpc_aftermath.py
pause