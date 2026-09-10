using UnityEngine;

namespace BizX.Game
{
    /// <summary>Dashboard-facing KPI model shared by Unity UI and future native/web clients.</summary>
    public sealed class BizXDashboardController : MonoBehaviour
    {
        [SerializeField] private string playerName = "Explorer";
        public int Score { get; private set; }
        public int XP { get; private set; }
        public float ExpeditionProgress { get; private set; }
        public float PlayTimeSeconds { get; private set; }
        public int PeerCount { get; private set; }
        public int BestRank { get; private set; }

        public void ApplySnapshot(BizXGameSnapshot snapshot)
        {
            if (snapshot == null) return;
            Score = snapshot.score;
            XP = snapshot.xp;
            ExpeditionProgress = Mathf.Clamp01(snapshot.expedition);
            PlayTimeSeconds = Mathf.Max(0, snapshot.playTimeSeconds);
        }

        public void SaveCurrent()
        {
            GameSaveService.Save(new BizXGameSnapshot
            {
                chapter = "chapter_01",
                score = Score,
                xp = XP,
                expedition = ExpeditionProgress,
                playTimeSeconds = PlayTimeSeconds
            });
        }

        public void ResumeLatest()
        {
            if (GameSaveService.TryLoad(out var snapshot)) ApplySnapshot(snapshot);
        }

        public string PlayerName => playerName;
    }
}
