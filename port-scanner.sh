for port in {1..65535}; do (echo >/dev/tcp/10.10.10.86/$port) 2>/dev/null && echo port $port is open; done
