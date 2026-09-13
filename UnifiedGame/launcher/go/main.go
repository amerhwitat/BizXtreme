package main
import("flag";"fmt")
func main(){ mode:=flag.String("mode","default","game mode"); cash:=flag.Float64("cash",10000,"starting cash"); flag.Parse(); fmt.Printf("{\"application\":\"BizXtreme Unified Game\",\"mode\":\"%s\",\"runtime\":\"go\",\"cash\":%.2f,\"status\":\"started\"}\n",*mode,*cash) }
