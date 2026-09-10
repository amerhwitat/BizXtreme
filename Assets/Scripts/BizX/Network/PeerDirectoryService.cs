using System;
using System.Collections.Generic;
using UnityEngine;

namespace BizX.Network
{
    [Serializable]
    public sealed class PeerDirectoryEntry
    {
        public string peerId;
        public string displayName;
        public string lastSeen;
        public string networkHint;
        public List<string> capabilities = new List<string>();
    }

    /// <summary>
    /// Opt-in discovery contract for connected BizXtreme users.
    /// Raw IP addresses are deliberately not persisted by the game client.
    /// A directory may return pseudonymous peer IDs and a relay/direct hint.
    /// </summary>
    public sealed class PeerDirectoryService : MonoBehaviour
    {
        [SerializeField] private string directoryUrl;
        public string DirectoryUrl => directoryUrl;
        public bool Enabled => !string.IsNullOrWhiteSpace(directoryUrl);

        public void SetDirectoryUrl(string url) => directoryUrl = url?.Trim() ?? string.Empty;

        public PeerDirectoryEntry[] ParseResponse(string json)
        {
            if (string.IsNullOrWhiteSpace(json)) return Array.Empty<PeerDirectoryEntry>();
            var wrapper = JsonUtility.FromJson<PeerDirectoryWrapper>(json);
            return wrapper?.users ?? Array.Empty<PeerDirectoryEntry>();
        }

        [Serializable]
        private sealed class PeerDirectoryWrapper
        {
            public PeerDirectoryEntry[] users;
        }
    }
}
