# Ansible Role: Besu

### Description
Ansible role that will install, configure and runs [Besu](https://www.hyperledger.org/projects/besu): an enterprise Java Ethereum Client

### Table of Contents
  - [Supported Platforms](#supported-platforms)
  - [Dependencies](#dependencies)
  - [Role Variables](#role-variables)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

### Supported Platforms
```
* MacOS
* Debian
* Ubuntu
* Redhat(CentOS/Fedora)
* Amazon
```

### Dependencies

* JDK 11 or greater

### Role Variables:

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file. By and large these variables are configuration options. Please refer to the Besu [docs](https://besu.hyperledger.org/en/stable/) for more information

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `besu_build_from_source` | ___unset___ |  When set to `true`, Besu is build from git sources. See also `besu_git_repo` and `besu_git_commit` |
| `besu_version` | ___unset___ |  __REQUIRED__ if `besu_build_from_source` is false. Version of Besu to install and run. All available versions are listed on our Besu [solutions](https://pegasys.tech/solutions/hyperledger-besu/) page |
| `besu_git_repo` | https://github.com/hyperledger/besu.git | The URL to use when cloning besu sources. Only necessary when `besu_build_from_source` is `true`. |
| `besu_git_commit` | master | The git commit to use when building Besu from source. Can be a branchname, commit hash, or anything that's legal to be used as an argument to `git checkout`. Only used if `besu_build_from_source` is `true`. |
| `besu_user` | besu | Besu user |
| `besu_group` | besu | Besu group |
| `besu_download_url` | https://hyperledger.jfrog.io/artifactory/besu-binaries/besu/{{ besu_version }}/besu-{{ besu_version }}.tar.gz | The download tar.gz file used. You can use this if you need to retrieve besu from a custom location such as an internal repository. |
| `besu_install_dir` | /opt/besu | Path to install to  |
| `besu_config_dir` | /etc/besu | Path for default configuration |
| `besu_node_private_key_file` | "" | Path for node private key, if supplied. This needs to include the node key file name and path like so `/home/me/me_node/myPrivateKey`. If not supplied Besu will create one automatically |
| `besu_data_dir` | /opt/besu/data | Path for data directory|
| `besu_log_dir` | /var/log/besu | Path for logs |
| `besu_log4j_config_file` | "" | Absolute path for a custom log4j config file |
| `besu_profile_file` | /etc/profile.d/besu-path.sh | Path to allow loading Besu into the system PATH |
| `besu_managed_service` | true | Enables a systemd service (or launchd if on Darwin) |
| `besu_launchd_dir` | /Library/LaunchAgents | The default launchd directory  |
| `besu_systemd_dir` | /etc/systemd/system/ | The default systemd directory |
| `besu_systemd_state` | restarted | The default option for the systemd service state |
| `besu_identity` | ___unset___  | Configuration of Identity in the Client ID |
| `besu_host_ip` | "" | The host IP that Besu uses for the P2P network. This specifies the host on which P2P listens |
| `besu_default_ip` | "{{ default(ansible_host) \| default('127.0.0.1') }}" | The fallback default for `besu_host_ip` |
| `besu_max_peers` | ___unset___ | The maximum number of P2P connections you can establish |
| `besu_network` | mainnet | The network that this node will join. Other values are 'ropsten', 'rinkeby', 'goerli', 'classic', 'mordor', 'kotti', 'dev' and 'custom' |
| `besu_genesis_path` | ___unset___ | The path to the genesis file, only valid when `besu_network` is `custom` |
| `besu_sync_mode` | FAST | Specifies the synchronization mode. Other values are 'FULL' |
| `besu_log_level` | INFO | The log level to use. Other log levels are 'OFF', 'FATAL', 'WARN', 'INFO', 'DEBUG', 'TRACE', 'ALL' |
| `besu_p2p_port` | 30303 | Specifies the P2P listening ports (UDP and TCP). Ports must be exposed appropriately |
| `besu_min_gas` | 1000 | The minimum price that a transaction offers for it to be included in a mined block |
| `besu_miner_enabled` | false | Enables mining when the node is started |
| `besu_miner_coinbase` | 0x | Account to which mining rewards are paid |
| `besu_miner_extra_data` | "" | A hex string representing the 32 bytes to be included in the extra data field of a mined block. |
| `besu_rpc_http_enabled` | true | Enabled the HTTP JSON-RPC service |
| `besu_rpc_http_host` | 0.0.0.0 | Specifies the host on which HTTP JSON-RPC listens |
| `besu_rpc_http_port` | 8545 | Specifies the port on which HTTP JSON-RPC listens |
| `besu_rpc_http_api` | ["ADMIN","DEBUG","NET","ETH","MINER","WEB3"] | Comma-separated APIs to enable on the HTTP JSON-RPC channel. When you use this option, the `besu_rpc_http_enabled` option must also be enabled |
| `besu_rpc_http_cors_origins` | ["all"] | Comma separated origin domain URLs for CORS validation |
| `besu_rpc_ws_enabled` | true | Enabled the WebSockets service |
| `besu_rpc_ws_api` | ["NET", "ETH", "WEB3"] | Comma-separated APIs to enable on the HTTP JSON-RPC channel. When you use this option, the `besu_rpc_ws_enabled` option must also be enabled |
| `besu_rpc_ws_host` | 0.0.0.0 | Specifies the host on which WebSockets listens |
| `besu_rpc_ws_port` | 8546 | Specifies Websockets JSON-RPC listening port (TCP). Port must be exposed appropriately |
| `besu_graphql_http_enabled` | true | Enabled the HTTP JSON-RPC service |
| `besu_graphql_http_host` | 0.0.0.0 | Specifies the host on which HTTP JSON-RPC listens |
| `besu_graphql_http_port` | 8547 | Specifies the port on which HTTP JSON-RPC listens |
| `besu_graphql_http_cors_origins` | ["all"] | Comma separated origin domain URLs for CORS validation |
| `besu_metrics_host` | 0.0.0.0 | Specifies the host on which Prometheus accesses Besu metrics. The metrics server respects the `besu_whitelist` option |
| `besu_metrics_port` | 9545 | Specifies the port on which Prometheus accesses Besu metrics |
| `besu_bootnodes` | [] | List of comma-separated enode URLs for P2P discovery bootstrap. When connecting to MainNet or public testnets, the default is a predefined list of enode URLs |
| `besu_host_whitelist` | `["*"]` | Comma-separated list of hostnames to allow access to the JSON-RPC API. By default, access from localhost and 127.0.0.1 is accepted. |
| `besu_permissions_accounts_config_file` | ___unset___ | Path to the [local accounts permissioning file](http://besu.hyperledger.org/en/stable/HowTo/Limit-Access/Local-Permissioning/#permissions-configuration-file) |
| `besu_permissions_nodes_config_file` | ___unset___ | Path to the [local nodes permissioning file](http://besu.hyperledger.org/en/stable/HowTo/Limit-Access/Local-Permissioning/#permissions-configuration-file) |
| `besu_permissions_accounts_contract_address` | ___unset___ | The contract address for onchain accounts permissioning |
| `besu_permissions_nodes_contract_address` | ___unset___ | The contract address for onchain nodes permissioning |
| `besu_cmdline_args` | "" | Command line args that are passed in as overrides |
| `besu_env_opts` | [] | Settings passed to the JVM through `BESU_OPTS` environment variable. eg: `[-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005]s` |
| `besu_privacy_enabled` | false | Enable privacy |
| `besu_privacy_url` | "" | URL to contact Orion on including port eg: `http://localhost:8888` |
| `besu_privacy_public_key_file` | ""| Path to Orion public key |
| `besu_privacy_marker_tx_signing_key_file` | "" | Path of the private key file used to sign Privacy Marker Transactions. If you do not specify this option, Besu signs each transaction with a different randomly generated key. |

### Example Playbook

1. Default setup:
Install the role from galaxy
```
ansible-galaxy install pegasyseng.hyperledger_besu
```

Create a requirements.yml with the following:
Replace `x.y.z` below with the version you would like to use from the Besu [solutions](https://pegasys.tech/solutions/hyperledger-besu/) page
```
---
- hosts: localhost
  connection: local
  force_handlers: True

  roles:
  - role: pegasyseng.hyperledger_besu
    vars:
      besu_version: x.y.z

```

Run with ansible-playbook:
```
ansible-playbook -v /path/to/requirements.yml
```


2. Install via github

```
ansible-galaxy install git+https://github.com/pegasyseng/ansible-role-besu.git
```

Create a requirements.yml with the following:
Replace `x.y.z` below with the version you would like to use from the Besu [solutions](https://pegasys.tech/solutions/hyperledger-besu/) page
```
---
- hosts: localhost
  connection: local
  force_handlers: True

  roles:
  - role: ansible-role-besu
    vars:
      besu_version: x.y.z

```

Run with ansible-playbook:
```
ansible-playbook -v /path/to/requirements.yml
```


### License

Apache


### Author Information

PegaSysEng, 2019
