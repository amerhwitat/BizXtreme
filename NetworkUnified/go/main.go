package main
import("fmt";"net";"os";"strconv")
func main(){p:=8787;if n,e:=strconv.Atoi(os.Getenv("NETWORK_API_PORT"));e==nil&&n>0{p=n};fmt.Printf("{\"schema\":\"bizxtreme.network.api.v1\",\"implementation\":\"go\",\"port\":%d}\n",p);fmt.Println("scope 127.0.0.1 = local/intranet");_,e:=net.DialTimeout("tcp",fmt.Sprintf("127.0.0.1:%d",p),1e9);fmt.Println("local API port reachable =",e==nil)}
