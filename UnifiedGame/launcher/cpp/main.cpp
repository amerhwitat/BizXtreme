#include <iostream>
#include <string>
int main(int argc, char** argv) {
    std::string mode="default"; double cash=10000;
    for(int i=1;i<argc;i++){ if(std::string(argv[i])=="--mode" && i+1<argc) mode=argv[++i]; else if(std::string(argv[i])=="--cash" && i+1<argc) cash=std::stod(argv[++i]); }
    std::cout << "{\"application\":\"BizXtreme Unified Game\",\"mode\":\"" << mode << "\",\"runtime\":\"cpp\",\"cash\":" << cash << ",\"status\":\"started\"}\n";
}
