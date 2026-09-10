using System;
using UnityEngine;

namespace BizX.Game
{
    [Serializable]
    public sealed class BizXGameSnapshot
    {
        public int schema = 1;
        public string chapter = "chapter_01";
        public int score;
        public int xp;
        public float expedition;
        public float playTimeSeconds;
        public string savedAtUtc;
    }

    /// <summary>Local persistent save/resume record. Cloud/P2P sync can be layered above this contract.</summary>
    public static class GameSaveService
    {
        private const string SaveKey = "bizxtreme.save.v1";

        public static void Save(BizXGameSnapshot snapshot)
        {
            snapshot.savedAtUtc = DateTime.UtcNow.ToString("O");
            PlayerPrefs.SetString(SaveKey, JsonUtility.ToJson(snapshot));
            PlayerPrefs.Save();
        }

        public static bool TryLoad(out BizXGameSnapshot snapshot)
        {
            snapshot = null;
            if (!PlayerPrefs.HasKey(SaveKey)) return false;
            try
            {
                snapshot = JsonUtility.FromJson<BizXGameSnapshot>(PlayerPrefs.GetString(SaveKey));
                return snapshot != null;
            }
            catch (Exception ex)
            {
                Debug.LogWarning($"BizX save load failed: {ex.Message}");
                return false;
            }
        }

        public static void Clear() { PlayerPrefs.DeleteKey(SaveKey); PlayerPrefs.Save(); }
    }
}
