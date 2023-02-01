[![CircleCI](https://circleci.com/gh/MalitsPlus/SolisClient/tree/master.svg?style=shield&circle-token=cc6ec2eea021e431785d7d719d53afaf60747f83)](https://circleci.com/gh/MalitsPlus/SolisClient/tree/master) 

# Solis Client

A component of [IDOLY-Backend](https://github.com/MalitsPlus/IDOLY-Backend). This repo is responsible for running CI independently against original repo.

[![CircleCI](https://dl.circleci.com/insights-snapshot/gh/MalitsPlus/SolisClient/master/run-scenarios/badge.svg?window=24h&circle-token=1f1381e10da0c144f199e402339c6fd48308db43)](https://app.circleci.com/insights/github/MalitsPlus/SolisClient/workflows/run-scenarios/overview?branch=master&reporting-window=last-24-hours&insights-snapshot=true)

## Usage

```text
usage: main.py [-h] [-t TOKEN] [-f] [-fk] [-k] [-a ASSET_MODE] [-o] [--kvauth KVAUTH] [--kvurl KVURL] [--venus]

options:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Your firebase refreshToken.
  -f, --force           Update databases without checking version.
  -fk, --force-kv       Put databases without checking version.
  -k, --kv              Notify KV server.
  -a ASSET_MODE, --asset-mode ASSET_MODE
                        Enable asset decryption mode. Can be either (all | diff).
  -o, --overwrite       Overwrite cached token. If '--token' does not exist, this argument takes no effect.
  --kvauth KVAUTH       KV server auth token.
  --kvurl KVURL         KV server endpoint.
  --venus               Check and update(if needed) hoshimi-venus databases.
```

- `--token`: **Must be given at first running**, can be omitted if `refreshToken` in `cache/client_cache.json` it not empty. If they both exist, the one in `client_cache.json` will be used first.
- `-k, --kvauth, --kvurl`: All **must be present at the same time**, otherwise they will be ignored.

## Updating

If API has been updated, take the following steps to keep the client proto schema up-to-date with server.

0. Back up your files to avoid unexpected overrides.

1. Move `dump.cs` generated by il2cppdumper to `cache/` folder.

2. Run `proto_analyzer_meta.py` to generate .proto files.

3. Add `service`s to `ProtoApi.proto`. Currently, required services are listed as follows.

    ```protobuf
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

4. Run `gen_proto.bat` to generate python code.
