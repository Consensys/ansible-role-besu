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
| `besu_version` | ___unset___ |  __REQUIRED__ Version of Besu to install and run. All available versions are listed on our Besu [solutions](https://pegasys.tech/solutions/hyperledger-besu/) page |
| `besu_user` | besu | Besu user |
| `besu_group` | besu | Besu group |
| `besu_download_url` | https://bintray.com/hyperledger-org/besu-repo/download_file?file_path=besu-{{ besu_version }}.tar.gz | The download tar.gz file used. You can use this if you need to retrieve besu from a custom location such as an internal repository. |
| `besu_install_dir` | /opt/besu | Path to install to  |
| `besu_config_dir` | /etc/besu | Path for default configuration |
| `besu_node_private_key_file` | "" | Path for node private key, if supplied. This needs to include the node key file name and path like so `/home/me/me_node/myPrivateKey`. If not supplied Besu will create one automatically |
| `besu_data_dir` | /opt/besu/data | Path for data directory|
| `besu_log_dir` | /var/log/besu | Path for logs |
| `besu_profile_file` | /etc/profile.d/besu-path.sh | Path to allow loading Besu into the system PATH |
| `besu_managed_service` | true | Enables a systemd service (or launchd if on Darwin) |
| `besu_launchd_dir` | /Library/LaunchAgents | The default launchd directory  |
| `besu_systemd_dir` | /etc/systemd/system/ | The default systemd directory |
| `besu_systemd_state` | restarted | The default option for the systemd service state |
| `besu_host_ip` | "" | The host IP that Besu uses for the P2P network. This specifies the host on which P2P listens |
| `besu_default_ip` | "{{ default(ansible_host) \| default('127.0.0.1') }}" | The fallback default for `besu_host_ip` |
| `besu_network` | mainnet | The network that this node will join. Other values are 'ropsten', 'rinkeby', 'goerli', 'dev' and 'custom' |
| `besu_genesis_path` | ___unset___ | The path to the genesis file, only valid when `besu_network` is `custom` |
| `besu_sync_mode` | FAST | Specifies the synchronization mode. Other values are 'FULL' |
| `besu_log_level` | INFO | The log level to use. Other log levels are 'OFF', 'FATAL', 'WARN', 'INFO', 'DEBUG', 'TRACE', 'ALL' |
| `besu_p2p_port` | 30303 | Specifies the P2P listening ports (UDP and TCP). Ports must be exposed appropriately |
| `besu_rpc_http_enabled` | true | Enabled the HTTP JSON-RPC service |
| `besu_rpc_http_host` | 0.0.0.0 | Specifies the host on which HTTP JSON-RPC listens |
| `besu_rpc_http_api` | ["ADMIN","DEBUG","NET","ETH","MINER","WEB3"] | Comma-separated APIs to enable on the HTTP JSON-RPC channel. When you use this option, the `besu_rpc_http_enabled` option must also be enabled |
| `besu_rpc_ws_enabled` | true | Enabled the WebSockets service |
| `besu_rpc_ws_host` | 0.0.0.0 | Specifies the host on which WebSockets listens |
| `besu_rpc_ws_port` | 8546 | Specifies Websockets JSON-RPC listening port (TCP). Port must be exposed appropriately |
| `besu_metrics_host` | 0.0.0.0 | Specifies the host on which Prometheus accesses Besu metrics. The metrics server respects the `besu_whitelist` option |
| `besu_metrics_port` | 9545 | Specifies the port on which Prometheus accesses Besu metrics |
| `besu_bootnodes` | [] | List of comma-separated enode URLs for P2P discovery bootstrap. When connecting to MainNet or public testnets, the default is a predefined list of enode URLs |
| `besu_host_whitelist` | ["*"] | Comma-separated list of hostnames to allow access to the JSON-RPC API. By default, access from localhost and 127.0.0.1 is accepted. |
| `besu_cmdline_args` | "" | Command line args that are passed in as overrides |
| `besu_env_opts` | "" | Environmental variable BESU_OPTS that gets passed to the JVM. eg: -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005 |


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
