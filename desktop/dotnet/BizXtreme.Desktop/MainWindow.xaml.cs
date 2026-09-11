using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Json;
using System.Windows;
namespace BizXtreme.Desktop;
[DataContract] public sealed class GameState { [DataMember] public long Score{get;set;} [DataMember] public long Xp{get;set;} [DataMember] public long PlayTime{get;set;} [DataMember] public int Chapter{get;set;}=1; [DataMember] public int Expedition{get;set;}=72; }
public partial class MainWindow : Window {
 private GameState _state=new(); private readonly string _path=Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),"BizXtreme","save.json");
 public MainWindow(){InitializeComponent();Directory.CreateDirectory(Path.GetDirectoryName(_path)!);Load();Refresh();}
 void Refresh(){ScoreText.Text=_state.Score.ToString("N0");XpText.Text=_state.Xp.ToString("N0");ExpeditionText.Text=$"{_state.Expedition}%";ChapterText.Text=_state.Chapter.ToString();PlayTimeText.Text=$"{_state.PlayTime / 60}m";}
 void Explore_Click(object s,RoutedEventArgs e){_state.Score+=500;_state.Xp+=150;_state.PlayTime+=60;if(_state.Xp>=_state.Chapter*1000)_state.Chapter++;if(_state.Expedition<100)_state.Expedition++;Refresh();}
 void Save_Click(object s,RoutedEventArgs e){Save();MessageBox.Show("Game state saved locally.","BizXtreme",MessageBoxButton.OK,MessageBoxImage.Information);}
 void Resume_Click(object s,RoutedEventArgs e){Load();Refresh();}
 void Hall_Click(object s,RoutedEventArgs e){MessageBox.Show($"Current local score: {_state.Score:N0}\nHall of Fame data is stored per user profile.","BizXtreme");}
 void Discover_Click(object s,RoutedEventArgs e){MessageBox.Show("Player discovery uses opt-in peer identifiers. Raw IP addresses are not persisted or scanned.","BizXtreme P2P");}
 void Save(){using var stream=File.Create(_path);new DataContractJsonSerializer(typeof(GameState)).WriteObject(stream,_state);}
 void Load(){try{using var stream=File.OpenRead(_path);_state=(GameState)new DataContractJsonSerializer(typeof(GameState)).ReadObject(stream)!;}catch{_state=new();}}
}
