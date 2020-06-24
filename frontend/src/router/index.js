import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Project from '../views/Project.vue';
import Admin from '../views/Admin.vue';

Vue.use(VueRouter);

  const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/project', name: 'Project', component: Project },
    { path: '/admin', name: 'Admin', component: Admin },
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
