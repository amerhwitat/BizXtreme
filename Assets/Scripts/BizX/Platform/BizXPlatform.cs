using UnityEngine;

namespace BizX.Platform
{
    public enum BizXPlatformKind { Unknown, Windows, MacOS, Linux, Android, IOS, WebGL }

    public static class BizXPlatform
    {
        public static BizXPlatformKind Current
        {
            get
            {
#if UNITY_WEBGL
                return BizXPlatformKind.WebGL;
#elif UNITY_ANDROID
                return BizXPlatformKind.Android;
#elif UNITY_IOS
                return BizXPlatformKind.IOS;
#elif UNITY_STANDALONE_WIN
                return BizXPlatformKind.Windows;
#elif UNITY_STANDALONE_OSX
                return BizXPlatformKind.MacOS;
#elif UNITY_STANDALONE_LINUX
                return BizXPlatformKind.Linux;
#else
                return BizXPlatformKind.Unknown;
#endif
            }
        }

        public static bool SupportsTouch =>
#if UNITY_ANDROID || UNITY_IOS
            true;
#else
            false;
#endif

        public static string PersistentDataPath => Application.persistentDataPath;
    }
}
