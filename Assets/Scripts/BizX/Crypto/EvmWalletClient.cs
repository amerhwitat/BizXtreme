using System;
using System.Runtime.InteropServices;
using UnityEngine;

namespace BizX.Crypto
{
    public sealed class EvmWalletClient : MonoBehaviour
    {
#if UNITY_WEBGL && !UNITY_EDITOR
        [DllImport("__Internal")] private static extern void BizXWalletConnect(string gameObject, string callback);
        [DllImport("__Internal")] private static extern void BizXWalletBalance(string address, string callback);
        [DllImport("__Internal")] private static extern void BizXWalletSend(string txJson, string callback);
#endif

        public event Action<string> Connected;
        public event Action<string> BalanceReceived;
        public event Action<string> TransactionSubmitted;

        public void Connect()
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            BizXWalletConnect(gameObject.name, nameof(OnWalletConnected));
#else
            Debug.Log("EVM wallet connection is available through the platform wallet adapter.");
#endif
        }

        public void GetNativeBalance(string address)
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            BizXWalletBalance(address, nameof(OnBalance));
#else
            Debug.LogWarning("Use a native/mobile wallet adapter for non-WebGL builds.");
#endif
        }

        public void SendNative(string from, string to, string valueWei, string chainIdHex)
        {
            var tx = $"{{\"from\":\"{from}\",\"to\":\"{to}\",\"value\":\"{valueWei}\",\"chainId\":\"{chainIdHex}\"}}";
#if UNITY_WEBGL && !UNITY_EDITOR
            BizXWalletSend(tx, nameof(OnTransaction));
#else
            Debug.LogWarning("Native/mobile builds must delegate signing to their wallet provider.");
#endif
        }

        public void OnWalletConnected(string address) { Connected?.Invoke(address); }
        public void OnBalance(string json) { BalanceReceived?.Invoke(json); }
        public void OnTransaction(string result) { TransactionSubmitted?.Invoke(result); }
    }
}
