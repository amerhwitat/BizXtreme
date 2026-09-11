#define UNICODE
#define _UNICODE
#include <windows.h>
#include <shlobj.h>
#include <fstream>
#include <sstream>
#include <string>
struct State { long long score=0, xp=0, playTime=0; int chapter=1, expedition=72; };
static State g; static HWND status;
static std::wstring Path() { PWSTR p=nullptr; SHGetKnownFolderPath(FOLDERID_LocalAppData,0,nullptr,&p); std::wstring x=p?p:L"."; if(p) CoTaskMemFree(p); x+=L"\\BizXtreme"; CreateDirectoryW(x.c_str(),nullptr); return x+L"\\save.dat"; }
static void Save(){std::ofstream o(Path(),std::ios::trunc);o<<g.score<<' '<<g.xp<<' '<<g.playTime<<' '<<g.chapter<<' '<<g.expedition;}
static void Load(){std::ifstream i(Path());if(!(i>>g.score>>g.xp>>g.playTime>>g.chapter>>g.expedition))g={};}
static void Refresh(){std::wstringstream s;s<<L"BIZXTREME — AURORA FRONTIER\r\n\r\nScore: "<<g.score<<L"\r\nXP: "<<g.xp<<L"\r\nChapter: "<<g.chapter<<L"\r\nExpedition: "<<g.expedition<<L"%\r\nPlay time: "<<g.playTime<<L" sec\r\n\r\nStories: Awakening • Broken Signal • Frontier Alliance • Black Aurora • Great Expedition • Glass Horizon • Neural Frontier";SetWindowTextW(status,s.str().c_str());}
LRESULT CALLBACK W(HWND h,UINT m,WPARAM w,LPARAM){if(m==WM_CREATE){status=CreateWindowW(L"STATIC",L"",WS_CHILD|WS_VISIBLE,20,20,740,270,h,nullptr,nullptr,nullptr);CreateWindowW(L"BUTTON",L"Explore",WS_CHILD|WS_VISIBLE,20,310,120,36,h,(HMENU)1,nullptr,nullptr);CreateWindowW(L"BUTTON",L"Save",WS_CHILD|WS_VISIBLE,150,310,100,36,h,(HMENU)2,nullptr,nullptr);CreateWindowW(L"BUTTON",L"Resume",WS_CHILD|WS_VISIBLE,260,310,100,36,h,(HMENU)3,nullptr,nullptr);CreateWindowW(L"BUTTON",L"Hall of Fame",WS_CHILD|WS_VISIBLE,370,310,130,36,h,(HMENU)4,nullptr,nullptr);CreateWindowW(L"BUTTON",L"Discover Players",WS_CHILD|WS_VISIBLE,510,310,150,36,h,(HMENU)5,nullptr,nullptr);Refresh();return 0;}if(m==WM_COMMAND){switch(LOWORD(w)){case 1:g.score+=500;g.xp+=150;g.playTime+=60;if(g.xp>=(g.chapter*1000))++g.chapter;if(g.expedition<100)++g.expedition;Refresh();break;case 2:Save();MessageBoxW(h,L"Game saved locally.",L"BizXtreme",MB_OK);break;case 3:Load();Refresh();break;case 4:MessageBoxW(h,L"Hall of Fame is maintained locally and can be synchronized by an approved service.",L"BizXtreme",MB_OK);break;case 5:MessageBoxW(h,L"Player discovery uses opt-in peer identifiers. Raw IP addresses are not persisted.",L"BizXtreme P2P",MB_OK);break;}return 0;}if(m==WM_DESTROY){Save();PostQuitMessage(0);return 0;}return DefWindowProcW(h,m,w,l);}
int WINAPI wWinMain(HINSTANCE hi,HINSTANCE, PWSTR,int show){Load();const wchar_t c[]=L"BizXtremeStandalone";WNDCLASSW wc{};wc.lpfnWndProc=W;wc.hInstance=hi;wc.lpszClassName=c;wc.hCursor=LoadCursor(nullptr,IDC_ARROW);RegisterClassW(&wc);HWND h=CreateWindowExW(0,c,L"BizXtreme — Standalone VC++ Desktop",WS_OVERLAPPEDWINDOW,CW_USEDEFAULT,CW_USEDEFAULT,800,420,nullptr,nullptr,hi,nullptr);if(!h)return 1;ShowWindow(h,show);MSG m{};while(GetMessageW(&m,nullptr,0,0)>0){TranslateMessage(&m);DispatchMessageW(&m);}return (int)m.wParam;}
