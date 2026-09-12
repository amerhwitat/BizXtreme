import 'dart:collection';

enum PlayerPresence { queued, invited, ready, playing, disconnected, eliminated }
enum SessionChannel { game, chat, voice }
class SessionPlayer { SessionPlayer({required this.id, required this.name, this.priority = 0, this.presence = PlayerPresence.queued, this.joinedAt = 0}); final String id; final String name; int priority; PlayerPresence presence; final int joinedAt; }
class GameSession {
  GameSession({required this.gameId, this.seats = 2, this.disconnectGraceSeconds = 15});
  final String gameId; final int seats; final int disconnectGraceSeconds; final List<SessionPlayer> players = []; final Queue<SessionPlayer> queue = Queue<SessionPlayer>();
  List<SessionPlayer> get activePlayers => players.where((p) => p.presence == PlayerPresence.playing || p.presence == PlayerPresence.ready).toList();
  List<SessionPlayer> get prioritizedQueue => queue.toList()..sort((a,b) => b.priority != a.priority ? b.priority.compareTo(a.priority) : a.joinedAt.compareTo(b.joinedAt));
  void invite(SessionPlayer p) { p.presence = PlayerPresence.invited; players.add(p); }
  void enqueue(SessionPlayer p) { p.presence = PlayerPresence.queued; queue.add(p); }
  bool admitNext() { if (activePlayers.length >= seats || queue.isEmpty) return false; final p = prioritizedQueue.first; queue.remove(p); p.presence = PlayerPresence.playing; players.add(p); return true; }
  bool disconnect(String id) { final p = _find(id); if (p == null || p.presence != PlayerPresence.playing) return false; p.presence = PlayerPresence.disconnected; return true; }
  bool forfeit(String id) { final p = _find(id); if (p == null || p.presence != PlayerPresence.disconnected) return false; p.presence = PlayerPresence.eliminated; return true; }
  void startNextRound() { players.removeWhere((p) => p.presence == PlayerPresence.eliminated || p.presence == PlayerPresence.disconnected); while (activePlayers.length < seats && admitNext()) {} }
  SessionPlayer? _find(String id) => players.where((p) => p.id == id).firstOrNull;
}
extension<T> on Iterable<T> { T? get firstOrNull => isEmpty ? null : first; }
