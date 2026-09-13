import Foundation
import Network
let p=Int(ProcessInfo.processInfo.environment["NETWORK_API_PORT"] ?? "8787") ?? 8787
print("{\"schema\":\"bizxtreme.network.api.v1\",\"implementation\":\"swift\",\"port\":\(p)}")
print("scope 127.0.0.1 = local/intranet")
let c=NWConnection(host:"127.0.0.1",port:.init(integerLiteral:UInt16(p)),using:.tcp);let sem=DispatchSemaphore(value:0);c.stateUpdateHandler={s in switch s{case .ready:print("local API port reachable");sem.signal();case .failed:print("local API port not reachable (normal if server not running)");sem.signal();default:break}};c.start(queue:.global());_ = sem.wait(timeout:.now()+1);c.cancel()
