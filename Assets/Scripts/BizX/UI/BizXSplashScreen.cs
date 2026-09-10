using System.Collections;
using UnityEngine;
using UnityEngine.UI;

namespace BizX.UI
{
    /// <summary>Displays the packaged BizXtreme/Aurora Frontier splash before the main menu.</summary>
    public sealed class BizXSplashScreen : MonoBehaviour
    {
        [SerializeField] private RawImage image;
        [SerializeField] private CanvasGroup canvasGroup;
        [SerializeField] private float minimumSeconds = 2.0f;

        private IEnumerator Start()
        {
            var texture = Resources.Load<Texture2D>("BizXtremeSplash");
            if (texture != null && image != null) image.texture = texture;
            yield return new WaitForSeconds(minimumSeconds);
            if (canvasGroup != null)
            {
                float t = 0;
                while (t < .6f)
                {
                    t += Time.unscaledDeltaTime;
                    canvasGroup.alpha = 1f - Mathf.Clamp01(t / .6f);
                    yield return null;
                }
            }
            gameObject.SetActive(false);
        }
    }
}
