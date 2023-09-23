关于本地clone仓库出现的问题:
1: Recv failure: Connection was reset
如果报这个错误我们可以执行下面的命令:
git config --global http.sslVerify false
执行完后可能还会报超时错误
Failed to connect to github.com port 443 after 21080 ms: Couldn't connect to server
可以执行以下命令:
git config --global --unset http.proxy
