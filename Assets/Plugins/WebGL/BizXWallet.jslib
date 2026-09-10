mergeInto(LibraryManager.library, {
  BizXWalletConnect: function (gameObjectPtr, callbackPtr) {
    const gameObject = UTF8ToString(gameObjectPtr);
    const callback = UTF8ToString(callbackPtr);
    window.BizXUnityGameObject = gameObject;
    const provider = window.ethereum;
    if (!provider) {
      SendMessage(gameObject, callback, JSON.stringify({ ok:false, error:'No EVM wallet provider detected' }));
      return;
    }
    provider.request({ method: 'eth_requestAccounts' })
      .then(accounts => SendMessage(gameObject, callback, accounts[0] || ''))
      .catch(err => SendMessage(gameObject, callback, JSON.stringify({ ok:false, error:String(err && err.message || err) })));
  },

  BizXWalletBalance: function (addressPtr, callbackPtr) {
    const address = UTF8ToString(addressPtr);
    const callback = UTF8ToString(callbackPtr);
    const provider = window.ethereum;
    if (!provider) return;
    provider.request({ method:'eth_getBalance', params:[address, 'latest'] })
      .then(balance => SendMessage(window.BizXUnityGameObject || '', callback, JSON.stringify({ ok:true, address, balanceWei:balance })))
      .catch(err => SendMessage(window.BizXUnityGameObject || '', callback, JSON.stringify({ ok:false, error:String(err && err.message || err) })));
  },

  BizXWalletSend: function (txPtr, callbackPtr) {
    const txJson = UTF8ToString(txPtr);
    const callback = UTF8ToString(callbackPtr);
    const provider = window.ethereum;
    if (!provider) return;
    let tx;
    try { tx = JSON.parse(txJson); } catch (e) {
      SendMessage(window.BizXUnityGameObject || '', callback, JSON.stringify({ ok:false, error:'Invalid transaction JSON' }));
      return;
    }
    provider.request({ method:'eth_sendTransaction', params:[tx] })
      .then(hash => SendMessage(window.BizXUnityGameObject || '', callback, JSON.stringify({ ok:true, txHash:hash })))
      .catch(err => SendMessage(window.BizXUnityGameObject || '', callback, JSON.stringify({ ok:false, error:String(err && err.message || err) })));
  }
});
