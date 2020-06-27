import 'babel-polyfill';

import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import './plugins/axios';
import './plugins/elementUI';
import './plugins/vueScroll';
import './plugins/Backtop';
import './plugins/markdownEditor';

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
