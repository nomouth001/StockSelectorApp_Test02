self.addEventListener('install', event => {
  console.log('[ServiceWorker] 설치 완료');
  self.skipWaiting();
});
self.addEventListener('fetch', event => {
  return;
});
