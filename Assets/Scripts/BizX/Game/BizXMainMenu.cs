using System;
using UnityEngine;

namespace BizX.Game
{
    /// <summary>Platform-neutral main menu controller. Dashboard, persistence and social discovery are optional UI layers.</summary>
    public sealed class BizXMainMenu : MonoBehaviour
    {
        public event Action<string> MenuActionRequested;

        public void Play() => Request("play");
        public void ContinueGame() => Request("continue");
        public void Dashboard() => Request("dashboard");
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
