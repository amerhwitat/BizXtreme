using System;
using UnityEngine;

namespace BizX.Game
{
    /// <summary>
    /// Platform-neutral main menu controller. Wire these actions to Unity UI buttons.
    /// The original game remains the primary Play path; commerce and wallet features are secondary systems.
    /// </summary>
    public sealed class BizXMainMenu : MonoBehaviour
    {
        public event Action<string> MenuActionRequested;

        public void Play() => Request("play");
        public void ContinueGame() => Request("continue");
        public void Missions() => Request("missions");
        public void Events() => Request("events");
        public void Inventory() => Request("inventory");
        public void Marketplace() => Request("marketplace");
        public void Wallet() => Request("wallet");
        public void BackupWallet() => Request("wallet.backup");
        public void Receive() => Request("wallet.receive");
        public void Send() => Request("wallet.send");
        public void Settings() => Request("settings");

        private void Request(string action)
        {
            MenuActionRequested?.Invoke(action);
            Debug.Log($"BizX menu action: {action}");
        }
    }
}
