import { createRouter, createWebHistory } from 'vue-router'
import title from "@/views/title.vue";
import LoginView from "@/views/LoginView";
import dataView from "@/views/dataView/dataView.vue";
import AddTableView from "@/views/AddTableView.vue";
import dataView1 from "@/views/dataView/dataView1.vue";
import dataView2 from "@/views/dataView/dataView2.vue";
import dataView3 from "@/views/dataView/dataView3.vue";
import dataView4 from "@/views/dataView/dataView4.vue";
import dataView5 from "@/views/dataView/dataView5.vue";
import userDataView1 from "@/views/userDataView/userDataView1.vue";
import userDataView2 from "@/views/userDataView/userDataView2.vue";
import userDataView3 from "@/views/userDataView/userDataView3.vue";
import userDataView4 from "@/views/userDataView/userDataView4.vue";
import userDataView5 from "@/views/userDataView/userDataView5.vue";
import userDataView from "@/views/userDataView/userDataView.vue";

const routes = [
  {
    path: '/',
    name: 'title',
    component: title
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/data',
    component: dataView
  },
  {
    path: '/addTable',
    name: 'addTable',
    component: AddTableView
  },
  {
    path: '/userData',
    name: 'userData',
    component: userDataView
  },
  {
    path: '/userData1',
    name: 'userData1',
    component: userDataView1
  },
  {
    path: '/userData2',
    name: 'userData2',
    component: userDataView2
  },
  {
    path: '/userData3',
    name: 'userData3',
    component: userDataView3
  },
  {
    path: '/userData4',
    name: 'userData4',
    component: userDataView4
  },
  {
    path: '/userData5',
    name: 'userData5',
    component: userDataView5
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
