// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "BizXtremeMobile",
    platforms: [.iOS(.v16)],
    products: [.library(name: "BizXtremeMobile", targets: ["BizXtremeMobile"])],
    targets: [.target(name: "BizXtremeMobile")]
)
