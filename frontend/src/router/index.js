import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Project from '../views/Project.vue';

Vue.use(VueRouter);

  const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/login', name: 'Login', component: Login },
    { path: '/project', name: 'Project', component: Project },
  ];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior () {
    return { x: 0, y: 0 };
  },
});

export default router;
