# Telegram Open Network HTTP web proxy

This proxy is used to proxify user requests into the Telegram Open Network, in which you can access sites that hidden from global Internet.


### Installation:
1. Linux system
2. Get **rldp-http-proxy** from: https://github.com/ton-blockchain/ton \
or take built container from: https://hub.docker.com/r/it4addict/rldp-http-proxy
3. Get ton-global config: https://test.ton.org/ton-global-lite-client.config.json
4. Clone ton_web_proxy

### Startup steps:
1. Run: `rldp-http-proxy/rldp-http-proxy -p 8080 -c 3333 -C ton-global-lite-client.config.json` or \
  `docker run -ti it4addict/rldp-http-proxy -p 8080 -c 3333 -C ton-global-lite-client.config.json`; if you using Docker container.
2. Then run cmd `docker-compose up --build` in directory where you cloned a **TON_web_proxy**

Must see output like below:
```
ton_proxy   | ======== Running on http://0.0.0.0:3000 ========
ton_proxy   | (Press CTRL+C to quit)

```
