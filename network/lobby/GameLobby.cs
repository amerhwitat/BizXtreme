namespace BizXtreme.Network;

public enum PlayerState { Queued, Invited, Ready, Playing, Disconnected, Eliminated }
public enum ChannelKind { Game, Chat, Voice }

public sealed record LobbyPlayer(string PlayerId, string DisplayName, int Priority = 0, PlayerState State = PlayerState.Queued, long JoinedAt = 0);
public sealed record LobbyConfig(string GameId, int Seats = 2, bool AllowVoice = true, bool AllowChat = true, int DisconnectTimeoutSeconds = 15);

public sealed class GameLobby
{
    private readonly LobbyConfig _config;
    private readonly List<LobbyPlayer> _players = [];
    private readonly List<LobbyPlayer> _queue = [];
    public GameLobby(LobbyConfig config) => _config = config;
    public IReadOnlyList<LobbyPlayer> Players => _players;
    public IReadOnlyList<LobbyPlayer> Queue => _queue.OrderByDescending(x => x.Priority).ThenBy(x => x.JoinedAt).ToList();
    public void Invite(LobbyPlayer p) => _players.Add(p with { State = PlayerState.Invited });
    public void Enqueue(LobbyPlayer p) { _queue.Add(p with { State = PlayerState.Queued }); SortQueue(); }
    public void SetPriority(string id, int priority) { var i = _queue.FindIndex(x => x.PlayerId == id); if (i >= 0) _queue[i] = _queue[i] with { Priority = priority }; SortQueue(); }
    public bool AdmitNext() { if (ActiveCount() >= _config.Seats || _queue.Count == 0) return false; var p = _queue[0]; _queue.RemoveAt(0); _players.Add(p with { State = PlayerState.Playing }); return true; }
    public bool MarkDisconnected(string id) => Change(id, PlayerState.Playing, PlayerState.Disconnected);
    public bool ForfeitDisconnected(string id) => Change(id, PlayerState.Disconnected, PlayerState.Eliminated);
    public void StartNextRound() { _players.RemoveAll(x => x.State is PlayerState.Eliminated or PlayerState.Disconnected); while (ActiveCount() < _config.Seats && AdmitNext()) { } }
    public int ActiveCount() => _players.Count(x => x.State is PlayerState.Playing or PlayerState.Ready);
    private bool Change(string id, PlayerState from, PlayerState to) { var i = _players.FindIndex(x => x.PlayerId == id && x.State == from); if (i < 0) return false; _players[i] = _players[i] with { State = to }; return true; }
    private void SortQueue() { _queue.Sort((a,b) => b.Priority != a.Priority ? b.Priority.CompareTo(a.Priority) : a.JoinedAt.CompareTo(b.JoinedAt)); }
}
