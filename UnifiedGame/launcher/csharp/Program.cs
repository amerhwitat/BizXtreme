using System;
class Program {
    static void Main(string[] args) {
        var mode="default"; var cash=10000.0;
        for(int i=0;i<args.Length;i++){ if(args[i]=="--mode" && i+1<args.Length) mode=args[++i]; else if(args[i]=="--cash" && i+1<args.Length && double.TryParse(args[++i],out var c)) cash=c; }
        Console.WriteLine($"{{\"application\":\"BizXtreme Unified Game\",\"mode\":\"{mode}\",\"runtime\":\"csharp\",\"cash\":{cash:F2},\"status\":\"started\"}}");
    }
}
