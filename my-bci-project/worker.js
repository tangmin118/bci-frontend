// Web Worker：在后台线程中运行定时器，不受浏览器标签页切换影响
let intervalId = null;

self.onmessage = function(e) {
    if (e.data.action === 'start') {
        const interval = e.data.interval || 20;
        // 清除旧的定时器，防止重复
        if (intervalId) clearInterval(intervalId);
        // 启动新的定时器，按指定间隔发送 tick 消息
        intervalId = setInterval(() => {
            self.postMessage({ type: 'tick' });
        }, interval);
    } else if (e.data.action === 'stop') {
        if (intervalId) {
            clearInterval(intervalId);
            intervalId = null;
        }
    }
};
