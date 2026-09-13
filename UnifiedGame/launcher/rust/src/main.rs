fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut mode = "default";
    let mut cash = 10000.0_f64;
    let mut i = 1;
    while i < args.len() {
        match args[i].as_str() {
            "--mode" if i + 1 < args.len() => { mode = &args[i + 1]; i += 1; }
            "--cash" if i + 1 < args.len() => { cash = args[i + 1].parse().unwrap_or(10000.0); i += 1; }
            _ => {}
        }
        i += 1;
    }
    println!(r#"{{"application":"BizXtreme Unified Game","mode":"{}","runtime":"rust","cash":{},"status":"started"}}"#, mode, cash);
}
